form="file=@$PWD/cat.jpeg"
echo $form
curl --form $form 127.0.0.1:12344 -v