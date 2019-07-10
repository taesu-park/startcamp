# gitignore



 git init을 하면 해당 파일을 작성하는 습관을 들이자!

`.gitignore`파일에 작성된 파일 혹은 폴더 등은 git으로 관리되지 않는다. 예시는 다음과 같다.

```select a language
__pycache__/ # __pycache__ 폴더 안에 있는 내용 모두
*.zip		 # 확장자가 zip인 파일 모두
profie.jpg	 # profile.jpg 파일
```



처음에는 직접 만들기보다 gitignore에서 내 개발환경에 맞춰 만들어주는 파일을 적용하자.



예를 들면, pycharm을 쓰고 있을 떄 `.idea/`를 올리지 않는다거나, python에서는 `__pycache__`를 올릴 필요는 없다.

