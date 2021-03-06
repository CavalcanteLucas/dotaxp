module.exports = {
    "root": true,
    "parserOptions": {
        "parser": "babel-eslint"
    },
    "plugins": ["vue"],
    "settings": {
        "html/html-extensions": [".html"]
    },
    "globals": {
        "axios": true,
        "elastic": true
    },
    "extends": [
        "eslint:recommended",
        "plugin:vue/recommended"
    ],
    "rules": {
        "curly": ["error", "all"],
        "comma-dangle": ["error", "only-multiline"],
        "camelcase": ["error", {"properties": "never"}],
        "indent": ["error", 4, {"SwitchCase": 1}],
        "object-curly-spacing": ["error", "never"],
        "space-before-function-paren": ["error", "never"],
        "space-before-blocks": ["error", "always"],
        "space-infix-ops": ["error", {"int32Hint": false}],
        "no-alert": "error",
        "no-dupe-args": "error",
        "no-duplicate-case": "error",
        "no-duplicate-imports": "error",
        "no-empty": "error",
        "no-unused-vars": "off",
        "no-undef": "off",
        "no-debugger": "off",
    },
    "env": {
        "browser": true,
        "node": true,
        "commonjs": true,
        "es6": true
    }
}