const router = require('express').Router();
const { requireRole } = require('../utils/auth-middleware');
const pdfLib = require('pdf-lib');
const fs = require('fs');
const AuditLog = require('../models/auditLog');

// GET /api/forms/:id/download
router.get('/:id/download', requireRole('admin'), async (req, res) => {
  const pdfBytes = fs.readFileSync('path/to/template.pdf');
  const pdfDoc = await pdfLib.PDFDocument.load(pdfBytes);
  const watermark = await pdfDoc.embedText(`User: ${req.user.id}  Time: ${new Date().toISOString()}`);
  const pages = pdfDoc.getPages();
  pages[0].drawText('SAPCO', { x: 50, y: 50, size: 12, font: watermark });
  const output = await pdfDoc.save();

  await AuditLog.record(req.user.id, `download form ${req.params.id}`);
  res.setHeader('Content-Type', 'application/pdf');
  res.send(output);
});

module.exports = router;
