# IT SERVICE AGREEMENT
## Enterprise Template — Germany & EU | Version 1.0

> **HOW TO USE THIS TEMPLATE**
> Drafting notes appear in `[DRAFTING NOTE: ...]` blocks throughout.
> Alternative clauses for different risk profiles, sector-specific requirements, or opposing counsel positions are marked `[OPTION A]`, `[OPTION B]`, `[FALLBACK]`.
> Mandatory provisions under German or EU law are marked `[MANDATORY]`.
> Clauses requiring particularization are marked `[SPECIFY]`.
> This template is governed by German law with references to applicable EU regulations.
> **Last regulatory review:** February 2026 (covers GDPR, NIS2 Directive / BSIG 2023, EU AI Act 2024, Data Act 2023, DORA 2023 where applicable, Digital Services Act, EU Cyber Resilience Act 2024).

---

# IT SERVICE AGREEMENT

**This IT Service Agreement** ("**Agreement**") is entered into as of **[DATE]** ("**Effective Date**")

**between**

**[FULL LEGAL NAME OF SERVICE PROVIDER]**, a company incorporated under the laws of **[GERMANY / OTHER JURISDICTION]**, registered with the commercial register (*Handelsregister*) of **[COURT]** under registration number **[HRB NUMBER]**, with its registered seat at **[ADDRESS]**, VAT ID (*Umsatzsteuer-Identifikationsnummer*): **[VAT ID]**
("**Service Provider**" or "**SP**")

**and**

**[FULL LEGAL NAME OF CUSTOMER]**, a company incorporated under the laws of **[GERMANY / OTHER JURISDICTION]**, registered with the commercial register of **[COURT]** under registration number **[HRB NUMBER]**, with its registered seat at **[ADDRESS]**, VAT ID: **[VAT ID]**
("**Customer**")

Service Provider and Customer are each a "**Party**" and together the "**Parties**."

> **[DRAFTING NOTE — PARTIES]:** Verify correct legal entity names and registration details. For non-German entities, add a branch/representative clause if contracting through a German branch. If Customer is a public body (*öffentliche Hand*), consider including a public procurement compliance clause and confirm that award procedures (VgV/VOB/UVgO) have been completed. For group structures, define affiliates separately and decide whether affiliates may order services under this framework (see Section 3.4).

---

## RECITALS

WHEREAS, the Service Provider is in the business of providing IT services, including **[BRIEF DESCRIPTION]**;

WHEREAS, the Customer desires to obtain such IT services from the Service Provider on the terms and conditions set forth herein;

NOW, THEREFORE, in consideration of the mutual covenants and agreements set forth herein, the Parties agree as follows:

---

## PART I — GENERAL TERMS

---

### Section 1 — DEFINITIONS

In this Agreement, the following terms have the meanings set out below. Additional defined terms may be set out in Schedules.

1.1 **"Affiliate"** means any entity that directly or indirectly controls, is controlled by, or is under common control with a Party, where "control" means the ownership of more than fifty percent (50%) of the voting shares or equivalent controlling interest.

1.2 **"AI Components"** means any functionality within the Services that uses machine learning, generative AI, large language models, or other artificial intelligence techniques, as specified in the relevant Service Schedule.

> **[DRAFTING NOTE — AI COMPONENTS]:** The EU AI Act (Regulation (EU) 2024/1689) applies from 2 August 2026 (most provisions; prohibited AI systems from 2 February 2025; GPAI provisions from 2 August 2025). If the Services include AI Components, classify them by risk level (prohibited / high-risk / limited-risk / minimal-risk) and include obligations per Section 21 of this Agreement. Consider whether the Service Provider acts as "provider" or "deployer" under the AI Act.

1.3 **"Applicable Law"** means all laws, regulations, regulatory guidance, judicial decisions, and binding standards applicable to the respective Party or the Services, including without limitation the laws of Germany, EU Regulations directly applicable in Germany, and the laws of any other jurisdiction where the Services are performed or the data is processed.

1.4 **"Business Day"** means a day other than Saturday, Sunday, or a public holiday in **[SPECIFY STATE(S) in Germany or other jurisdiction]**.

1.5 **"Change"** means any modification to the scope, nature, volume, or technical specifications of the Services, including changes to the system environment.

1.6 **"Change of Control"** means any transaction or series of transactions resulting in a change in the ownership or control of a Party.

1.7 **"Confidential Information"** has the meaning set out in Section 13.

1.8 **"Customer Data"** means all data, content, and information (i) owned by or licensed to the Customer; (ii) processed by the Service Provider under or in connection with this Agreement; or (iii) generated through Customer's use of the Services.

> **[DRAFTING NOTE — CUSTOMER DATA]:** Distinguish carefully between: (a) **Personal Data** (subject to GDPR/DSGVO); (b) **Non-personal business data** (subject to EU Data Act, trade secrecy law); (c) **Publicly available data**. Under the EU Data Act (Regulation (EU) 2023/2854, applying from 12 September 2025), rights to access and portability of IoT-generated and machine-generated data are regulated. Ensure data ownership and portability obligations in Sections 10 and 26 are consistent with the Data Act.

1.9 **"Data Processing Agreement"** or "**DPA**" means the data processing agreement attached as **Schedule [•]**, forming an integral part of this Agreement.

1.10 **"Documentation"** means all technical and user documentation provided by the Service Provider relating to the Services.

1.11 **"Fees"** means the charges payable by the Customer as set out in **Schedule [•]** (Commercial Terms).

1.12 **"Force Majeure Event"** has the meaning set out in Section 28.

1.13 **"Incident"** means an unplanned interruption to or reduction in the quality of a Service. Incidents are classified by severity as set out in **Schedule [•]** (Service Levels).

1.14 **"Intellectual Property Rights"** or "**IPR**" means all intellectual property rights anywhere in the world, including patents, utility models, copyrights (*Urheberrechte*), database rights, design rights, trade marks, trade secrets, know-how, and all applications for registration of any of the foregoing.

1.15 **"Key Personnel"** means the individuals named in **Schedule [•]** (Key Personnel).

1.16 **"Maintenance Window"** means the planned downtime periods set out in **Schedule [•]** (Service Levels).

1.17 **"Personal Data"** has the meaning assigned in Article 4(1) GDPR.

1.18 **"Processing"** has the meaning assigned in Article 4(2) GDPR.

1.19 **"Security Incident"** means a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, data transmitted, stored, or otherwise processed in connection with the Services.

1.20 **"Service Credits"** means the credits payable by the Service Provider upon failure to meet Service Level targets, as set out in **Schedule [•]**.

1.21 **"Service Levels"** or **"SLA"** means the service level commitments set out in **Schedule [•]** (Service Levels).

1.22 **"Service Schedule"** means each schedule describing a specific service or service category forming part of this Agreement.

1.23 **"Services"** means the IT services described in each applicable Service Schedule and any Statement of Work.

1.24 **"Software"** means the software and applications used by the Service Provider to provide the Services, including third-party software components, as specified in the applicable Service Schedule.

1.25 **"Statement of Work"** or "**SOW**" means a document signed by both Parties specifying particular deliverables, timelines, and pricing for a project or service.

1.26 **"Subcontractor"** means any third party engaged by the Service Provider to perform any part of the Services.

1.27 **"Term"** has the meaning set out in Section 25.

---

### Section 2 — SCOPE OF SERVICES

2.1 **Services.** Subject to the terms of this Agreement, the Service Provider shall provide the Services described in the applicable Service Schedules and any Statements of Work.

2.2 **Service Schedules and SOWs.** Each Service Schedule and SOW is incorporated into and governed by this Agreement. In case of conflict, the order of precedence is: (i) applicable mandatory law; (ii) the main body of this Agreement; (iii) the relevant Service Schedule or SOW; (iv) other Schedules.

> **[DRAFTING NOTE — ORDER OF PRECEDENCE]:** Service Providers typically prefer the main Agreement to prevail over individual SOWs (to prevent ad hoc changes eroding standard protections). Customers sometimes insist that project-specific SOWs control. Negotiate order of precedence carefully — particularly regarding liability caps, which must be consistent across all documents.

2.3 **Changes.** Either Party may request a Change by submitting a written Change request. The Parties shall negotiate the impact on Fees, timelines, and Service Levels in good faith. No Change becomes binding until both Parties have signed a written Change Order.

2.4 **Service Provider's Obligations.** The Service Provider shall:

  (a) perform the Services with the professional care and skill of a competent IT service provider experienced in providing services of the same type (*mit der Sorgfalt eines ordentlichen Kaufmanns*, §§ 347, 269 HGB);

  (b) comply with all Applicable Laws relevant to the provision of the Services;

  (c) maintain sufficient qualified personnel to perform the Services;

  (d) promptly notify the Customer of any circumstances that may materially affect the Services.

2.5 **Customer's Obligations.** The Customer shall:

  (a) provide the Service Provider with timely access to systems, premises, information, and personnel reasonably required to perform the Services;

  (b) comply with all usage guidelines and acceptable use policies provided by the Service Provider;

  (c) promptly notify the Service Provider of any changes to its systems or requirements that may affect the Services;

  (d) designate a named Customer contact responsible for coordination.

2.6 **Customer Dependencies.** The Service Provider's obligations to meet Service Levels and delivery dates are conditional upon the Customer fulfilling its obligations under Section 2.5. Where a Service Level failure is attributable to the Customer's failure to co-operate, the Service Provider shall be relieved of its corresponding obligation to that extent.

> **[DRAFTING NOTE — CUSTOMER DEPENDENCIES]:** This is a critical risk-allocation clause. Service Providers should insist on detailed enumeration of Customer dependencies in each SOW. For managed services or outsourcing, consider a formal governance framework (Section 6) to track and document dependency fulfilment.

---

### Section 3 — FRAMEWORK AGREEMENT AND ORDERING

3.1 **Framework Structure.** This Agreement constitutes a master framework (*Rahmenvertrag*) governing the relationship between the Parties for all IT services. Individual Services are ordered and governed through Service Schedules and SOWs executed hereunder.

3.2 **Ordering Process.** The Customer may request Services by submitting a written order referencing this Agreement. An order is accepted when signed by an authorised representative of the Service Provider.

3.3 **Standard Terms Exclusion.** Any Customer's general terms and conditions (*Allgemeine Geschäftsbedingungen*, **AGB**) are hereby expressly excluded. The Parties' agreement is limited to this Agreement, its Schedules, and individually negotiated SOWs.

> **[DRAFTING NOTE — AGB / BATTLE OF FORMS]:** Under German law (§§ 305 et seq. BGB), conflicting general terms cancel each other out only to the extent they conflict (*Kollisionsregel*). To avoid the "last shot" doctrine, include an explicit exclusion clause. If the Customer insists on referencing its own procurement terms, negotiate which terms control which subject matter, particularly liability, IP, and data protection.

3.4 **Affiliate Orders.**

**[OPTION A — Affiliates may order:]** Customer's Affiliates may place orders under this Agreement. Each Affiliate order constitutes a separate contract between that Affiliate and the Service Provider on the terms of this Agreement. The Customer remains jointly and severally liable (*gesamtschuldnerisch*) for obligations of its Affiliates.

**[OPTION B — No Affiliate orders without amendment:]** Customer's Affiliates may only order Services under this Agreement if the Parties have first executed a written amendment identifying the relevant Affiliate and any adjusted commercial terms.

---

## PART II — SERVICE DELIVERY

---

### Section 4 — SERVICE LEVELS AND AVAILABILITY

4.1 **Service Level Commitments.** The Service Provider shall meet the Service Levels set out in **Schedule [•]** (Service Levels). Service Levels include, as applicable: (i) availability targets; (ii) response and resolution times by Incident severity; (iii) performance metrics; (iv) Maintenance Windows.

4.2 **Measurement.** Service Level performance shall be measured by the Service Provider's monitoring systems, as described in the applicable Schedule. The Customer may deploy independent monitoring tools at its own cost. In case of discrepancy, the Parties shall endeavour to reconcile data; if unresolved within **[10]** Business Days, an independent technical expert appointed by agreement (or, failing agreement, by the **[Deutsche Institut für Normung e.V. (DIN)]** or an agreed dispute resolution body) shall determine the correct measurement.

4.3 **Service Credits.**

**[OPTION A — Service Credits as Sole Remedy for SLA Breach:]**
Service Credits shall be the Customer's sole and exclusive remedy for failure to meet Service Levels, unless the failure constitutes a material breach of this Agreement.

**[OPTION B — Service Credits Without Exclusion of Further Remedies:]**
Service Credits are a genuine pre-estimate of loss and shall be paid without prejudice to any other rights or remedies the Customer may have under this Agreement or Applicable Law.

> **[DRAFTING NOTE — SERVICE CREDITS AS SOLE REMEDY]:** Under German law (§ 307 BGB), a clause excluding further statutory remedies (particularly *Minderung*, *Rücktritt*, and damages under §§ 280, 323 BGB) in standard terms may be void if it unreasonably disadvantages the other party. Option A may be challenged as unfair. Option B is safer from a German law validity perspective. If Option A is used, ensure it only applies to SLA breaches below a materiality threshold.

4.4 **Planned Maintenance.** The Service Provider shall provide the Customer with at least **[5]** Business Days' advance notice of planned maintenance. Emergency maintenance may be performed with shorter notice where strictly necessary for security or stability reasons; the Service Provider shall notify the Customer as soon as practicable.

4.5 **Continuous Improvement.** The Service Provider shall participate in quarterly service reviews and present a service improvement plan if average availability falls below **[95%]** over any rolling **[3-month]** period.

---

### Section 5 — INCIDENT MANAGEMENT

5.1 **Incident Reporting.** The Customer shall report Incidents via **[helpdesk portal / telephone / email]** as specified in **Schedule [•]**.

5.2 **Severity Classification.** Incidents shall be classified as set out in **Schedule [•]**. The initial severity classification is made by the Customer; the Service Provider may re-classify an Incident upon investigation with written notification and reasons.

5.3 **Resolution Process.** The Service Provider shall: (i) acknowledge receipt within the response time set out in Schedule [•]; (ii) provide status updates at the frequency specified per severity level; (iii) resolve or provide a workaround within the resolution time; (iv) issue a root cause analysis for **[Severity 1]** Incidents within **[5]** Business Days of resolution.

5.4 **Major Incident Management.** For Severity 1 Incidents, the Service Provider shall immediately convene a bridge call with the Customer and escalate to senior technical management.

5.5 **Security Incidents.** Security Incidents are governed by Section 15 and the DPA. Notice requirements under GDPR Article 33 (72 hours to supervisory authority) and Article 34 (notification to data subjects) are the responsibility of the Customer as controller, supported by the Service Provider pursuant to the DPA.

---

### Section 6 — GOVERNANCE AND ESCALATION

6.1 **Governance Structure.** The Parties shall establish a governance structure comprising:

  (a) **Operational Level:** Day-to-day service delivery management, meeting **[monthly]** or as needed;
  (b) **Management Level:** Review of performance, issues, and strategic direction, meeting **[quarterly]**;
  (c) **Executive Level:** Escalation and strategic relationship, convening as needed and at least **[annually]**.

6.2 **Service Reviews.** At each Management Level meeting, the Service Provider shall present a service performance report covering the preceding period, including: (i) SLA performance; (ii) Incident statistics; (iii) open Change requests; (iv) security updates; (v) planned activities.

6.3 **Escalation.** Either Party may escalate unresolved issues through the governance levels defined in Section 6.1. Escalation contacts are set out in **Schedule [•]** (Contacts and Escalation).

6.4 **Key Personnel.** The Service Provider shall ensure that Key Personnel are assigned and available throughout the Term. The Service Provider shall not remove or replace Key Personnel without giving the Customer **[20]** Business Days' prior written notice and the Customer's written consent (not to be unreasonably withheld or delayed).

---

### Section 7 — CHANGE MANAGEMENT

7.1 **Change Request.** Either Party may initiate a Change by submitting a written Change request describing the proposed change, rationale, and anticipated impact.

7.2 **Change Impact Assessment.** Within **[10]** Business Days of receipt of a Change request, the Service Provider shall provide a written impact assessment covering: (i) scope changes; (ii) timeline impact; (iii) Fee impact; (iv) risk assessment; (v) Service Level impact.

7.3 **Emergency Changes.** Changes required urgently for security or legal compliance reasons may be implemented by the Service Provider with shorter notice; however, formal documentation shall follow within **[5]** Business Days.

7.4 **Regulatory Changes.** Where a Change is required solely due to a change in Applicable Law, the Parties shall negotiate in good faith the allocation of associated costs. The Service Provider shall not charge for changes required due to its own compliance failures.

> **[DRAFTING NOTE — REGULATORY CHANGE COSTS]:** With the volume of EU digital regulation currently in force or entering into force (NIS2, AI Act, Data Act, DORA, Cyber Resilience Act, eIDAS 2.0), this clause is commercially important. Service Providers want to pass through compliance costs; Customers want to limit this to new obligations not reasonably foreseeable at contract inception. Consider a baseline date and a materiality threshold.

---

## PART III — COMMERCIAL TERMS

---

### Section 8 — FEES AND PAYMENT

8.1 **Fees.** The Customer shall pay the Fees set out in **Schedule [•]** (Commercial Terms). Fees are exclusive of applicable VAT (*Umsatzsteuer/Mehrwertsteuer*).

8.2 **Invoicing.** The Service Provider shall issue invoices **[monthly in arrears / in advance]**. Invoices must comply with §§ 14, 14a UStG (German VAT Act) and, for cross-border transactions, relevant EU VAT rules.

8.3 **Payment Terms.** The Customer shall pay undisputed invoices within **[30]** calendar days of the invoice date. Late payment shall accrue interest at the statutory rate under § 288 BGB (**[currently 9 percentage points above the base rate (*Basiszinssatz*)** for commercial transactions between businesses]).

> **[DRAFTING NOTE — PAYMENT TERMS]:** The EU Late Payment Directive (Directive 2011/7/EU, currently under revision) sets a default of 30 days for B2B transactions and 30 days (extendable to 60) for public authorities. Germany implements this via §§ 271a, 286, 288 BGB. Contractual payment terms exceeding 60 days for commercial transactions may be unenforceable or challengeable under § 271a BGB. For large volume contracts, consider structured payment milestones in the SOW.

8.4 **Disputed Invoices.** The Customer shall notify the Service Provider in writing of any disputed invoice amount within **[10]** Business Days of receipt. The Customer shall pay the undisputed portion of any invoice by the due date. Disputed amounts shall be resolved through Section 30 (Dispute Resolution).

8.5 **Price Adjustment.** Fees may be adjusted annually by the Service Provider upon **[60]** days' written notice, but not by more than the increase in the **[Consumer Price Index for Germany (*Verbraucherpreisindex*, published by Statistisches Bundesamt) / HICP EU]** for the preceding twelve-month period.

**[FALLBACK — Customer-protective version:]** Fees are fixed for the first **[24]** months. Thereafter, the Service Provider may propose a price adjustment by **[90]** days' written notice. If the Parties do not agree on revised Fees within **[30]** days of such notice, the Customer may terminate the affected Services on **[90]** days' notice.

8.6 **Audit Rights (Financial).** No more than once per year, the Customer may audit the Service Provider's records relating to Fees upon **[15]** Business Days' notice. The Customer shall bear audit costs unless the audit reveals an overcharge exceeding **[5%]**, in which case the Service Provider shall bear reasonable audit costs and promptly reimburse the overcharge with interest at the rate in Section 8.3.

---

### Section 9 — INTELLECTUAL PROPERTY

9.1 **Service Provider Background IP.** The Service Provider retains all IPR in its pre-existing software, tools, methodologies, processes, and know-how ("**Background IP**"). Nothing in this Agreement transfers ownership of Background IP to the Customer.

9.2 **Licence to Use Services.** The Service Provider grants the Customer a non-exclusive, non-transferable, revocable (on termination) licence to use the Services and any associated Software and Documentation solely for the Customer's internal business purposes during the Term.

9.3 **Customer Background IP.** The Customer retains all IPR in Customer Data and in materials provided to the Service Provider. The Customer grants the Service Provider a limited licence to use Customer Data solely for the purpose of performing the Services.

9.4 **Deliverables.**

**[OPTION A — Deliverables owned by Service Provider (licence to Customer):]**
All deliverables, works, and materials created specifically for the Customer under this Agreement ("**Deliverables**") are owned by the Service Provider. The Service Provider grants the Customer a perpetual, irrevocable, non-exclusive, royalty-free licence to use the Deliverables for the Customer's internal business purposes.

**[OPTION B — Deliverables owned by Customer:]**
All Deliverables are works commissioned by the Customer. To the extent permitted by applicable copyright law (including § 69b UrhG for software created by employees in the course of employment), the Service Provider hereby assigns all IPR in the Deliverables to the Customer with effect from creation. The Service Provider retains a licence to use its Background IP embedded in Deliverables.

> **[DRAFTING NOTE — IP OWNERSHIP OF DELIVERABLES]:** Under German copyright law (*Urheberrecht*, UrhG), copyright cannot be fully assigned for personal authorship works — only exclusive exploitation rights (*ausschließliche Nutzungsrechte*) can be transferred. For software created by employees, § 69b UrhG grants the employer exploitation rights. For bespoke software commissioned from an external service provider, ensure the contract grants the broadest possible exploitation rights, including source code access and the right to modify. Option B is achievable and protects the Customer; Option A is more typical for service providers and easier to defend operationally.

9.5 **Open Source.** The Service Provider shall maintain a record of all open-source software components used in the Services. The Service Provider shall not use open-source software subject to "copyleft" licences (e.g., GPL v2/v3, AGPL) in a manner that would require the Customer's proprietary code or data to be disclosed or licensed under open-source terms, without the Customer's prior written consent.

9.6 **Third-Party Software.** The Service Provider shall ensure that all third-party software licences required for the Services are in place. The Service Provider shall promptly notify the Customer of any third-party licence changes that may materially affect the Services.

9.7 **IP Indemnity.** The Service Provider shall indemnify, defend, and hold harmless the Customer from any third-party claim that the Services infringe a third party's IPR in Germany or any other EU Member State where the Customer uses the Services, provided that: (i) the Customer promptly notifies the Service Provider of the claim; (ii) the Service Provider has sole control of the defence; (iii) the infringement is not caused by the Customer's modification or misuse. This indemnity does not apply to open-source components where the Customer has been notified of relevant licence terms.

> **[DRAFTING NOTE — IP INDEMNITY SCOPE]:** The IP indemnity is typically one of the most heavily negotiated provisions. Service Providers try to limit it to Germany; Customers want EU-wide or global coverage. Cap the indemnity at an agreed multiple of Fees or align with the general liability cap. Consider carve-outs for: (i) Customer-directed modifications; (ii) use in combination with other products; (iii) use after Service Provider has offered a non-infringing alternative.

---

## PART IV — DATA AND SECURITY

---

### Section 10 — DATA GOVERNANCE AND DATA ACT COMPLIANCE

10.1 **Data Processing Agreement.** The Parties have entered into the DPA attached as **Schedule [•]**, which governs the Processing of Personal Data. In case of conflict between the DPA and this Agreement on matters of data protection, the DPA prevails.

10.2 **Customer Data Ownership.** As between the Parties, the Customer is and remains the owner of all Customer Data. The Service Provider acquires no rights in Customer Data other than as expressly set out in this Agreement.

10.3 **Data Use Restriction.** The Service Provider shall process Customer Data only: (i) to perform the Services; (ii) as directed by the Customer; (iii) as required by Applicable Law (in which case Section 10.7 applies). The Service Provider shall not use Customer Data for any other purpose, including improving its own products or services, without the Customer's explicit prior written consent.

10.4 **EU Data Act Compliance.** Where the Services involve connected products or related services generating data within the scope of Regulation (EU) 2023/2854 (EU Data Act, applicable from 12 September 2025):

  (a) The Service Provider shall make available to the Customer access to non-personal data generated by the Customer's use of the Services, in a structured, commonly used, and machine-readable format;

  (b) The Service Provider shall support data portability requests within **[30]** calendar days;

  (c) The Service Provider shall not use data generated through Customer's use of the Services to derive insights that give the Service Provider a competitive advantage over the Customer without explicit consent;

  (d) The Parties shall implement interoperability standards as required under the Data Act.

> **[DRAFTING NOTE — EU DATA ACT]:** The EU Data Act (Regulation (EU) 2023/2854) creates mandatory data access and portability rights in IoT/connected-device contexts and also regulates cloud switching rights (Articles 23-31). Cloud and managed service providers must comply with cloud switching obligations from 12 September 2025. The Data Act prohibits contractual terms in B2B contracts that are "manifestly disproportionate" regarding data access, data portability, and liability for data loss (Article 13). Review all data-related clauses for Data Act compliance.

10.5 **Data Localisation.**

**[OPTION A — EU-only data processing:]**
The Service Provider shall process all Customer Data exclusively within the European Economic Area (**EEA**). Any transfer of Customer Data outside the EEA requires the Customer's prior written consent and appropriate safeguards under Chapter V GDPR.

**[OPTION B — Specific country restrictions:]**
The Service Provider shall process Customer Data exclusively in **[Germany / specified EU Member States]** unless the Customer provides prior written consent for processing in other locations, which shall not be unreasonably withheld.

**[OPTION C — No geographic restriction:]**
The Service Provider may process Customer Data in any jurisdiction subject to compliance with GDPR Chapter V and the DPA.

> **[DRAFTING NOTE — DATA LOCALISATION]:** Many German enterprise customers (particularly in finance, healthcare, and public sector) require Germany-only or EU-only processing. This has cost implications for the Service Provider. For regulated industries (e.g., financial services under DORA), outsourcing to third-country providers requires prior regulatory notification (see Section 22). Cloud providers offering sovereign cloud zones in Germany (e.g., AWS European Sovereign Cloud, Azure Germany North) can meet Option B requirements.

10.6 **Data Return and Deletion.** Upon termination or expiry of this Agreement (or an individual Service):

  (a) The Service Provider shall provide the Customer with a complete export of all Customer Data in a portable, industry-standard format within **[30]** calendar days of termination;

  (b) Following successful export, the Service Provider shall securely delete or destroy all copies of Customer Data within **[60]** calendar days;

  (c) The Service Provider shall provide written certification of deletion upon request.

10.7 **Legal Disclosure Requests.** If the Service Provider receives a court order, regulator demand, or other legal process requiring disclosure of Customer Data, the Service Provider shall: (i) promptly notify the Customer to the extent legally permitted; (ii) co-operate with the Customer to seek a protective order or other appropriate relief; (iii) disclose only the minimum data required.

---

### Section 11 — INFORMATION SECURITY

11.1 **Security Standards.** The Service Provider shall implement and maintain an information security management system meeting the standards set out in **Schedule [•]** (Security Requirements), which shall be at least equivalent to:

  (a) **ISO/IEC 27001:2022** certification (or equivalent recognized standard); and
  (b) The minimum security measures required under **Article 21 NIS2 Directive** (implemented in Germany through the IT-Sicherheitsgesetz 2.0 / BSIG 2023).

> **[DRAFTING NOTE — NIS2 / BSIG]:** The NIS2 Directive (Directive (EU) 2022/2555) was transposed into German law through the BSIG reform (Gesetz zur Umsetzung der NIS-2-Richtlinie, in force from 18 October 2024). If the Customer is an "essential" or "important" entity under NIS2/BSIG (energy, transport, health, digital infrastructure, etc.), they have obligations to ensure their IT service providers meet security requirements. The Service Provider must demonstrate NIS2-equivalent controls. For critical infrastructure (*KRITIS*), additional BSI requirements apply.

11.2 **Security Measures.** As a minimum, the Service Provider shall implement:

  (a) Risk-based information security policies and procedures;
  (b) Access control, least-privilege principles, and multi-factor authentication for access to Customer Data;
  (c) Encryption of Customer Data at rest (AES-256 or equivalent) and in transit (TLS 1.2 or higher);
  (d) Regular vulnerability scanning and penetration testing (at least annually, with results shared with Customer upon request);
  (e) Security incident detection and response capabilities;
  (f) Supply chain security controls (Section 12);
  (g) Business continuity and disaster recovery (Section 16);
  (h) Employee security training and awareness.

11.3 **Security Certifications.** The Service Provider shall maintain the security certifications set out in **Schedule [•]** and shall provide the Customer with current certification documents upon request. The Service Provider shall notify the Customer within **[10]** Business Days if any required certification lapses or is suspended.

11.4 **Penetration Testing.** The Customer may, upon **[20]** Business Days' prior written notice and at its own cost, conduct penetration testing or security audits of the Service Provider's systems used to provide the Services, subject to agreed scope and conditions that do not disrupt other customers' services.

**[FALLBACK — Service Provider-protective version:]** The Customer may not conduct penetration testing independently but may request the Service Provider to commission penetration testing by a mutually agreed qualified third party at the Customer's cost, with results shared with the Customer.

11.5 **BSI Notifications.** Where the Service Provider is itself a KRITIS operator or an important/essential entity under BSIG, it shall fulfil its notification obligations to the BSI (*Bundesamt für Sicherheit in der Informationstechnik*) independently and shall inform the Customer of any BSI investigations or instructions that materially affect the Services.

---

### Section 12 — SUPPLY CHAIN SECURITY AND SUBCONTRACTORS

12.1 **Approved Subcontractors.** The Service Provider shall not engage Subcontractors to perform material parts of the Services without the Customer's prior written consent. An initial list of approved Subcontractors is set out in **Schedule [•]**. The Service Provider shall notify the Customer **[30]** days in advance of any proposed addition or replacement, and the Customer may object on reasonable grounds.

12.2 **Subcontractor Obligations.** The Service Provider shall impose on each Subcontractor obligations at least equivalent to those applicable to the Service Provider under this Agreement with respect to: (i) security; (ii) data protection; (iii) confidentiality; (iv) compliance.

12.3 **Service Provider Liability.** The Service Provider remains fully liable to the Customer for the acts and omissions of its Subcontractors as if they were acts and omissions of the Service Provider itself.

12.4 **Supply Chain Security Programme.** In accordance with NIS2 Article 21(2)(d) and the EU Cyber Resilience Act (CRA, Regulation (EU) 2024/2847), the Service Provider shall maintain a documented supply chain security programme covering:

  (a) Security risk assessment of critical Subcontractors;
  (b) Minimum security requirements for Subcontractors;
  (c) Contractual security obligations for Subcontractors;
  (d) Monitoring of Subcontractor compliance.

> **[DRAFTING NOTE — CYBER RESILIENCE ACT]:** The EU Cyber Resilience Act (Regulation (EU) 2024/2847) introduces mandatory cybersecurity requirements for products with digital elements. It entered into force on 10 December 2024, with most obligations applying from 11 December 2027. For software products provided as part of the Services, check whether the CRA applies and allocate responsibilities between manufacturer and service provider roles accordingly.

---

### Section 13 — CONFIDENTIALITY

13.1 **Definition.** "Confidential Information" means all non-public information disclosed by one Party ("**Disclosing Party**") to the other ("**Receiving Party**") in connection with this Agreement, in any form, that is: (i) marked as confidential; (ii) identified orally as confidential at the time of disclosure; or (iii) of a nature that a reasonable person would recognise as confidential.

13.2 **Obligations.** The Receiving Party shall: (i) keep Confidential Information strictly confidential; (ii) use it only for the purposes of this Agreement; (iii) disclose it only to its employees, agents, and advisors on a need-to-know basis who are bound by equivalent confidentiality obligations.

13.3 **Exceptions.** Confidentiality obligations do not apply to information that: (i) is or becomes publicly known through no breach by the Receiving Party; (ii) was known to the Receiving Party before disclosure; (iii) is received from a third party without restriction; (iv) is independently developed without reference to the Confidential Information; (v) must be disclosed under Applicable Law or court order (with prior notice to the Disclosing Party where legally permitted).

13.4 **Trade Secrets.** The Parties acknowledge that certain Confidential Information may constitute trade secrets within the meaning of Directive (EU) 2016/943 as implemented in Germany through the Geschäftsgeheimnisgesetz (**GeschGehG**). The Parties shall implement appropriate protective measures as required by § 2 No. 1(b) GeschGehG to maintain trade secret status.

13.5 **Survival.** Confidentiality obligations survive termination of this Agreement for a period of **[5]** years, except for trade secrets, which remain protected indefinitely under the GeschGehG.

13.6 **Injunctive Relief.** The Parties acknowledge that breach of this Section may cause irreparable harm for which monetary damages are insufficient. Each Party reserves the right to seek preliminary injunctive relief (*einstweilige Verfügung*) before any competent court.

---

## PART V — LIABILITY, WARRANTIES, AND INDEMNITIES

---

### Section 14 — WARRANTIES

14.1 **Service Provider Warranties.** The Service Provider warrants that:

  (a) It has full power and authority to enter into and perform this Agreement;
  (b) The Services will be performed with professional skill and care in accordance with industry standards (*Stand der Technik*) and Applicable Law;
  (c) The Services will materially conform to the specifications in the applicable Service Schedule during the Term;
  (d) It holds all licences, permits, and authorisations required to perform the Services;
  (e) The Software and Services do not, to its knowledge, contain malicious code.

14.2 **Customer Warranties.** The Customer warrants that:

  (a) It has full power and authority to enter into and perform this Agreement;
  (b) It has all necessary rights to provide Customer Data to the Service Provider;
  (c) Use of Customer Data in accordance with this Agreement will not infringe any third-party rights.

14.3 **Disclaimer.**

**[OPTION A — Service Provider's preferred position:]**
EXCEPT AS EXPRESSLY SET OUT IN THIS AGREEMENT, THE SERVICE PROVIDER MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.

**[OPTION B — German law-compliant (narrower disclaimer):]**
Implied warranties are excluded to the maximum extent permitted by German law. The Parties acknowledge that under German law, certain implied terms (particularly *Gewährleistungsrechte* under §§ 634 et seq. BGB for services with work character) cannot be fully excluded in standard terms and apply as statutory fallbacks.

> **[DRAFTING NOTE — WARRANTIES AND GERMAN LAW]:** German law distinguishes between: (a) **Dienstvertrag** (§§ 611 et seq. BGB) — service contract where no specific result is owed; (b) **Werkvertrag** (§§ 631 et seq. BGB) — work contract where a specific result (*Werk*) is owed. For managed services and ongoing IT operations, German courts often classify the contract as *Dienstvertrag*. For bespoke software development, it is typically *Werkvertrag* with statutory defect remedies (Nacherfüllung, Minderung, Rücktritt). The contractual characterisation affects statutory warranty rights and cannot be completely contractually altered in standard terms.

---

### Section 15 — SECURITY INCIDENT RESPONSE

15.1 **Incident Notification.** The Service Provider shall notify the Customer of any confirmed or reasonably suspected Security Incident without undue delay and in any event within **[24 hours]** of becoming aware.

15.2 **Notification Content.** The Security Incident notification shall include, to the extent available: (i) nature and scope of the incident; (ii) categories and approximate number of affected data subjects (if applicable); (iii) categories and approximate volume of affected records; (iv) contact details for further information; (v) description of likely consequences; (vi) remediation measures taken or proposed.

15.3 **Cooperation.** The Service Provider shall cooperate fully with the Customer and, where applicable, the Customer's data protection officer in investigating and remediating the Security Incident, and in satisfying notification obligations under GDPR Articles 33–34 and any other applicable notification obligations.

15.4 **Costs.** The costs of incident response, remediation, and notification shall be borne by the Party whose negligence or wilful misconduct caused or materially contributed to the Security Incident. Where responsibility is unclear, costs shall be shared equally pending determination of liability.

> **[DRAFTING NOTE — GDPR NOTIFICATION OBLIGATIONS]:** GDPR Article 33 requires data controllers to notify the supervisory authority within 72 hours of becoming aware of a Personal Data breach. The 24-hour contractual notification to the Customer is intentionally shorter than the 72-hour statutory deadline to give the Customer time to investigate and prepare the supervisory authority notification. The Customer (as controller) bears the notification obligation; the Service Provider (as processor) must support this under Article 28(3)(f).

---

### Section 16 — BUSINESS CONTINUITY AND DISASTER RECOVERY

16.1 **BC/DR Plan.** The Service Provider shall maintain a documented Business Continuity Plan (**BCP**) and Disaster Recovery Plan (**DRP**) for the Services, with recovery objectives meeting at least:

  - **Recovery Time Objective (RTO):** **[SPECIFY, e.g., 4 hours for critical systems]**
  - **Recovery Point Objective (RPO):** **[SPECIFY, e.g., 1 hour]**

16.2 **Testing.** The Service Provider shall test its BCP and DRP at least **[annually]** and shall provide the Customer with a summary of test results within **[20]** Business Days of each test.

16.3 **Customer-Specific DR.** If specific DR requirements are agreed for the Customer's environment, they shall be set out in the relevant Service Schedule.

---

### Section 17 — LIABILITY

17.1 **Unlimited Liability.** Nothing in this Agreement limits or excludes either Party's liability for: (i) death or personal injury caused by negligence (*grobe Fahrlässigkeit oder Vorsatz*, §§ 823, 276 BGB); (ii) fraud or fraudulent misrepresentation (*Arglist*); (iii) liability that cannot be excluded or limited under Applicable Law, including §§ 305 et seq. BGB (AGB-Recht), the Product Liability Act (*Produkthaftungsgesetz*), or the Data Protection Act (*BDSG*).

> **[DRAFTING NOTE — MANDATORY LIABILITY UNDER GERMAN LAW]:** Under § 309 No. 7 BGB, clauses excluding liability for: (a) death or personal injury caused by intentional or negligent breach; (b) damage caused by intentional breach or gross negligence are **void** in standard terms. Further, under § 309 No. 8 BGB, clauses limiting liability in a manner that would be unreasonable are void. Ensure the liability structure in this Section complies with these mandatory rules. Only in individually negotiated contracts (*Individualvereinbarungen*, § 305 BGB) can parties agree more liberal liability limitations.

17.2 **Liability Cap.**

**[OPTION A — Annual cap:]**
Subject to Section 17.1, each Party's total aggregate liability to the other under or in connection with this Agreement (whether in contract, tort, or otherwise) shall not exceed an amount equal to the total Fees paid or payable under this Agreement in the **[12 months]** preceding the event giving rise to the claim.

**[OPTION B — Per-incident cap with annual aggregate:]**
Subject to Section 17.1, (i) each Party's liability for any single claim or series of related claims shall not exceed **[SPECIFY, e.g., EUR 500,000]**; and (ii) each Party's total aggregate liability in any calendar year shall not exceed **[SPECIFY, e.g., EUR 2,000,000 or 12 months' Fees, whichever is higher]**.

**[OPTION C — Customer-protective version (no cap on data and security breaches):]**
Subject to Section 17.1, the liability cap in Section 17.2 shall not apply to: (i) breaches of Section 10 (Data Governance) or Section 11 (Information Security); (ii) breaches of the DPA; (iii) the IP indemnity in Section 9.7; (iv) breaches of confidentiality obligations under Section 13.

> **[DRAFTING NOTE — LIABILITY CAP LEVELS]:** The appropriate cap depends on: contract value, nature of services, criticality to the Customer's business, insurance coverage, and negotiating leverage. As a rule of thumb in German practice: **1× annual Fees** is typical for standard IT services; **2–3× annual Fees** for critical managed services. Data breach and security breach liability is increasingly uncapped in enterprise contracts given GDPR fines (up to 4% global turnover under Article 83 GDPR). Insurance requirements in Section 19 must be calibrated to the liability cap.

17.3 **Consequential Loss Exclusion.**

**[OPTION A — Standard exclusion:]**
Subject to Section 17.1, neither Party shall be liable to the other for any: (i) loss of profits; (ii) loss of revenue; (iii) loss of business; (iv) loss of anticipated savings; (v) loss of data (beyond the cost of reasonable restoration efforts); (vi) indirect or consequential loss; whether or not such loss was foreseeable or the Party had been advised of its possibility.

**[FALLBACK — Customer-protective carve-out:]**
Notwithstanding Section 17.3(i), the exclusion of consequential loss shall not apply where loss of data or Security Incidents are caused by the Service Provider's gross negligence (*grobe Fahrlässigkeit*) or wilful misconduct (*Vorsatz*).

> **[DRAFTING NOTE — CONSEQUENTIAL LOSS UNDER GERMAN LAW]:** German law does not use the common law "consequential loss" concept. German law distinguishes between *unmittelbarer Schaden* (direct damage) and *mittelbarer Schaden* (indirect damage, including lost profits). Exclusions of liability for *mittelbarer Schaden* or *entgangener Gewinn* in standard terms are generally permissible if not disproportionate, but must not exclude liability for intentional or grossly negligent conduct (§ 309 No. 7 BGB). Tailor the exclusion carefully to the specific services and risk profile.

17.4 **Duty to Mitigate.** Each Party shall take reasonable steps to mitigate its losses upon becoming aware of any event that may give rise to a claim under this Agreement.

17.5 **Notice of Claims.** Any claim under this Agreement must be notified to the other Party in writing within **[12]** months of the date the claiming Party became aware, or should reasonably have become aware, of the circumstances giving rise to the claim. Claims not notified within this period are time-barred, without prejudice to applicable statutory limitation periods under §§ 195 et seq. BGB.

> **[DRAFTING NOTE — LIMITATION PERIODS]:** The standard German limitation period (*Verjährungsfrist*) is 3 years from year-end knowledge (§§ 195, 199 BGB), with a maximum of 10 years regardless of knowledge (§ 199(4) BGB). Shortening the limitation period in standard terms is permissible for B2B contracts but must not be unreasonably short. 12 months is generally acceptable for commercial IT service contracts under German case law. Do not shorten limitation periods for intentional misconduct claims.

---

### Section 18 — INDEMNIFICATION

18.1 **General Indemnity.** Each Party ("**Indemnifying Party**") shall indemnify and hold harmless the other ("**Indemnified Party**") from and against third-party claims, losses, damages, costs, and expenses (including reasonable legal fees) arising from the Indemnifying Party's: (i) breach of this Agreement; (ii) negligence or wilful misconduct; (iii) infringement of third-party IPR (Section 9.7).

18.2 **Data Protection Indemnity.** The Service Provider shall indemnify the Customer against third-party claims and regulatory fines attributable to the Service Provider's breach of the DPA or its data protection obligations under this Agreement.

> **[DRAFTING NOTE — REGULATORY FINE INDEMNITY]:** GDPR fines are imposed on the controller (the Customer) and cannot be directly indemnified in a way that eliminates the deterrent effect. However, where a fine is wholly attributable to the Service Provider's actions as a processor (e.g., a security breach caused by the Service Provider's negligence), indemnity clauses covering reasonable portions of fines and costs are commercially appropriate. Some German courts have questioned whether contractual indemnities for regulatory fines are enforceable (*ordre public* concerns) — seek specific legal advice for high-value contracts.

18.3 **Indemnification Procedure.** The Indemnified Party shall: (i) promptly notify the Indemnifying Party; (ii) grant the Indemnifying Party sole control of the defence (with the right to participate at its own cost); (iii) provide reasonable cooperation.

---

### Section 19 — INSURANCE

19.1 **Required Coverage.** The Service Provider shall maintain throughout the Term, and for **[2]** years thereafter, the following minimum insurance coverages:

  (a) **Professional Indemnity / Errors and Omissions:** EUR **[SPECIFY, e.g., 5,000,000]** per claim and in the aggregate;
  (b) **Cyber Liability / Data Breach:** EUR **[SPECIFY, e.g., 5,000,000]** per claim and in the aggregate;
  (c) **Commercial General Liability** (*Betriebshaftpflicht*): EUR **[SPECIFY, e.g., 5,000,000]** per occurrence;
  (d) Any additional coverages required under Applicable Law.

19.2 **Evidence.** Upon request, the Service Provider shall provide the Customer with certificates of insurance evidencing the required coverages. The Service Provider shall notify the Customer within **[5]** Business Days if any required coverage is cancelled, materially reduced, or lapses.

---

## PART VI — REGULATORY COMPLIANCE

---

### Section 20 — GENERAL REGULATORY COMPLIANCE

20.1 **Compliance Obligation.** Each Party shall comply with all Applicable Laws relevant to its role under this Agreement, including:

  - **GDPR** (Regulation (EU) 2016/679) and **BDSG** (Bundesdatenschutzgesetz);
  - **NIS2 Directive** (Directive (EU) 2022/2555) and implementing German law;
  - **EU AI Act** (Regulation (EU) 2024/1689) where applicable;
  - **EU Data Act** (Regulation (EU) 2023/2854);
  - **EU Cyber Resilience Act** (Regulation (EU) 2024/2847) where applicable;
  - **DORA** (Regulation (EU) 2022/2554) where the Customer is a regulated financial entity;
  - **EU Digital Services Act** (Regulation (EU) 2022/2065) where applicable;
  - **eIDAS 2.0** (Regulation (EU) 2024/1183) where electronic identification or trust services are involved;
  - German sector-specific laws (e.g., **Telekommunikationsgesetz (TKG)**, **Medizinprodukterecht-Durchführungsgesetz**, financial supervisory laws).

20.2 **Regulatory Change Notification.** Each Party shall promptly notify the other of any regulatory development that materially affects the Services or either Party's ability to perform its obligations.

20.3 **Compliance Certification.** Upon reasonable request, each Party shall provide the other with reasonable evidence of its compliance with the provisions of this Section.

---

### Section 21 — AI ACT COMPLIANCE

21.1 **Applicability.** This Section applies where the Services include AI Components as defined in Section 1.2.

21.2 **Risk Classification.** The Parties shall cooperate to classify all AI Components by risk level in accordance with the EU AI Act. The classification is set out in **Schedule [•]** (AI Components Register) and shall be updated upon any material change.

21.3 **Service Provider Obligations (AI Act).**

  (a) **Prohibited AI Systems:** The Service Provider shall not use or provide AI systems classified as prohibited under Article 5 EU AI Act in any part of the Services.

  (b) **High-Risk AI Systems:** Where AI Components are classified as high-risk under Annex III EU AI Act, the Service Provider shall comply with Chapter III, Section 2 EU AI Act obligations, including: (i) risk management systems; (ii) technical documentation; (iii) human oversight measures; (iv) accuracy, robustness, and cybersecurity requirements; (v) registration in the EU database (where applicable).

  (c) **Transparency:** Where AI Components interact with the Customer's end users, the Service Provider shall ensure appropriate transparency disclosures as required by Article 50 EU AI Act.

  (d) **General Purpose AI (GPAI):** Where the Services incorporate GPAI models (Article 51 EU AI Act), the Service Provider shall comply with applicable GPAI provider obligations and provide the Customer with technical documentation and usage policies.

21.4 **Customer Obligations (AI Act — Deployer Role).** To the extent the Customer uses AI Components in a "deployer" capacity under the EU AI Act, the Customer shall comply with its deployer obligations under Article 26 EU AI Act, including implementing human oversight and informing affected employees in accordance with applicable labour law.

> **[DRAFTING NOTE — EU AI ACT TIMELINE]:** Most AI Act provisions apply from 2 August 2026, except: (a) prohibited AI systems: from 2 February 2025; (b) GPAI obligations: from 2 August 2025; (c) high-risk AI systems (Annex I — sectoral legislation): from 2 August 2027. Build a compliance roadmap into the SOW for AI-heavy services. Note that German employment law (*Betriebsverfassungsgesetz*, § 87 BetrVG) gives works councils co-determination rights regarding the introduction of AI systems for employee monitoring.

21.5 **AI Act Cooperation.** The Service Provider shall provide the Customer with all information reasonably required for the Customer to fulfil its obligations as a deployer under the EU AI Act, including relevant instructions for use, technical documentation, and cooperation with market surveillance authorities.

---

### Section 22 — FINANCIAL SECTOR AND DORA COMPLIANCE

22.1 **Applicability.** This Section applies where the Customer is a financial entity regulated under Regulation (EU) 2022/2554 (Digital Operational Resilience Act, **DORA**), which applies from 17 January 2025.

22.2 **DORA-Mandated Provisions.** To the extent required by DORA and the applicable regulatory technical standards (**RTS**), this Agreement includes the following:

  (a) **Full service description:** The Services, as described in the Service Schedules, constitute a complete and accurate description of the services provided.

  (b) **Locations of data processing:** Data processing locations are specified in **Schedule [•]** (Data Processing Locations).

  (c) **Data security provisions:** As set out in Section 11 and Schedule [•] (Security Requirements).

  (d) **Access, inspection, and audit rights:** As set out in Section 23.

  (e) **Availability, authenticity, integrity, and confidentiality of data:** As set out in Sections 10, 11, and 15.

  (f) **ICT incident reporting:** As set out in Section 5.5 and the DPA.

  (g) **Participation in TLPT (Threat-Led Penetration Testing):** The Service Provider shall cooperate with the Customer's TLPT programme as required by DORA Article 26 and applicable TIBER-EU/DORA-TLPT frameworks.

  (h) **Sub-outsourcing:** As set out in Section 12.

  (i) **Exit management and termination:** As set out in Sections 25 and 26.

  (f) **Termination rights for regulatory non-compliance:** As set out in Section 25.4.

22.3 **Regulatory Notification.** The Service Provider acknowledges that the Customer may be required to notify its competent authority (e.g., BaFin, ECB/SSM) of this Agreement as a material ICT outsourcing arrangement. The Service Provider shall provide all information reasonably required for such notifications.

22.4 **Concentration Risk.** The Service Provider shall promptly notify the Customer if providing services to the Customer would cause the Customer's concentration risk thresholds under DORA Article 29 to be exceeded.

> **[DRAFTING NOTE — DORA]:** DORA (Regulation (EU) 2022/2554) applies from 17 January 2025 to banks, insurers, investment firms, payment institutions, and other financial entities in the EU. It mandates specific contractual provisions for ICT third-party service providers. The EBA/EIOPA/ESMA Joint RTS on subcontracting of ICT services (Commission Delegated Regulation (EU) 2024/1505) and the RTS on ICT third-party risk management tools (Commission Delegated Regulation (EU) 2024/1502) set out detailed contractual content requirements. This Section provides a framework; a DORA-specific annex is recommended for financial sector contracts.

---

### Section 23 — AUDIT RIGHTS

23.1 **Audit Entitlement.** The Customer (and, where required by Applicable Law, competent regulatory authorities) shall have the right to audit the Service Provider's compliance with this Agreement, including its security controls, data protection measures, and service delivery.

23.2 **Customer-Led Audits.** Subject to Section 23.4, the Customer may conduct audits no more than **[once per year]**, upon **[20]** Business Days' prior written notice, specifying the scope and proposed timing. The Customer shall bear its own audit costs. Additional audits may be conducted: (i) where there is a reasonable suspicion of material breach; (ii) following a Security Incident; (iii) as required by regulatory authority.

23.3 **Audit by Third Parties.** The Customer may conduct audits through qualified independent auditors, provided such auditors execute a non-disclosure agreement with the Service Provider on reasonable terms.

23.4 **Audit Conduct.** Audits shall be conducted during Business Hours, with minimum disruption to the Service Provider's operations. The Service Provider may exclude from the audit scope: (i) information subject to legal privilege; (ii) information relating to other customers; (iii) commercially sensitive information not relevant to this Agreement.

23.5 **Regulatory Audit.** The Service Provider shall grant access to competent regulatory authorities (including BaFin, BSI, data protection authorities) without undue delay and shall cooperate fully with such authorities as required by law. The Service Provider shall promptly notify the Customer of any regulatory inspection relating to the Services.

23.6 **Certification-Based Assurance.** The Service Provider may satisfy audit requirements by providing up-to-date third-party audit reports (e.g., SOC 2 Type II, ISO 27001 certification audits) provided such reports address the subject matter of the requested audit.

---

## PART VII — TERM, TERMINATION, AND EXIT

---

### Section 24 — TERM

24.1 **Initial Term.** This Agreement shall commence on the Effective Date and, unless terminated earlier in accordance with its terms, shall continue for an initial term of **[SPECIFY, e.g., 3 years]** ("**Initial Term**").

24.2 **Renewal.** Following the Initial Term, this Agreement shall automatically renew for successive **[1-year]** periods unless either Party gives **[90]** days' written notice of non-renewal before the end of the then-current term.

**[FALLBACK — No automatic renewal:]** This Agreement shall not automatically renew. At least **[60]** days before the end of the Initial Term or any renewal term, the Parties shall discuss continuation of the Services.

> **[DRAFTING NOTE — AUTO-RENEWAL]:** Under German AGB law (§ 309 No. 9 BGB), automatic renewal clauses in standard terms are void if they extend the contract for more than **1 year** at a time for an indefinite period or if the non-renewal notice period exceeds **3 months**. Ensure compliance. For individually negotiated contracts (*Individualvereinbarung*), parties may agree longer periods.

---

### Section 25 — TERMINATION

25.1 **Termination for Convenience.** Either Party may terminate this Agreement (or individual Service Schedules) for convenience upon **[90]** days' prior written notice.

**[FALLBACK — Service Provider's preferred position — no termination for convenience:]** Neither Party may terminate this Agreement for convenience during the Initial Term. After the Initial Term, either Party may terminate on **[90]** days' written notice.

> **[DRAFTING NOTE — TERMINATION FOR CONVENIENCE]:** Service Providers typically resist termination for convenience during the initial term (to protect their investment). Customers often insist on it (e.g., for outsourcing transitions, M&A activity). A compromise is to allow Customer termination for convenience with a break fee equal to a fixed number of months' Fees.

25.2 **Termination for Material Breach.** Either Party may terminate this Agreement immediately by written notice if the other Party: (i) commits a material breach that, if capable of remedy, is not remedied within **[30]** days of written notice; (ii) commits repeated material breaches (even if individually remedied) that together constitute a pattern of non-performance.

25.3 **Termination for Insolvency.** Either Party may terminate this Agreement immediately upon written notice if the other Party: (i) is insolvent (*zahlungsunfähig*, § 17 InsO) or over-indebted (*überschuldet*, § 19 InsO); (ii) files for or has filed against it a petition for insolvency proceedings (*Insolvenzantrag*); (iii) makes a general assignment for the benefit of its creditors.

> **[DRAFTING NOTE — INSOLVENCY IN GERMAN LAW]:** Under German insolvency law (*Insolvenzordnung*, InsO), the insolvency administrator (*Insolvenzverwalter*) may elect to continue or terminate executory contracts (§ 103 InsO). Clauses providing for automatic termination upon insolvency may be challenged. However, where the contract is of a highly personal or trust-based nature (*höchstpersönlich*), courts may uphold termination. Include a clause allowing the Customer to source services from a third party pending insolvency proceedings.

25.4 **Termination for Regulatory Non-Compliance.**

  (a) The Customer may terminate this Agreement on **[30]** days' written notice if: (i) the Service Provider loses a regulatory certification required for provision of the Services; (ii) a competent authority orders the Customer to terminate the arrangement; (iii) the Service Provider suffers a data protection enforcement action that materially affects its ability to perform the Services.

  (b) For DORA-regulated financial entities, the Customer may terminate immediately if continued performance would place the Customer in breach of applicable prudential or operational resilience requirements.

25.5 **Change of Control.** Either Party may terminate this Agreement on **[60]** days' written notice if the other Party undergoes a Change of Control that, in the terminating Party's reasonable opinion, results in a material conflict of interest or a material adverse change in the other Party's ability to perform its obligations.

25.6 **Effects of Termination.** Upon termination or expiry:

  (a) The Service Provider shall continue to provide the Services during the exit period under Section 26;
  (b) All licences granted under this Agreement shall cease (subject to Section 26);
  (c) Each Party shall return or destroy the other's Confidential Information;
  (d) Accrued payment obligations remain due;
  (e) Sections 9, 13, 15, 17, 18, and 30 survive termination.

---

### Section 26 — EXIT MANAGEMENT AND TRANSITION

26.1 **Exit Obligation.** The Service Provider shall cooperate in good faith to support a smooth transition of the Services to the Customer or a successor service provider ("**Exit**").

26.2 **Exit Period.** The Service Provider shall continue to provide the Services for a period of up to **[12]** months following notice of termination or expiry ("**Exit Period**"), provided the Customer continues to pay the applicable Fees during the Exit Period.

26.3 **Exit Plan.** The Service Provider shall maintain and make available to the Customer an up-to-date Exit Plan (**Schedule [•]**) describing: (i) data export procedures; (ii) knowledge transfer; (iii) staff assistance available; (iv) system documentation; (v) assistance in migrating to a successor.

26.4 **Data Portability.** During and following the Exit Period, the Service Provider shall export Customer Data in a portable, open, and widely used format and shall not impose technical or contractual barriers to migration.

> **[DRAFTING NOTE — CLOUD SWITCHING / DATA ACT PORTABILITY]:** EU Data Act Articles 23–31 impose mandatory cloud switching obligations on cloud service providers, including free data export, interoperability obligations, and prohibition of excessive switching fees (from 12 September 2025). DORA Article 28(8) requires financial entities to include exit provisions in ICT third-party contracts. Ensure the Exit Plan and data portability provisions are consistent with these mandatory requirements.

26.5 **Switching Fees.** Any charges for data export and migration assistance during the Exit Period shall not exceed the Service Provider's reasonable cost. Data export fees for compliance with the EU Data Act shall be zero.

26.6 **Business Continuity During Exit.** The Service Provider shall maintain Service Levels during the Exit Period and shall not materially reduce the quality of Services or staffing during that period.

---

## PART VIII — GENERAL PROVISIONS

---

### Section 27 — NOTICES

27.1 All notices under this Agreement must be in writing and delivered to the addresses and contacts set out in **Schedule [•]** (Notices). Notices may be given by: (i) personal delivery; (ii) registered post (*Einschreiben*); (iii) courier; (iv) email (with read receipt or written acknowledgement), except for notices of termination, which must be by registered post or courier.

27.2 Notice periods run from the date of receipt. For registered post, receipt is presumed on the third Business Day after posting.

---

### Section 28 — FORCE MAJEURE

28.1 **Definition.** A "Force Majeure Event" means any event beyond the reasonable control of the affected Party, including natural disaster, war, terrorism, pandemic declared by WHO, governmental actions that are beyond the Party's reasonable control, or nationwide telecommunications or power infrastructure failure.

28.2 **Effect.** The affected Party is excused from performance to the extent directly prevented by a Force Majeure Event, provided it: (i) promptly notifies the other Party; (ii) takes all reasonable steps to mitigate the impact; (iii) keeps the other Party regularly informed.

28.3 **Exclusions.** The following are not Force Majeure Events: (i) labour disputes within the Service Provider's own workforce; (ii) financial inability to perform; (iii) foreseeable equipment failure (unless caused by an underlying Force Majeure Event); (iv) regulatory changes that were foreseeable at contract inception.

28.4 **Duration.** If a Force Majeure Event continues for more than **[60]** consecutive days, either Party may terminate the affected Services on **[30]** days' written notice without liability for termination charges.

> **[DRAFTING NOTE — CYBER ATTACKS AS FORCE MAJEURE]:** German courts have not uniformly accepted cyber attacks as Force Majeure events. A sophisticated ransomware attack may not qualify if the Service Provider failed to maintain adequate security controls (*Verschulden durch Unterlassen*). Distinguish between: (a) nation-state cyber warfare (potentially Force Majeure); (b) commercially motivated ransomware attacks (unlikely to be Force Majeure given NIS2 duty of care). Explicitly address cyber attacks in the Force Majeure clause or treat them separately under the security provisions.

---

### Section 29 — ANTI-CORRUPTION, SANCTIONS, AND EXPORT CONTROLS

29.1 **Anti-Corruption.** Each Party shall comply with all applicable anti-corruption and anti-bribery laws, including the German Anti-Corruption Laws (*Korruptionsstrafrecht*, §§ 331–335 StGB, § 299 StGB) and, where applicable, the UK Bribery Act 2010 and US Foreign Corrupt Practices Act.

29.2 **Sanctions.** Each Party represents and warrants that it is not, and its Affiliates, officers, and key employees are not, subject to EU, UN, or US sanctions. Each Party shall immediately notify the other if this representation ceases to be true.

29.3 **Export Controls.** The Service Provider shall comply with all applicable export control laws, including EU Dual-Use Regulation (Regulation (EU) 2021/821) and U.S. Export Administration Regulations (EAR), with respect to any technology, software, or data provided under this Agreement.

---

### Section 30 — DISPUTE RESOLUTION

30.1 **Escalation.** The Parties shall use reasonable efforts to resolve disputes through the governance escalation process in Section 6 before commencing formal proceedings.

30.2 **Mediation.** If a dispute is not resolved through escalation within **[30]** days, either Party may propose mediation. The mediator shall be appointed by the **[Deutsche Institution für Schiedsgerichtsbarkeit (DIS)]** or the **[Handelskammer Hamburg / München]** upon the Parties' joint request.

30.3 **Litigation.** If mediation fails or a Party declines mediation, disputes shall be submitted to the exclusive jurisdiction of the courts specified in Section 31.3.

**[OPTION — Arbitration instead of litigation:]** If mediation fails or is declined, disputes shall be finally resolved by arbitration under the DIS Arbitration Rules (**DIS-SchO**) by **[1/3]** arbitrators, conducted in **[Frankfurt am Main / Hamburg]**, in the **[German / English]** language. Arbitration awards are final and binding.

> **[DRAFTING NOTE — ARBITRATION VS. LITIGATION]:** For international B2B contracts, arbitration (DIS, ICC, LCIA) offers confidentiality and enforceability advantages. For domestic German B2B contracts, litigation before the commercial chambers (*Kammern für Handelssachen*) of the Landgerichte is often faster and cheaper. Some courts (notably Hamburg, Frankfurt, Cologne) offer proceedings in English. Consider also the German Technology & Patent Court (*Bundespatentgericht*) for IP disputes.

---

### Section 31 — GOVERNING LAW AND JURISDICTION

31.1 **Governing Law.** This Agreement and all non-contractual obligations arising out of or in connection with it are governed by the laws of the **Federal Republic of Germany**, excluding its conflict of law rules and excluding the UN Convention on Contracts for the International Sale of Goods (**CISG**).

31.2 **EU Law.** Nothing in this Agreement limits the direct application of EU Regulations.

31.3 **Jurisdiction.** The Parties irrevocably submit to the exclusive jurisdiction of the courts of **[Frankfurt am Main / Hamburg / Munich / Düsseldorf]** for the resolution of any disputes not subject to arbitration.

> **[DRAFTING NOTE — CHOICE OF COURT FOR FINANCIAL SECTOR]:** For contracts subject to BaFin oversight, Frankfurt am Main courts (LG Frankfurt, OLG Frankfurt) have significant expertise. For technology and IP disputes, Düsseldorf (LG/OLG Düsseldorf) has strong expertise in patent and IT matters. Munich (LG/OLG München) and Hamburg courts are also well regarded for commercial IT disputes.

---

### Section 32 — MISCELLANEOUS

32.1 **Entire Agreement.** This Agreement (including all Schedules and SOWs) constitutes the entire agreement between the Parties with respect to its subject matter and supersedes all prior negotiations, representations, and agreements.

32.2 **Amendments.** This Agreement may only be amended by a written document signed by duly authorised representatives of both Parties.

32.3 **Waiver.** Failure to exercise or delay in exercising any right under this Agreement does not constitute a waiver. Any waiver must be in writing.

32.4 **Severability.** If any provision of this Agreement is found invalid or unenforceable under Applicable Law, it shall be modified to the minimum extent necessary to make it valid and enforceable. All other provisions remain in full force.

32.5 **Assignment.** Neither Party may assign or transfer its rights or obligations under this Agreement without the other Party's prior written consent, not to be unreasonably withheld. Either Party may assign this Agreement to an Affiliate without consent, provided the assigning Party remains liable as guarantor. Assignment to a competitor of either Party requires consent and may be withheld at the other Party's discretion.

32.6 **No Partnership.** Nothing in this Agreement creates a partnership, joint venture, or agency relationship between the Parties. The Service Provider is an independent contractor.

32.7 **Third-Party Rights.** This Agreement does not confer any rights on third parties, except as expressly stated. The *Vertrag zugunsten Dritter* provisions of § 328 BGB do not apply unless expressly stated.

32.8 **Counterparts.** This Agreement may be signed in counterparts (including electronic signatures under Regulation (EU) 910/2014 (eIDAS) / eIDAS 2.0 (Regulation (EU) 2024/1183)), each of which is an original.

32.9 **Language.** This Agreement is executed in the **[English / German]** language. In the event of discrepancy between versions in different languages, the **[English / German]** version prevails.

> **[DRAFTING NOTE — ELECTRONIC SIGNATURES]:** Under eIDAS and eIDAS 2.0, qualified electronic signatures (QES) have equivalent legal effect to handwritten signatures throughout the EU. Advanced electronic signatures (AES) are legally recognised but may not satisfy form requirements for specific legal acts. For standard commercial contracts, AES (e.g., DocuSign, Adobe Sign) is sufficient under German law. For land charges or formation of certain company acts, QES or notarisation may be required.

---

**[SIGNATURE PAGE FOLLOWS]**

---

## SIGNATURE PAGE

**IN WITNESS WHEREOF**, the Parties have caused this Agreement to be duly executed by their authorised representatives as of the Effective Date.

**[SERVICE PROVIDER NAME]**

By: ___________________________

Name: _________________________

Title: __________________________

Date: __________________________


**[CUSTOMER NAME]**

By: ___________________________

Name: _________________________

Title: __________________________

Date: __________________________

---

---

# SCHEDULE OVERVIEW

| Schedule | Title | Status |
|---|---|---|
| Schedule 1 | Service Schedule(s) | [SPECIFY per service line] |
| Schedule 2 | Service Levels and SLA | [SPECIFY] |
| Schedule 3 | Commercial Terms and Fees | [SPECIFY] |
| Schedule 4 | Data Processing Agreement (DPA) | [Attach GDPR-compliant DPA] |
| Schedule 5 | Security Requirements | [ISO 27001/NIS2 baseline] |
| Schedule 6 | Approved Subcontractors | [List] |
| Schedule 7 | Key Personnel | [List] |
| Schedule 8 | Governance, Contacts and Escalation | [Matrix] |
| Schedule 9 | AI Components Register | [If applicable] |
| Schedule 10 | Exit Plan | [DR/BCP/Exit summary] |
| Schedule 11 | Data Processing Locations | [GDPR Chapter V / DORA] |
| Schedule 12 | Change Management Procedure | [Detail] |
| Schedule 13 | DORA-Specific Annex | [If financial sector] |

---

# ANNEX A — DRAFTING CHECKLIST

## Pre-Signature Compliance Checks

### GDPR / DSGVO
- [ ] DPA attached and compliant with Article 28 GDPR
- [ ] Data processing locations identified
- [ ] International transfer mechanism confirmed (SCCs, adequacy decision, BCRs)
- [ ] Data retention periods specified
- [ ] Data subject rights support obligations included
- [ ] DPIA conducted if high-risk processing
- [ ] Joint controller agreement if applicable

### NIS2 / BSIG
- [ ] Service Provider NIS2 compliance confirmed
- [ ] Security measures meet Article 21 NIS2 minimum requirements
- [ ] Supply chain security obligations included
- [ ] Incident notification timelines comply with NIS2 Article 23 (24h initial / 72h detailed / 1 month final)
- [ ] KRITIS obligations confirmed if applicable

### EU AI Act
- [ ] AI Components identified and risk-classified
- [ ] Prohibited AI systems confirmed absent
- [ ] High-risk AI documentation requirements met
- [ ] GPAI obligations confirmed if applicable
- [ ] Works council consultation completed (*BetrVG* § 87(1) No. 6 if employee monitoring involved)

### DORA (Financial Sector Only)
- [ ] DORA-mandated contractual provisions included (per Annex to DORA)
- [ ] ICT third-party risk register updated
- [ ] Concentration risk assessed
- [ ] Regulatory notification to BaFin/ECB prepared
- [ ] TLPT cooperation confirmed if DORA-critical provider

### EU Data Act
- [ ] Data access and portability obligations included
- [ ] Switching obligations meet Data Act Articles 23-31
- [ ] No manifestly disproportionate data access restrictions (Article 13 Data Act)
- [ ] Machine-generated data ownership addressed

### German Commercial Law
- [ ] Order of precedence clear and AGB exclusion included
- [ ] Auto-renewal compliant with § 309 No. 9 BGB
- [ ] Liability limitations compliant with §§ 307-309 BGB
- [ ] Payment terms comply with § 271a BGB (max 60 days B2B)
- [ ] Limitation periods compliant with §§ 195 et seq. BGB

### Cyber Resilience Act
- [ ] Software product obligations assessed (CRA Annex I)
- [ ] Security update obligations addressed
- [ ] Vulnerability disclosure obligations included

---

# ANNEX B — KEY REGULATORY REFERENCE TABLE

| Regulation | Citation | Key Obligations for IT Service Contracts | Applies From |
|---|---|---|---|
| GDPR | Regulation (EU) 2016/679 | Data processing agreement, security, breach notification | 25 May 2018 |
| BDSG | BGBl. I 2017, 2097 | German GDPR implementation, employee data | 25 May 2018 |
| NIS2 Directive | Directive (EU) 2022/2555 | Security requirements, incident notification | 18 Oct 2024 (DE) |
| EU AI Act | Regulation (EU) 2024/1689 | Risk-based AI obligations | Phased: 2025–2027 |
| EU Data Act | Regulation (EU) 2023/2854 | Data access, portability, cloud switching | 12 Sep 2025 |
| DORA | Regulation (EU) 2022/2554 | ICT third-party risk, financial sector | 17 Jan 2025 |
| Cyber Resilience Act | Regulation (EU) 2024/2847 | Product cybersecurity requirements | 11 Dec 2027 (most) |
| Digital Services Act | Regulation (EU) 2022/2065 | Platform obligations (if applicable) | 17 Feb 2024 |
| eIDAS 2.0 | Regulation (EU) 2024/1183 | Electronic signatures, identity wallets | Phased: 2024–2026 |
| GeschGehG | BGBl. I 2019, 466 | Trade secret protection | 26 Apr 2019 |
| IT-Sicherheitsgesetz 2.0 | BGBl. I 2021, 1122 | KRITIS security, BSI powers | 28 May 2021 |

---

> **DISCLAIMER**
> This template is provided for informational and drafting assistance purposes only. It does not constitute legal advice. All contractual arrangements should be reviewed by qualified German-qualified lawyers (*Rechtsanwälte*) experienced in IT and technology law before execution. Regulatory requirements change frequently — verify current law before use. No liability is accepted for reliance on this template without professional legal review.

---

*Template Version 1.0 | EU-Regulatory-Projects Repository | February 2026*
