# Implementation Plan for SAPCO Subscription Website

## 1. Architecture & Technology Stack
- **Backend:** Node.js with Express for REST API
- **Frontend:** React (create-react-app) served via Nginx
- **Database:** PostgreSQL hosted on AWS RDS
- **Hosting:** AWS Elastic Beanstalk or EC2 for the application servers
- **Storage:** S3 for document assets
- **Authentication:** JSON Web Tokens (JWT) with bcrypt password hashing
- **Billing:** Stripe subscriptions with three tiers (Single Form, Multi Form, Unlimited)
- **Permissions:** Role-based access control (RBAC) enforced in middleware
- **Watermarking:** Dynamic 3D watermark overlay on PDFs using `pdf-lib`; user ID and timestamp embedded. Audit logs stored for every download.
- **Security:** HTTPS (TLS 1.2+), HSTS, Content Security Policy, rate limiting, helmet middleware.

## 2. Major Steps
1. **Project setup** – Initialize backend and frontend repositories; configure ESLint/Prettier.
2. **Database schema** – Create tables for users, roles, permissions, forms, subscriptions, audit logs.
3. **Authentication module** – Implement registration and login endpoints with JWT.
4. **Subscription billing** – Integrate Stripe, create products/plans, handle webhooks for subscription status.
5. **Form management** – CRUD APIs for evaluation forms with file upload to S3.
6. **PDF generation** – Generate filled PDFs on demand; apply 3D watermark from server.
7. **Audit logging** – Middleware to record user actions (view, download, update) with timestamp/IP.
8. **Frontend pages** – Build React components for Home, About, Subscribe, Legal, Contact.
9. **Access control** – Protect routes by role, ensure forms only accessible with valid license count.
10. **Testing & QA** – Unit and integration tests, security review, performance profiling.
11. **Deployment** – Provision AWS resources, configure CI/CD, set up domain and SSL.
12. **Monitoring & Backups** – CloudWatch metrics, daily database snapshots, off-site backups.

## 3. Competitor Analysis
- **TeachPoint (Vector Solutions):** Offers educator evaluations, multiple form types, robust reporting. Subscription tiers by district size.
- **TalentEd Perform:** Comprehensive compliance platform for K-12. Tiers based on feature modules and number of administrators.
- **SchoolMint:** Provides evaluation templates and HR tools with scaling licenses.

SAPCO should mirror this approach by naming tiers:
1. **Essential** – single evaluation form license.
2. **Professional** – up to 15 evaluation licenses.
3. **Enterprise** – unlimited evaluations and priority support.

## 4. Security Considerations
- Enforce TLS everywhere and redirect HTTP to HTTPS.
- Implement strong password policies and MFA for administrators.
- Use Stripe's client-side tokenization to avoid handling raw card data.
- Use S3 pre-signed URLs for secure, expiring access to files.
- Disable printing/screenshotting via PDF security settings and custom JavaScript overlays (best-effort; no perfect prevention).

## 5. Milestones & Timeline
1. Requirements & design – 1 week
2. MVP backend & database – 2 weeks
3. Frontend screens & auth – 2 weeks
4. Billing integration – 1 week
5. PDF generation with watermark – 1 week
6. Final QA, deployment, SEO – 1 week

_Total: ~8 weeks for initial launch._
