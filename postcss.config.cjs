// postcss.config.cjs
module.exports = {
  plugins: [
    require('cssnano')({
      preset: ['advanced', {
        mergeRules: true,        // merge duplicated selectors
        discardDuplicates: true, // remove duplicated properties
        reduceIdents: true,      // shorten keyframe names
        mergeLonghand: true,     // combine longhand properties
      }],
    }),
  ],
};

