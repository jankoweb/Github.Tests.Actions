# TODO and FIXME List

## TODO
- [ ] [./.github/workflows/todo-file-generator.yml:1](./.github/workflows/todo-file-generator.yml#L1): name: Generate TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:19](./.github/workflows/todo-file-generator.yml#L19):       - name: Find TODO and FIXME
- [ ] [./.github/workflows/todo-file-generator.yml:21](./.github/workflows/todo-file-generator.yml#L21):           # Prohledá všechny soubory na TODO a uloží je do todos.tmp s cestou a číslem řádku
- [ ] [./.github/workflows/todo-file-generator.yml:22](./.github/workflows/todo-file-generator.yml#L22):           grep -rnw '.' -e "TODO" > todos.tmp || echo "No TODO found."
- [ ] [./.github/workflows/todo-file-generator.yml:26](./.github/workflows/todo-file-generator.yml#L26):       - name: Generate TODO.md in Root
- [ ] [./.github/workflows/todo-file-generator.yml:28](./.github/workflows/todo-file-generator.yml#L28):           echo "# TODO and FIXME List" > TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:29](./.github/workflows/todo-file-generator.yml#L29):           echo "" >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:31](./.github/workflows/todo-file-generator.yml#L31):           # Sekce TODO
- [ ] [./.github/workflows/todo-file-generator.yml:32](./.github/workflows/todo-file-generator.yml#L32):           echo "## TODO" >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:39](./.github/workflows/todo-file-generator.yml#L39):               echo "- [ ] [$file_path:$line_number]($file_path#L$line_number): $content" >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:42](./.github/workflows/todo-file-generator.yml#L42):             echo "No TODO comments found." >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:44](./.github/workflows/todo-file-generator.yml#L44):           echo "" >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:47](./.github/workflows/todo-file-generator.yml#L47):           echo "## FIXME" >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:54](./.github/workflows/todo-file-generator.yml#L54):               echo "- [ ] [$file_path:$line_number]($file_path#L$line_number): $content" >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:57](./.github/workflows/todo-file-generator.yml#L57):             echo "No FIXME comments found." >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:60](./.github/workflows/todo-file-generator.yml#L60):       - name: Commit and push TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:64](./.github/workflows/todo-file-generator.yml#L64):           git add TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:65](./.github/workflows/todo-file-generator.yml#L65):           git commit -m "Update TODO.md with latest TODO and FIXME comments" || echo "No changes to commit"
- [ ] [./testovaci-skript-s-todos.py:9](./testovaci-skript-s-todos.py#L9):     # TODO: Přidat personalizovaný pozdrav podle denní doby (např. dobré ráno, dobré odpoledne, dobrý večer)
- [ ] [./testovaci-skript-s-todos.py:30](./testovaci-skript-s-todos.py#L30):     # TODO: Přidat vstup pro uživatele, aby zadal své jméno a rok narození
- [ ] [./testovaci-skript-s-todos.py:34](./testovaci-skript-s-todos.py#L34):     # TODO: Implementovat kontrolu platnosti vstupu
- [ ] [./.git/hooks/sendemail-validate.sample:22](./.git/hooks/sendemail-validate.sample#L22): # Replace the TODO placeholders with appropriate checks according to your
- [ ] [./.git/hooks/sendemail-validate.sample:27](./.git/hooks/sendemail-validate.sample#L27): 	# TODO: Replace with appropriate checks (e.g. spell checking).
- [ ] [./.git/hooks/sendemail-validate.sample:35](./.git/hooks/sendemail-validate.sample#L35): 	# TODO: Replace with appropriate checks for this patch
- [ ] [./.git/hooks/sendemail-validate.sample:41](./.git/hooks/sendemail-validate.sample#L41): 	# TODO: Replace with appropriate checks for the whole series

## FIXME
- [ ] [./.github/workflows/todo-file-generator.yml:19](./.github/workflows/todo-file-generator.yml#L19):       - name: Find TODO and FIXME
- [ ] [./.github/workflows/todo-file-generator.yml:23](./.github/workflows/todo-file-generator.yml#L23):           # Prohledá všechny soubory na FIXME a uloží je do fixmes.tmp s cestou a číslem řádku
- [ ] [./.github/workflows/todo-file-generator.yml:24](./.github/workflows/todo-file-generator.yml#L24):           grep -rnw '.' -e "FIXME" > fixmes.tmp || echo "No FIXME found."
- [ ] [./.github/workflows/todo-file-generator.yml:28](./.github/workflows/todo-file-generator.yml#L28):           echo "# TODO and FIXME List" > TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:46](./.github/workflows/todo-file-generator.yml#L46):           # Sekce FIXME
- [ ] [./.github/workflows/todo-file-generator.yml:47](./.github/workflows/todo-file-generator.yml#L47):           echo "## FIXME" >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:57](./.github/workflows/todo-file-generator.yml#L57):             echo "No FIXME comments found." >> TODO.md
- [ ] [./.github/workflows/todo-file-generator.yml:65](./.github/workflows/todo-file-generator.yml#L65):           git commit -m "Update TODO.md with latest TODO and FIXME comments" || echo "No changes to commit"
- [ ] [./todos.tmp:2](./todos.tmp#L2): ./.github/workflows/todo-file-generator.yml:19:      - name: Find TODO and FIXME
- [ ] [./todos.tmp:6](./todos.tmp#L6): ./.github/workflows/todo-file-generator.yml:28:          echo "# TODO and FIXME List" > TODO.md
- [ ] [./todos.tmp:13](./todos.tmp#L13): ./.github/workflows/todo-file-generator.yml:47:          echo "## FIXME" >> TODO.md
- [ ] [./todos.tmp:15](./todos.tmp#L15): ./.github/workflows/todo-file-generator.yml:57:            echo "No FIXME comments found." >> TODO.md
- [ ] [./todos.tmp:18](./todos.tmp#L18): ./.github/workflows/todo-file-generator.yml:65:          git commit -m "Update TODO.md with latest TODO and FIXME comments" || echo "No changes to commit"
- [ ] [./testovaci-skript-s-todos.py:16](./testovaci-skript-s-todos.py#L16):     # FIXME: Ověřit, jestli je věk správný pro někoho, kdo se narodil ještě letos a neměl narozeniny
- [ ] [./testovaci-skript-s-todos.py:33](./testovaci-skript-s-todos.py#L33):     # FIXME: Pokud uživatel zadá neplatný rok, zobrazit chybovou zprávu
