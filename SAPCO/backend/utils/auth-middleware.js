const jwt = require('jsonwebtoken');

function requireRole(role) {
  return (req, res, next) => {
    const auth = req.headers.authorization;
    if (!auth) return res.status(401).end();
    try {
      const token = auth.split(' ')[1];
      const payload = jwt.verify(token, process.env.JWT_SECRET);
      if (payload.role !== role) return res.status(403).end();
      req.user = payload;
      next();
    } catch (err) {
      return res.status(401).end();
    }
  };
}

module.exports = { requireRole };
