# log_processor_edstem


# TESTING

- python3 test.py

# Deployment to lamda functions





## # [Functions | Lambda](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions)


### 1. Navigate to AWS console and select lambda function and. Click on Create function
![Step 1 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/00a25698-8ac5-45ce-ace2-1a06e28c6c0b/0d0e684e-5808-4f1a-a5fb-ffbd5b6d1c5d.png?crop=focalpoint&fit=crop&fp-x=0.9358&fp-y=0.1189&fp-z=2.9426&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=792&mark-y=232&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNjMmaD05MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 2. Enter your desired function name in my case i added as "process_my_logs"
![Step 2 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/ad812741-86b9-484a-a739-c7176362d822/2c9b2770-d49f-464c-99ca-02f220b90925.png?crop=focalpoint&fit=crop&fp-x=0.3416&fp-y=0.3659&fp-z=1.0771&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=297&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz04MTImaD0zNCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 3. select the required run time 
![Step 3 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/f286ea97-8bd6-4a72-81c7-587d9f40754f/92b6c2c5-d99c-4d7f-a5c5-d7568f974a37.png?crop=focalpoint&fit=crop&fp-x=0.3416&fp-y=0.4734&fp-z=1.0771&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=382&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz04MTImaD0zNCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 4. Click on Python 3.13…
![Step 4 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/6b0fdd98-a336-441f-895f-586987e53bae/33f1e237-35bb-4694-87f4-9f5ff4b5c8b8.png?crop=focalpoint&fit=crop&fp-x=0.1840&fp-y=0.6328&fp-z=1.6305&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=54&mark-y=373&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02MTMmaD01MiZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 5. Change the architecture info if required 
![Step 5 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/21d7dd23-eab8-41f7-a5d7-c03032fc9ac3/15193bb8-3fbf-4483-b471-fda92067b821.png?crop=focalpoint&fit=crop&fp-x=0.3416&fp-y=0.5671&fp-z=1.0771&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=403&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz04MTImaD00NCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 6. Click on Create function
![Step 6 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/a788ea2d-8dc1-492c-a87b-2870de17a22e/dee47e0a-e278-4ee3-8b04-dad03ca79a4a.png?crop=focalpoint&fit=crop&fp-x=0.9358&fp-y=0.8506&fp-z=4.0000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=645&mark-y=335&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz00OTQmaD0xMjcmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 7. Click on lambda_function.py, preview
![Step 7 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/73b87148-dc61-4796-ba0a-933cc9987356/c08f240f-148c-476e-b68a-1afe9bade726.png?crop=focalpoint&fit=crop&fp-x=0.6156&fp-y=0.9034&fp-z=1.3236&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=11&mark-y=383&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTc5Jmg9NjI1JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 8. change the function name , based on your required name (optional)
![Step 8 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/aa64a3ba-d15d-49fc-818e-45992866ef7e/fc89e94a-6105-41dc-9cf4-8c84071b50a8.png?crop=focalpoint&fit=crop&fp-x=0.3817&fp-y=0.6564&fp-z=3.0685&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=589&mark-y=367&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yMyZoPTYzJmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 9. Copy text area titled "process_my_logs"
![Step 9 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/2e6083c9-fa44-4db9-9a57-dcd0f0833f88/4a9caf52-3cbb-4447-9659-5e9175986e80.png?crop=focalpoint&fit=crop&fp-x=0.3817&fp-y=0.6564&fp-z=3.0685&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=589&mark-y=367&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yMyZoPTYzJmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 10. Click on Edit
![Step 10 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/214d21dc-11c5-4160-946d-951f32c56637/64a12d44-0e5e-4b89-b98c-ad3135c70f2a.png?crop=focalpoint&fit=crop&fp-x=0.7350&fp-y=0.7610&fp-z=3.4385&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=493&mark-y=344&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yMTMmaD0xMDkmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 11. rename the handler with your function name
![Step 11 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/ade7c763-cb01-40bc-b1da-2a14ba4dcbf1/85487265-cae9-4f0d-96d7-19975bea5ed2.png?crop=focalpoint&fit=crop&fp-x=0.3416&fp-y=0.3220&fp-z=1.0771&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=260&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz04MTImaD0zNCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 12. Click on Save
![Step 12 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/61fc2743-8a4c-4c77-ab9b-5f28e16f849a/30186021-7a18-4ad1-8950-63dafe8ba54d.png?crop=focalpoint&fit=crop&fp-x=0.9596&fp-y=0.5896&fp-z=2.9426&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=960&mark-y=352&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xOTUmaD05MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 13. Click on Test
![Step 13 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/c3ab2575-32e5-4880-9db3-f396f1aa7769/0eb7bb18-2dbe-4bec-8811-6daae92ca091.png?crop=focalpoint&fit=crop&fp-x=0.0920&fp-y=0.4140&fp-z=2.8480&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=243&mark-y=341&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xNDMmaD0xMTYmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 14. create a new test event  , i created as  "test_event_1"
![Step 14 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/79729397-6754-44a9-850e-4056edb90e42/f8480820-6c0a-4f4e-ab6b-37c0e754d8da.png?crop=focalpoint&fit=crop&fp-x=0.5004&fp-y=0.6215&fp-z=1.0281&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=16&mark-y=471&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTY3Jmg9MzMmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 15. add your required body 
![Step 15 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/fb5fe8da-3766-4116-bbbe-1e63becaf311/273ccfae-4b42-456b-8992-355f279de7c1.png?crop=focalpoint&fit=crop&fp-x=0.5139&fp-y=0.6713&fp-z=1.0584&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=17&mark-y=357&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTY1Jmg9MzI2JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 16. Click on Save
![Step 16 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/5a1f558d-39b4-4278-bebf-5cebdaba113b/9241c8fe-7623-4470-9783-540c6c41283a.png?crop=focalpoint&fit=crop&fp-x=0.8934&fp-y=0.5757&fp-z=2.9426&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=726&mark-y=352&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xOTUmaD05MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 17. Click on Test
![Step 17 screenshot](https://images.tango.us/workflows/af86e0e9-e058-4527-8b21-12e51f739799/steps/27bd4c9e-0a31-4c6a-b0fa-3767f4a31233/512a300f-b183-4155-8a6c-f7b1a67d0ba0.png?crop=focalpoint&fit=crop&fp-x=0.9473&fp-y=0.5757&fp-z=2.9426&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=921&mark-y=352&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xODUmaD05MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)



### 
# Deployment to API Gateway



### 1. Navigate to aws console and search for api gateway and. Click on Create API
![Step 1 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/ab424ee9-4509-438b-afef-131e4a93ad5d/90144ac9-98ae-4838-acc1-40227a14c4fe.png?crop=focalpoint&fit=crop&fp-x=0.9334&fp-y=0.1946&fp-z=2.9426&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=823&mark-y=352&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yODQmaD05MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 2. Select REST API and click on build
![Step 2 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/50689b27-6124-42ae-8add-7fc87185f073/e073e545-a637-4ffa-bc31-c4d6f029263c.png?crop=focalpoint&fit=crop&fp-x=0.9451&fp-y=0.7523&fp-z=3.7370&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=824&mark-y=339&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yNTkmaD0xMTkmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 3. Enter your desired API name and select new api option
![Step 3 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/6ec1b452-a5a4-44a0-bfb4-b0d1280a62b7/46a52f7c-2aeb-4b48-8a6e-c6d99b7693cd.png?crop=focalpoint&fit=crop&fp-x=0.3416&fp-y=0.4562&fp-z=1.0771&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=375&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz04MTImaD0zNCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 4. Click on Create API
![Step 4 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/111b17d7-c542-476f-88bb-14d49af48125/09fe94f5-5de1-4bdb-970d-6a8a41fdfa10.png?crop=focalpoint&fit=crop&fp-x=0.9466&fp-y=0.7364&fp-z=3.5269&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=804&mark-y=343&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNDAmaD0xMTImZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 5. Once you landed to the dashboard , Click on Create method
![Step 5 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/06b9e319-ee83-442e-8e35-d504bee207df/8afc0776-99a6-4128-8c72-3978fd296b41.png?crop=focalpoint&fit=crop&fp-x=0.9234&fp-y=0.3997&fp-z=2.9426&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=753&mark-y=352&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNTQmaD05MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 6. Click on Select a method type
![Step 6 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/ef10b7ff-41c4-404f-b9ad-6908ffe7afb3/8638d3bf-1758-4d7b-a04a-354aa177a5f2.png?crop=focalpoint&fit=crop&fp-x=0.3416&fp-y=0.3260&fp-z=1.0771&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=263&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz04MTImaD0zNCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 7. Select POST method
![Step 7 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/8f6b1deb-f3c9-427d-8ec5-460a22a04f73/37c5d0fc-a5a1-4f9a-a22b-b6e89f2853a0.png?crop=focalpoint&fit=crop&fp-x=0.3416&fp-y=0.5372&fp-z=1.0771&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=383&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz04MTImaD0zNCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 8. Click on Lambda function
![Step 8 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/be9b1d29-698f-4554-9c72-3831e7b8af71/0b62dab7-bd7a-42e4-99b7-731a36a1c1c1.png?crop=focalpoint&fit=crop&fp-x=0.3411&fp-y=0.6275&fp-z=1.6399&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=295&mark-y=373&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02MTAmaD01MiZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 9. select our lambda function , which we created process_my_logs 
![Step 9 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/db04a70f-5875-48ca-b15b-abbb4d757368/2d73b96a-2061-447f-bc95-f919f8baceb3.png?crop=focalpoint&fit=crop&fp-x=0.3411&fp-y=0.6633&fp-z=1.6399&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=295&mark-y=373&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02MTAmaD01MiZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 10. Click on Create method
![Step 10 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/e11f38ed-0355-4c30-a6e5-c3bf8c526820/ec3c1924-771f-4473-a07a-c776d6b4b36e.png?crop=focalpoint&fit=crop&fp-x=0.9371&fp-y=0.9137&fp-z=4.0000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=658&mark-y=459&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz00ODEmaD0xMjcmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 11. Once after redirection , now Click on Deploy API
![Step 11 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/9a8d5bb0-1741-4c74-ab86-88bd22116229/d613adc8-ec34-4925-9950-826733edd3bf.png?crop=focalpoint&fit=crop&fp-x=0.9457&fp-y=0.2032&fp-z=2.9426&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=862&mark-y=352&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yOTMmaD05MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 12. Click on *New stage*…
![Step 12 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/aa4d8c0a-7ad4-47ac-bcfc-81716579386e/fe668e35-60d0-4d7c-bd19-258819135561.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5120&fp-z=1.4793&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=266&mark-y=375&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02NjcmaD00NyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 13. Enter your staging name example : "process-logs-v1"
![Step 13 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/c56f3583-197d-4ace-b87e-e777a8df92ec/f38852e9-179e-4998-b001-bfcba842e90c.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.4661&fp-z=1.4793&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=266&mark-y=375&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02NjcmaD00NyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 14. Click on Deploy
![Step 14 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/35cbc7d1-f3d7-4edb-b866-fef233e2397b/29b1fed4-ad4c-49ed-9316-d1bbeb4d5430.png?crop=focalpoint&fit=crop&fp-x=0.6560&fp-y=0.7304&fp-z=2.7341&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=492&mark-y=355&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yMTYmaD04NyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 15. Now test this link your POSTMAN or in CURL 
![Step 15 screenshot](https://images.tango.us/workflows/32e64bc3-0b8d-4351-b455-4b344110bbfe/steps/8148f23d-562c-461d-b64f-af8d6bb1e229/4d5cbe18-e00d-427f-b1ba-ff57326f41b1.png?crop=focalpoint&fit=crop&fp-x=0.7004&fp-y=0.5212&fp-z=1.7471&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=28&mark-y=379&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTQ0Jmg9MzkmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)



# TESTING IN POSTMAN / CURL


```

curl -X POST https://utv97slwoi.execute-api.us-east-1.amazonaws.com/process-logs-v1 \
     -H "Content-Type: application/json" \
     -d '{
       "candidate_id": 121211,
       "log_content": "[2024-01-07 10:15:30] ERROR: Database connection\nfailed\n[2024-01-07 10:15:35] INFO: Retry attempt 1"
     }'
```






