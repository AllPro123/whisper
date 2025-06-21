const express = require('express');
const app = express();
const authRoutes = require('./routes/auth');
const billingRoutes = require('./routes/billing');
const formsRoutes = require('./routes/forms');
const helmet = require('helmet');
const morgan = require('morgan');

app.use(express.json());
app.use(helmet());
app.use(morgan('combined'));

app.use('/api/auth', authRoutes);
app.use('/api/billing', billingRoutes);
app.use('/api/forms', formsRoutes);

app.listen(3000, () => console.log('Server running on port 3000'));
