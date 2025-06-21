const router = require('express').Router();
const stripe = require('stripe')(process.env.STRIPE_SECRET);

// POST /api/billing/checkout
router.post('/checkout', async (req, res) => {
  const { priceId } = req.body;
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    mode: 'subscription',
    line_items: [{ price: priceId, quantity: 1 }],
    success_url: process.env.DOMAIN + '/success',
    cancel_url: process.env.DOMAIN + '/cancel'
  });
  res.json({ url: session.url });
});

module.exports = router;
