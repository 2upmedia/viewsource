module.exports = {
  files: {
    javascripts: {
      joinTo: {
        'vendor.js': /^(?!app)/,
        'app.js': /^app/
      }
    },
    stylesheets: {
      joinTo: 'app.css'
    }
  },
  npm: {
    globals: {jQuery: 'jquery'}
  },
  plugins: {
    babel: {presets: ['es2015']},
    sass: {
      options: {
        includePaths: ['node_modules/foundation-sites/scss', 'node_modules/motion-ui/src', 'node_modules/highlight.js/styles']
      }
    }
  }
};
