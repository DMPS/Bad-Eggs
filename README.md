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

Customer Journey: Bob is the CEO of Zalmart Inc.  He is responsible for ensuring all company partners are 'above the board'

1.) How?:  Bob goes to www.badeggs.github.io and creates an account. He enters the bank account for his company and accepts the terms. 

2.) What?: The Bad Eggs app makes an API call to the Open Bank Project to retrieve Bob's transactions.  The transaction data includes the name of the payee.

3.) Who?:  The Open Corporates API performs a lookup on the payee name. It returns a brief summary of each payee.

4.) When?: The Payee name is matched against a consolidated list of all persons and entities that are subject to sanctions which are effective in the UK
http://www.hm-treasury.gov.uk/fin_sanctions_index.htm

5.) Bob sends a link to any other partners allowing them access to his Bad Eggs account and strongly encourages them to do the same.

6.) Where?: Bob recieves a push notification on his phone if a transaction is flagged by the system.

Suggested Outputs:

1.) Create a website

2.) API Call to Open Bank Project

3.) API Call to Open Corporates (Matti)

4.) API Call to Sanctions API (Self-Created) (Dalton)

5.) Push Notification System 

6.) Pitch for Sunday (James)

Resources: 
https://www.lawsociety.org.uk/support-services/advice/articles/checking-the-sanctions-list/

http://www.hm-treasury.gov.uk/fin_sanctions_index.htm
