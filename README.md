# EnjoyMap

EnjoyMap - веб-сайт с картой г. Москва и отмеченными местами, интересными для посещения.
Хотите интересно провести время в Москве и развеяться? Направляйтесь к ближайшей к вам метке на карте. Или выберите ту, которая заинтересует больше всего?

## Демоверсия
Сайт развёрнут для демонстрации [здесь](https://askripko.pythonanywhere.com/)   
<img height="500" src="https://github.com/Skripko-A/enjoymap/blob/master/readme_docs/enoymap_mobile2" width="240"/>
<img height="500" src="https://github.com/Skripko-A/enjoymap/blob/master/readme_docs/enjoymap_mobile_1" width="240"/>

### Админка  
[https://askripko.pythonanywhere.com/admin](https://askripko.pythonanywhere.com/admin)  
Для того, чтобы добавить новую локацию на панели администратора:  
 - зайдите в раздел Locations
 - кликните кнопку `ADD LOCATION +` в правом верхнем углу
 - заполните поля и добавьте фотографии
 - кликните кнопку `SAVE` внизу
 - новая локация сразу появляется в БД и на карте  
### Загрузка новых локаций программно
Предусмотрено программное добавление локаций с помощью команды `load_place`.  
Вам понадобится готовый файл с данными о локации (он очень похож на поля, которые мы заполняем в админке)
Например, такой json с данными для [антикафе Bizone](https://raw.githubusercontent.com/Skripko-A/enjoymap/master/readme_docs/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json): 

 - В терминале зайдите в виртуальное окружение  
```bash
cd project_directory
source .venv/bin/activate
 ```
 - Скопируйте ссылку на json файл с данными
 - запустите процесс загрузки новой локации из вашего json файла:
```commandline
python3 manage.py load_place https://ссылка на файл с данными
```
 - Дождитесь сообщения о том, что локация успешно добавлена:
![](https://github.com/Skripko-A/enjoymap/blob/master/readme_docs/load_place_demo.png)

## Лицензия

Этот проект лицензирован под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.

[Readme для разработчика](https://github.com/Skripko-A/enjoymap/blob/master/readme_for_dev.md)