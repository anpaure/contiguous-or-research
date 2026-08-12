# Audit of `K11_CENTRAL_THREE_LAYER_EXACT_PACKING.md`

## Verdict

**PASS.**  The frozen 463-entry word covers every rank-five, rank-six, and
rank-seven mask in singleton, pair, and triple windows respectively.  Its
selected witnesses attain endpoint saving `1583`, and the general
three-antichain incidence cap proves that no admissible packing can exceed
`1583`.

The conclusion is therefore exact:

```text
Lambda_3(C([11],5),C([11],6),C([11],7)) = 1583.
```

There is one terminology qualification.  The complete raw window rows are
not all literally bijections: the first 462 singleton windows are a
bijection onto rank five (the final singleton is the rank-one mask `4`), all
462 pair windows are a bijection onto rank six, and the 461 triple windows
are a **surjection** onto the 330 rank-seven masks.  Their multiplicity
histogram `(multiplicity -> number of masks)` is

```text
1 -> 218,  2 -> 95,  3 -> 15,  4 -> 2.
```

Selecting the first triple occurrence of each rank-seven mask gives the
required 330-element bijection of targets to chosen triple witnesses.  This
is the selection used in the endpoint packing and is exactly what the theorem
note and checker claim; the raw-row distinction does not change the result.

In particular, exact simultaneous endpoint ordering does not lower the
three-family value to `1579` or `1577`; these ranks alone cannot recover the
rank-count bound `465` or force `466`.

## Independent reconstruction

Two checkers use different starting points.

1. `scratch/check_k11_central_three_layer_exact_packing.py` starts with the
   frozen rank-six Hamilton path, reconstructs the 463-entry word, and checks
   the complete endpoint packing including all three bichromatic forests.
2. `scratch/audit_k11_central_three_layer_exact_packing.cpp` starts only with
   the frozen 463-entry word.  It independently rediscovers all selected
   singleton, pair, and triple witnesses, checks every interval OR, every
   endpoint chain, and each bichromatic projected forest, and reproduces the
   upper-bound arithmetic.

The frozen inputs hash to

```text
71dfa5b4c33c86dee070b46fb991d9c8a0ef2c9d49a09825fc96d8e8c398552f
  scratch/certificates/k11_distance19/k11_allbase_r7full.txt

2f71437d1c9294a3dd886f28cdba85b2c8992696d201d569a943f37681db88a8
  scratch/certificates/k11_central_567_factor.txt
```

The reproduction commands are

```text
python3 scratch/check_k11_central_three_layer_exact_packing.py

g++ -O2 -std=c++20 scratch/audit_k11_central_three_layer_exact_packing.cpp \
  -o /tmp/audit_k11_central_three_layer_exact_packing
/tmp/audit_k11_central_three_layer_exact_packing
```

Both print `PASS`.

## Proof audit

* The 461 consecutive rank-six intersections are distinct rank-five masks.
  The sole omitted mask, `535`, lies in the first rank-six vertex, so adjoining
  it at the front turns the intersections into all 462 rank-five masks.
* Consecutive rank-five entries are distinct five-subsets of the same six-set,
  hence their union is exactly that six-set.  The terminal singleton `4`
  supplies the final pair.
* Triple windows are unions of consecutive pair windows.  The frozen path's
  upper colours are all 330 rank-seven masks.
* The chosen witnesses have 462 distinct left endpoints and 463 distinct
  right endpoints.  Their saving is therefore
  `(1254-462)+(1254-463)=1583`.
* The two endpoint sides contain, in total, one singleton block, 265
  two-target blocks, and 659 three-target blocks.  Thus their directly
  recomputed statistics are

  ```text
  S=265+2*659=1583,
  p=265+3*659=2242,
  D=2*265+3*659=2507,
  D=3S-p.
  ```

  The three actual bichromatic projections have respectively `923`, `659`,
  and `660` distinct edges; each has maximum degree two and is acyclic.
  Hence the displayed physical endpoint blocks are admissible in the exact
  definition of `Lambda_3`, not merely in a numerical relaxation.
* For any three-family packing, the three projected forests have at most
  `923`, `660`, and `660` edges.  With `D=3S-p<=2V`, this gives
  `S<=floor((2508+2243)/3)=1583`.

No universality claim is made for the 463-entry word outside ranks 5--7.
Accordingly, the certificate does not contradict `nu(11)>=465`; it closes
only the proposed central three-antichain endpoint obstruction.
