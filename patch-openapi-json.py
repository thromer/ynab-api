import json
import sys

def main():
  api = json.loads(sys.stdin.read())

  schemas = api['components']['schemas']
  for k, v in schemas.items():
    required = set(v['required'] if 'required' in v else [])
    if 'properties' in v:
      for pk, pv in v['properties'].items():
        if not pk in required:
          pv['nullable'] = True
  sys.stdout.write(json.dumps(api, indent=2))

main()
