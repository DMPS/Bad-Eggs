# Bad-Eggs
<h3>Making the Sharing Economy Safer via a Passive Money Laundering Monitoring System</h3>

See presentation on http://slides.com/daltonscott/deck-1/#/

<i>"The sharing economy struggles with the same issues facing bitcoin, the crypto-currency that has been criticized for its facilitation of money laundering and criminal activity as well as a lack of safety for its buyers."</i> - David Weiner, Wall Street Journal, 22 May 2014

<b>The Problem:</b>

-CEOs rely on accountants and lawyers to tell them if they are transacting with banned parties.  48% of respondents said that they did not check their clients against these sanctions lists. 

-Under The Al Qaida and Taliban (United Nations Measures) Order 2006 and the Terrorism (United Nations Measures) Order 2006, 
it is a criminal offence for any natural or legal person to:  deal with the funds of designated persons, or make funds and economic resources available, directly or indirectly for the benefit of designated persons.

-The list of sanctioned targets is very lengthy and updated frequently. It is not cost effective for SMEs to keep track of these lists.

<b> The Market:</b>

"Billions of pounds of corrupt cash are flowing through the UK’s financial sector, according to an official report." - Vanessa Houlden, FT

UK Businesses continue to export their products and services, currently valued at approximately £22.1 billion.

<b>The Solution:</b> 

Bad Eggs is a quick and passive way for SMEs to be alerted of doing business with individuals or companies on the sanctions list.

<b>The Customer Journey:</b> 

Bob is the CEO of JetShare, a London, UK based private jet sharing business.  Xavier is a drug dealer based in Acity, Acountry who just scored £100K in an illegal deal. He wants to launder his money through his company, Dodgy Limited.

1.) Bob goes to www.badeggs.github.io and creates an account. He enters the bank account for his company and accepts the terms. 

2.) Xavier sets up two recurring payments. First, he pays BreatheBnB £1000 per day for 60 days to rent luxury suites in Paris, Rome, and Berlin. Second, he pays Bob £3500 per month for 10 months to use one of Bob's jets to fly to his rented flats around the world. 

3.) The Bad Eggs app makes an API call to the Open Bank Project to retrieve Bob's incoming and outgoing transactions.  The transaction data includes the £3500 payment from Xavier's company, Dodgy Limited.

4.) The Open Corporates API performs a lookup on the Open Bank Projects list of counterparties/payors. It returns a brief summary of each payee including information about Dodgy Limited.

5.) The Sanctions API matches all payor/counterparty names against a current list of all persons and entities subject to sanctions in the UK. Source: http://www.hm-treasury.gov.uk/fin_sanctions_index.htm

6.) Bob recieves a push notification on his phone to say that the incoming payment of £3500 from Xavier's company a transaction is potentially fraudulent.  He submits a suspicious activity report (SAR) to the National Crime Agency. 

<b>The Benefits:</b>

-Businesses don't have to rely on their accountant to tell them if they are doing business with a sanctioned company(Disintermediation)

-Bob just has to log in and Bad Eggs takes care of the rest! We monitor his transactions and alert him of any suspicious activity

-As an investor, Bad Eggs has low implementation and build costs, so your ROI is high


<b>Outputs:</b>

1.) Create a website (Matti)

2.) API Call to Open Bank Project (Dalton)

3.) API Call to Open Corporates (Dalton)

4.) API Call to Sanctions API (Self-Created) (Dalton)

5.) Push Notification System (Future Delivery?)

6.) Pitch for Sunday (James)

<b>Resources:</b> 

https://www.lawsociety.org.uk/support-services/advice/articles/checking-the-sanctions-list/
http://www.hm-treasury.gov.uk/fin_sanctions_index.htm
https://www.uktradeinfo.com/Statistics/OverseasTradeStatistics/Pages/OTS.aspx
http://www.ft.com/cms/s/0/7d3a0a24-733d-11e5-a129-3fcc4f641d98.html#axzz43Qu6WZAQ

<b>Background:</b>

Startupbootcamp FinTech is back organising a FinTech hackathon at the Rainmaking Loft. The hackathon will be taking place on the weekend just after St. Patrick's Day. We are organising a hackathon on the theme of FinTech for Sharing Economy. 

<b>The Challenge:</b>

Intesa Sanpaolo - #1 Disintermediation and trust-based scoring methods

Sharing Economy implies the disintermediation of middle-men, such as institutions, as they are gradually replaced by platforms (e.g. P2P lending, crowdfunding, investment club). All these platforms allow users to directly access valuable assets (connections, knowledge, competencies and resources) through networks which act as trust-circles, relying on community and feedback as alternative scoring methods. Develop a model or a proof of concept about Sharing Economy showing how Financial Institutions may fully include such paradigm in their operational models and credit-scoring methodologies.

Any other cool stuff? 
We want to make this hackathon fun and inspiring, so we are happy that Open Bank Project and MyOrder will providing their API for the hackathon  Our global partner Amazon Web Services are offering credits for the hackathon so teams can use their platform during the event. And fun activities related to St. Patrick's Day of course.

<b>The Team</b>

Matti, James & Dalton
