let express = require('express');
let router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', {title: 'Form validation', success: req.session.success, errors: req.session.errors});
    req.session.errors = null;
});

router.post('/submit', function(req, res, next) {
  // check validity
    req.check('email', 'invalid email address').isEmail();
    req.check('password', 'password is invalid').isLength({min: 4}).equals(req.body.confirmPassword);

    let errors = req.validationErrors();
    if (errors) {
        req.session.errors = errors;
        req.session.success = false;
    } else {
        req.session.success = true;
    }
    res.redirect('/');
});

module.exports = router;
