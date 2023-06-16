1. Download official spec:

```
wget https://api.youneedabudget.com/papi/spec-v1-swagger.json
```

2. Convert from swagger to openapi 3:

```
java -jar ./swagger-codegen-cli-3.0.29.jar generate -l openapi -i spec-v1-swagger.json -o .
```

3. Manually make "note" and "memo" fields nullable in all locations.

For example, change:

```
"note" : {
  "type" : "string"
},
```

to:

```
"note" : {
  "type" : "string",
  "nullable" : true
},
```

4. Generate api:

```
java -jar openapi-generator-cli.jar generate -i openapi.json -g python --enable-post-process-file --package-name ynab_api
```

5. Optionally, format:

```
yapf -ir **/*.py
```
