# i18n

Esta biblioteca fornece funcionalidade i18n para Python 3 pronta para uso. 
O uso é baseado principalmente na biblioteca python-i18n.


## Instalação

Digite isto no seu cmd, terminal e afins.

    pip install https://github.com/Demonize-Me-Again/i18n.git

## Como usar o modulo

O uso mais simples, embora não muito útil, seria

```py
 from i18n import Files, Translator

 files = Files()
 files.load_folder()
 files = Translator(files=files, language='pt_BR')


 print(files.get('test|exemplo', values={"ola":"Olá"}))
```


## Definir a extensão

Para definir o tipo de arquivo que irá usar basta definir o valor no cabeçario da função  ``Files()`` o valor seria ``Files(file_extension='json')`` para json e ``Files(file_extension='yaml')`` para yaml.

Os formatos YAML e JSON são suportados para armazenar traduções. Com a configuração padrão, se você tiver usando o seguinte formato.


```py
 from i18n import Files, Translator

 files = Files(file_extension='json')
```

### test.json

```json
{
  "examplo":"{ola}, tudo bem?"
}
```
### test.yaml

    examplo: {ola}, tudo bem?

## Como definir o local da traduções

O local padrão da tradução dos arquivo é ``/json/translate/``, porém você pode
definir no cabeçario da ``Files()``

```py
 from i18n import Files, Translator

 files = Files(path='novo_local/traducoes')
```

## Carregar as traduções

Para carregar as traduções e obter-la basta chamar uma função do ``Files()``
que seu nome é ``load_folder()``, tendo isso em mente as traduções serão carregadas e armazenada num array da livraria.

```py
 from i18n import Files, Translator

 files = Files(path='novo_local/traducoes')
 files.load_folder()
```
Também podemos carregar arquivos de outro diretorio para globalizar, é podemos mudar o nome do tipo de leitura das linguagem ao trocar o regex em ``pattern``
ao invez de ser predefinido ``pt_BR`` que seria a pasta dos arquivos em português.

```py
 from i18n import Files, Translator

 files = Files(path='novo_local/traducoes')
 files.load_folder()
 files.load_folder(path='outro_local/traducoes', pattern='[a-z]')
```


## Obter as traduções

Para obter as traduções basta chamar uma função do ``Files()``
e passa-la pela função ``Translator()`` e definir a linguagem que deseja obter a tradução é chamar a função ``get()`` da função ``Translator()`` passando seus valores que são ``path``, é ``values`` que é opcional..

```py
 from i18n import Files, Translator

 files = Files()
 files.load_folder()
 files = Translator(files=files, language='pt_BR')
 
 print(files.get('test|exemplo', values={"exemplo":"Olá"}))
```