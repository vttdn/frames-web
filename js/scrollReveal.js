document.addEventListener("DOMContentLoaded", function () {
  const words = document.querySelectorAll(".staticTxt span");
  let revealedCount = 7; // Number of words initially revealed
  let scrollThreshold = 5; // Scroll amount needed to reveal the next word
  let accumulatedScroll = 0;
  let isLastWordRevealed = false; // Flag to track if the last word is revealed

  const revealNextWord = () => {
    if (revealedCount < words.length) {
      words[revealedCount].classList.add("revealed");
      revealedCount++;
      accumulatedScroll = 0; // Reset accumulated scroll after revealing a word
    } else {
      isLastWordRevealed = true; // Mark that the last word has been revealed
    }
  };

  const hidePreviousWord = () => {
    if (revealedCount > 7) {
      revealedCount--;
      words[revealedCount].classList.remove("revealed");
      accumulatedScroll = 0; // Reset accumulated scroll after hiding a word
    }
  };

  const resetReveal = () => {
    for (let i = 7; i < words.length; i++) {
      words[i].classList.remove("revealed");
    }
    revealedCount = 7;
    isLastWordRevealed = false; // Reset the flag
  };

  // Initially reveal the first six words
  for (let i = 0; i < revealedCount; i++) {
    words[i].classList.add("revealed");
  }

  let lastScrollY = window.scrollY;
  window.addEventListener("scroll", () => {
    const scrollY = window.scrollY;
    const scrollDirection = scrollY - lastScrollY;
    const atBottom = scrollY + window.innerHeight >= document.documentElement.scrollHeight;

    accumulatedScroll += Math.abs(scrollDirection);

    // Prevent revealing more words once the last word is revealed and we reach the bottom
    if (isLastWordRevealed && atBottom) {
      return; // Prevent any further word reveals if at the bottom and last word is revealed
    }

    // Reveal the next word if scrolling down and threshold is met
    if (scrollDirection > 0 && accumulatedScroll >= scrollThreshold) {
      revealNextWord();
    }

    // Reverse the animation by hiding the previous word if scrolling up and threshold is met
    else if (scrollDirection < 0 && accumulatedScroll >= scrollThreshold && !atBottom) {
      hidePreviousWord();
    }

    // Reset to initial state if scrolled to the top or overshoots
    if (scrollY <= 0) {
      resetReveal();
    }

    lastScrollY = scrollY;
  });
});