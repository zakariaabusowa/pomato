from firebase import firebase
firebase = firebase.FirebaseApplication('https://stocker-929ba-default-rtdb.firebaseio.com/', None)
new_price = 'unavailbale'
result = firebase.post('/rtx3080/price', new_price)
print (result)