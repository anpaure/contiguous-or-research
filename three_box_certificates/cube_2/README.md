# Certificate for `g_3(2,2,2)=10`

Files:

- `2_2_2_n10.word`: a verified length-10 word;
- `cube222_n9.cnf`: the sound-and-complete length-9 CNF;
- `cube222_n9.drat.gz`: Kissat's compressed DRAT refutation;
- `cube222_n9_check.log`: output of `drat-trim` ending in `s VERIFIED`.

Recheck the upper certificate after compiling the repository generator:

```bash
g++ -O3 -std=c++17 three_box_exact_sat.cpp -o three_box_exact_sat
./three_box_exact_sat verify 2 2 2 \
  three_box_certificates/cube_2/2_2_2_n10.word
./three_box_exact_sat witness 2 2 2 \
  three_box_certificates/cube_2/2_2_2_n10.word
```

Recheck the lower certificate with `drat-trim`:

```bash
gzip -dc three_box_certificates/cube_2/cube222_n9.drat.gz > /tmp/cube222_n9.drat
drat-trim three_box_certificates/cube_2/cube222_n9.cnf /tmp/cube222_n9.drat
```

Expected final line:

```text
s VERIFIED
```

The CNF encoding is documented in `THREE_CHAIN_BOX_EXACT.md` and implemented
by `three_box_exact_sat.cpp`.
