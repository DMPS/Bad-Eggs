# Bad-Eggs
Making the Sharing Economy Safer - Money Laundering

"The sharing economy struggles with the same issues facing bitcoin, the crypto-currency that has been criticized for its facilitation 
of money laundering and criminal activity as well as a lack of safety for its buyers."

Problem: 
-48% of respondents said that they did not check their clients against these sanctions lists. 
-Under The Al Qaida and Taliban (United Nations Measures) Order 2006 and the Terrorism (United Nations Measures) Order 2006, 
it is a criminal offence for any natural or legal person to:
deal with the funds of designated persons, or make funds and economic resources available, directly or indirectly for the benefit of designated persons.
-The list of sanctioned targets is very lengthy and updated frequently. It is not cost effective for SMEs to keep track of these lists.

Solution: Bad Eggs is a quick and passive way for SMEs to be alerted of doing business with individuals or companies on the sanctions list.

Customer Journey: Bob is the CEO of JetShare, a UK based private jet sharing business.  Xavier is a drug dealer who just scored £100K in an illegal deal. He wants to launder his money through his company, Dodgy Limited.

1.) Bob goes to www.badeggs.github.io and creates an account. He enters the bank account for his company and accepts the terms. 

2.) Xavier sets up two recurring payments. First, he pays BreatheBnB £1000 per day for 60 days to rent luxury suites in Paris, Rome, and Berlin. Second, he pays Bob £3500 per month for 10 months to use one of Bob's jets to fly to his rented flats around the world. 

3.) The Bad Eggs app makes an API call to the Open Bank Project to retrieve Bob's incoming and outgoing transactions.  The transaction data includes the £3500 payment from Xavier's company, Dodgy Limited.

4.) The Open Corporates API performs a lookup on the Open Bank Projects list of counterparties/payors. It returns a brief summary of each payee including information about Dodgy Limited.

5.) The Sanctions API matches all payor/counterparty names against a current list of all persons and entities subject to sanctions in the UK. Source: http://www.hm-treasury.gov.uk/fin_sanctions_index.htm

6.) Bob recieves a push notification on his phone to say that the incoming payment of £3500 from Xavier's company a transaction is potentiall fraudulent.

Suggested Outputs:

1.) Create a website (Matti)

2.) API Call to Open Bank Project (Dalton)

3.) API Call to Open Corporates (Complete)

4.) API Call to Sanctions API (Self-Created) (Complete)

5.) Push Notification System 

6.) Pitch for Sunday (James)

Resources: 
https://www.lawsociety.org.uk/support-services/advice/articles/checking-the-sanctions-list/

http://www.hm-treasury.gov.uk/fin_sanctions_index.htm
