const logs = [];

module.exports.record = async function(userId, action) {
  logs.push({ userId, action, at: new Date() });
  console.log('AUDIT', userId, action);
};
