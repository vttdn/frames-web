// --- Constants ---
const MIN_RADIUS = 1;
const MAX_RADIUS = 16;
const DEPTH = 2;
const NUM_POINTS_INNER = 2500;
const NUM_POINTS_OUTER = 875; // 3500 / 4
const LEFT_COLOR = "D01D41";
const RIGHT_COLOR = "8b5cf6";

// --- Scene Setup ---
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x101010);

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(-1, -1.5, -2);
camera.fov = 60; // A larger FOV for a more zoomed-out effect
camera.updateProjectionMatrix();
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// --- Lights ---
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5); // Reduce intensity
scene.add(directionalLight);

const pointLight = new THREE.PointLight(0xffffff, 1); // Reduce power from 10
pointLight.position.set(-30, 0, -30);
scene.add(pointLight);

// --- Orbit Controls ---
const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.minDistance = 20;
controls.maxDistance = 20;

// --- Color Gradient Function ---
const getGradientStop = (ratio) => {
    ratio = Math.max(0, Math.min(1, ratio)); // Clamp between 0 and 1

    const c0 = LEFT_COLOR.match(/.{1,2}/g).map(oct => parseInt(oct, 16) * (1 - ratio));
    const c1 = RIGHT_COLOR.match(/.{1,2}/g).map(oct => parseInt(oct, 16) * ratio);
    const ci = [0, 1, 2].map(i => Math.min(Math.round(c0[i] + c1[i]), 255));

    // Ensure hex has 6 digits
    return `#${ci.map(c => c.toString(16).padStart(2, "0")).join("")}`;
};

const calculateColor = (x) => {
    const maxDiff = MAX_RADIUS * 2;
    const distance = x + MAX_RADIUS;

    const ratio = distance / maxDiff;

    const stop = getGradientStop(ratio);
    return stop;
};

const randomFromInterval = (min, max) => {
    return Math.random() * (max - min) + min;
};

// --- Particle Creation ---
function createSquareParticle(position, hexColor) {
    const color = new THREE.Color(hexColor); // Convert to THREE.Color
    const geometry = new THREE.PlaneGeometry(0.1, 0.1);
    const material = new THREE.MeshStandardMaterial({
        color: color, 
        emissive: color, 
        emissiveIntensity: 0.25, 
        side: THREE.DoubleSide, 
        roughness: 0.5,
    });
    const square = new THREE.Mesh(geometry, material);
    square.position.set(...position);
    square.rotation.z = Math.PI / 4;
    return square;
}

const ring = new THREE.Group();

// Move the ring group to the right by adjusting its X position
ring.position.x = 3; // Adjust this value to move the object more to the right
ring.position.y = 5;

// --- Generate Inner Ring Particles ---
for (let i = 0; i < NUM_POINTS_INNER; i++) {
    const randomRadius = randomFromInterval(MIN_RADIUS, MAX_RADIUS);
    const angle = Math.random() * Math.PI * 2;
    const x = Math.cos(angle) * randomRadius;
    const y = Math.sin(angle) * randomRadius;
    const z = randomFromInterval(-DEPTH, DEPTH);
    const color = calculateColor(x);
    const square = createSquareParticle([x, y, z], color);
    ring.add(square);
}

// --- Generate Outer Ring Particles ---
for (let i = 0; i < NUM_POINTS_OUTER; i++) {
    const randomRadius = randomFromInterval(MIN_RADIUS / 2, MAX_RADIUS * 2);
    const angle = Math.random() * Math.PI * 2;
    const x = Math.cos(angle) * randomRadius;
    const y = Math.sin(angle) * randomRadius;
    const z = randomFromInterval(-DEPTH * 10, DEPTH * 10);
    const color = calculateColor(x);
    const square = createSquareParticle([x, y, z], color);
    ring.add(square);
}

scene.add(ring);

// --- Animation Loop ---
const clock = new THREE.Clock();

function animate() {
    requestAnimationFrame(animate);
    ring.rotation.z = clock.getElapsedTime() * 0.05;
    controls.update();
    renderer.render(scene, camera);
}

animate();

// --- Handle Window Resize ---
window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
