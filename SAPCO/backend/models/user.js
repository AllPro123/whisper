// Placeholder user model using in-memory users for demo
const users = [
  { id: 1, email: 'admin@example.com', password_hash: '$2b$10$hash', role: 'admin' }
];

module.exports.findByEmail = async function(email) {
  return users.find(u => u.email === email);
};
