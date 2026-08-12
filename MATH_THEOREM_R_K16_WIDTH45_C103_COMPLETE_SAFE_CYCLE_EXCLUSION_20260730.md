# K16 WIDTH45 count-103: complete safe-cycle exclusion and the exact fractional gap

Date: 2026-07-30  
Lane: R  
Status: **proved source-relative binary exclusion at count 103; no literal K16 word claim**

## 0. Main result

Consider the frozen K16 asymmetric carrier, its 12,870 transition ports, and
the authenticated catalogue of 211,604 directed seams.  Give every selected
port capacity one, impose cyclic Sep5 on each frozen source component, and
require all 93 WIDTH45 residual targets to be serviced.  Then there is no
endpoint-balanced binary seam selection of cardinality 103.

More precisely, the exact scale-four identity leaves three count-103 ledgers:

```text
A  exact-once service,                    slack 4;
B  one repeated price-3 target,           slack 1;
C  one repeated price-4 target,           slack 0.
```

All three are excluded by complete directed safe-cycle classifications:

```text
B: 43 safe cycles containing the unique slack-1 seam;
   every one already has a forbidden repeat signature.

C: 56 safe tight cycles, of which 52 are locally compatible;
   their provider union omits 33 mandatory targets.

A: 385 safe target-simple cycles, with slack histogram
   0^22, 2^15, 3^50, 4^298 and no slack-1 cycle;
   all 343 possible positive cycle seeds fail exact target completion by
   the 884,763 compatible tight subsets.
```

The previously proved WIDTH45 parity theorem gives the lower bound 103 in
this same frozen catalogue.  The new exclusion therefore raises the exact
**frozen source-relative WIDTH45/global-Sep5 floor to 104**.

This is not a proof of an unrestricted K16 word lower bound.  Another carrier,
an exterior-moving rethread, a seam outside this catalogue, or a different
physical interface is not excluded.

There is a genuine integrality gap.  Both surviving continuous faces A and B
have independently replayed exact rational points at mass 103.  Thus the
binary result is not a linear/Farkas consequence of the current capacity,
Sep5, service and activator rows.

## 1. Frozen model

Let `P` be the 12,870 ports and `E` the 211,604 authenticated directed seams.
For `e=(u,v)`, let

* `h_te` be the authenticated WIDTH45 target incidence;
* `a_t in {3,4,6,8}` be the target price;
* `Phi:P->{0,...,7}` be the exact scale-four potential; and
* 
  ```text
  s_e = 4 + Phi(v)-Phi(u)-sum_t a_t h_te >= 0
  ```
  be the integral seam slack.

The 93 target prices sum to 408.  For a binary seam vector `x`, endpoint
balance and port capacity are

```text
sum_{e out of p} x_e = sum_{e into p} x_e = d_p,
d_p in {0,1}.
```

If `p,p+1,...` are the cyclic positions in one frozen source component,
global Sep5 is

```text
d_p+d_(p+1)+...+d_(p+4) <= 1
```

at every cyclic start.

There are 150 authenticated width-five endpoint occurrences.  A selected
occurrence seam has its two endpoints cut.  Each of its three collateral
positions lies within cyclic distance at most four of an endpoint.  Therefore
binary balance plus Sep5 forces every collateral cut to zero and forces the
occurrence activator to equal the seam selector.  Treating those 150 hits as
ordinary seam hits is consequently exact for every binary point considered
here.

Potential telescoping gives

```text
4 sum_e x_e = sum_t a_t mu_t + sum_e s_e x_e,
mu_t = sum_e h_te x_e.
```

At count 103, put

```text
R = sum_t a_t(mu_t-1),
S = sum_e s_e x_e.
```

Then

```text
R+S=4.
```

Since all targets are covered and the least price is three, the only integral
possibilities are `(R,S)=(0,4),(3,1),(4,0)`, namely A, B and C above.

## 2. Complete cycle normal form

### Lemma 2.1

Every endpoint-balanced binary capacity-one seam set is a vertex-disjoint
union of directed simple cycles.  Each constituent cycle is internally Sep5
safe.  Conversely, a family of pairwise port/Sep5-compatible directed simple
cycles is endpoint-balanced and capacity one.

### Proof

At every used port indegree equals outdegree and is at most one.  Following
successors therefore returns to the starting port, and distinct components
are directed simple cycles.  Sep5 restricts every subset, hence each cycle.
The converse follows by adding the cycle incidences.  QED.

For a cycle `Q`, let

```text
ell(Q)   = number of seams,
sigma(Q) = sum_{e in Q} s_e,
H(Q)     = multiset of target incidences on Q.
```

Potential telescoping on one cycle gives

```text
4 ell(Q) = sum_{t in H(Q)} a_t + sigma(Q).
```

Every cycle in a count-103 point has length at most 103.  In branch A every
cycle is target-simple.  In B, every cycle is target-simple except that the
unique global price-three repeat may occur twice on one cycle or once on two
cycles.  In C the analogous statement holds for the unique price-four repeat.

### Lemma 2.2 (canonical complete enumeration)

For a nonnegative slack budget `b`, every admissible directed simple cycle of
total slack at most `b` is enumerated exactly once by the following rules.

1. A tight cycle is rooted at its unique least tail port, and every nonclosing
   visited port must be larger than that root.
2. A positive-slack cycle is rotated to begin with its unique least positive
   seam id; every later positive seam must have larger id.
3. Depth first search retains only simple paths, the required target
   multiplicity, cyclic Sep5, total slack at most `b`, and length at most 103.

### Proof

Every tight simple cycle has one least port, so rule 1 fixes exactly one
rotation.  Every positive cycle has one least positive seam id, so rule 2 does
the same.  Once the anchor is fixed, its ordered outgoing seam sequence is
unique.  The depth-first recursion tries every allowed outgoing seam, hence
inductively reaches every admissible sequence.  The pruning rules are all
necessary for a selected cycle and therefore remove no admissible one.  QED.

The native enumeration and a separately implemented Python enumeration use
these two canonicalizations.  The native run ended with `stopped=false`.
The independent implementation hash-checks and reparses every record of the
exported branch-A graph and obtains the identical ordered seam-cycle set.
Completeness of that graph relative to the raw seam/WIDTH45 inputs is supplied
separately by the hash-pinned exporter and its byte-identical replay.

## 3. Branch B is impossible

In B, `S=1`.  Because every seam slack is a nonnegative integer, exactly one
selected seam has slack one and every other selected seam is tight.  The
cycle containing that seam consists of the slack-one seam followed by a tight
return path.  Hence its slack-one seam must be one of the 43 authenticated
seams admitting a tight return.

An independent search over all 7,742 tight seams and these 43 slack-one seams
visited 189,207 return-path states and found exactly 43 globally Sep5-safe
slack cycles.  Their repeated-target signatures are

```text
15 cycles: [(price 3, load 2), (price 4, load 2)]
15 cycles: [(price 4, load 2)^4, (price 6, load 2)]
13 cycles: [(price 8, load 2), (price 8, load 2)].
```

The first family contains the one repeat B could allow but also a forbidden
price-four repeat.  The other two families contain several forbidden repeats.
No further selected cycle can remove an existing occurrence.  Thus none of
the 43 cycles can occur in a branch-B point, whereas every branch-B point
would have to contain one.  Branch B is impossible.

This argument permits the allowed price-three repeat to lie on a different
cycle: the local compatibility predicate accepts either no internal repeat or
exactly one price-three load two.  All 43 cycles fail even that weaker test.

## 4. Branch C is impossible

Branch C is all-tight and has one price-four repeat.  Complete enumeration
from the raw graph gives 56 globally Sep5-safe tight cycles.  Four cycles
already have three distinct price-eight targets at load two, so they cannot
occur.  The remaining 52 cycles have either no repeat or one price-four load
two and are the complete locally compatible branch-C bank.

Their provider union contains only 60 of the 93 targets.  The omitted targets
are exactly all 30 price-three targets and all three price-six targets:

```text
33337,33906,35044,36417,36599,36935,37320,40066,40430,41102,
41872,46811,47343,47364,48092,48583,49436,50976,51067,51235,
56173,56439,57059,58301,58385,60854,60987,61297,61918,61960,
63261,63416,64398.
```

Every branch-C support is a union of cycles from those 52 columns.  It cannot
service any omitted target.  Therefore branch C is impossible.  This is an
independent safe-cycle proof of the branch already excluded by the earlier
tight GF(2) locks.

## 5. Branch A is impossible

Branch A services every target exactly once, so every constituent cycle is
target-simple.  A complete graph export retains every seam of slack at most
four:

```text
slack 0        7,742 seams
slack 1        9,484 seams
slack 2       10,003 seams
slack 3       19,880 seams
slack 4      124,707 seams
total        171,816 seams.
```

The native canonical search and the independent search return the identical
385-cycle set.  The independent search visits 29,577 tight states and
2,082,069 positive states.  Its exact slack histogram is

```text
cycle slack 0       22
cycle slack 1        0
cycle slack 2       15
cycle slack 3       50
cycle slack 4      298
total              385.
```

Since total branch-A slack is four and there is no slack-one cycle, the only
possible cycle-slack ledgers are

```text
[4]       one slack-four cycle; or
[2,2]     two slack-two cycles.
```

A slack-three cycle cannot be completed to total four.  There are 298
slack-four seeds.  Among the `binom(15,2)=105` pairs of slack-two cycles,
exactly 45 are target-disjoint and globally Sep5 compatible.  Thus there are
343 possible positive seeds.

The 22 tight cycles have exactly 884,763 target-disjoint, mutually Sep5-safe
subsets, representing 884,736 distinct target-union masks.  For each of the
343 positive seeds, take the exact complement of its target set in the
93-target universe.  None of those 343 complements occurs among the tight
target-union masks:

```text
positive seeds with an exact tight target complement     0
complete target covers                                   0.
```

This contradiction is already at the target-union level.  No appeal to a
SAT solver or to the remaining seed-versus-tight physical conflict rows is
needed.  Hence branch A is impossible.

## 6. Exact continuous points and the integrality gap

The binary exclusions do not extend to the corresponding linear faces.

### Face B

The exact rational point has

```text
82 simple-cycle columns
602 positive seams
14 positive price-three excess coordinates
mass 103, slack 1
common denominator LCM 3815626875992349417192.
```

An independent checker verifies endpoint balance, capacity, all 12,870 Sep5
rows, all 750 occurrence inequalities, all 93 service rows, and the exact
physical scale-four ledger.

Only eight of its 82 particular cycles are individually usable as Boolean
branch-B columns; the restricted basis misses 33 targets.  The complete
global safe-cycle classification in Section 3, rather than that restricted
basis failure, proves the binary no-go.

### Face A

A complete 171,711-arc capacity/Sep5 LP produced a 647-seam basic point.  It
was exactified over `QQ` into

```text
101 simple-cycle columns
647 positive seams
mass 103, exact-once service, slack 4
common denominator LCM 434876746114120
maximum port mass 10226126778567/10871918652853 < 1
seven active cyclic Sep5 rows.
```

The independent fail-closed checker again verifies all endpoint, capacity,
Sep5, service, activator and scale-four rows exactly.  Only 20 of these 101
particular cycles survive the Boolean column filters, so this decomposition
is not a rounding basis.  The global 385-cycle exhaustion in Section 5 is the
decisive integral result.

Thus both A and B exhibit exact rational feasibility at count 103 while all
three integral ledgers are impossible.

## 7. Corollary and exact scope

### Corollary 7.1

Every endpoint-balanced binary WIDTH45/global-Sep5 target cover drawn from
the frozen 211,604-seam catalogue uses at least 104 seams.

### Proof

The authenticated scale-four/GF(2) theorem excludes counts at most 102.
At count 103, the exact identity leaves only A, B and C.  Sections 3--5
exclude all three.  QED.

This corollary is integral and source-relative.  It preserves the complete
binary occurrence interface because Sep5 forces every selected WIDTH5
activator.  It does **not** assert any of the following:

* that every possible K16 carrier lies in this seam catalogue;
* that reverse/exterior-moving seams absent from the catalogue are illegal;
* that a count-104 seam cover exists;
* that q1, survivor, connectivity, COMP3, boundary absorption, or literal
  contiguous-OR verification has been solved; or
* that the unrestricted value of `nu(16)` has changed.

## 8. Frozen artifacts

### Common inputs

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
scratch/k16_width45_provider_path_dual_20260730.audit.json
  SHA-256 115ce4dfbcfdbd652c0696f21c6f44b5ed58737f16752fa1e5bd203477c12f4a
scratch/k16_width45_symmetric_scale4_potential_20260730.audit.json
  SHA-256 1b7676e70e209dd2437c042e93eb11a853e35da2899452c1200c188b82d42920
```

### Branches B and C

```text
scratch/audit_r_k16_width45_c103_branchB_safe_cycles_20260730.py
  SHA-256 c33fc54274f3e4e13691efdba2334d39e1c37fe8f3a6ae1ece888ac905630761
scratch/branchBC_safe_cycles_v2.audit.json
  SHA-256 325bd367eccb578eb5e873e97eda78e5426476e3c9399bc068fb7a40d2c38ed2
  payload d531dbf7ede833d2e737a607dcb0ac893cadfcf495c0e0311cfcc551d4e03a32
scratch/cycles_notarget.json
  SHA-256 fcacacafede479c0ebfd361ad5a9a7daf3313c93006bde2e943389a46cf0fe8e
```

The combined replay used one H100 CPU, 33,184 KiB maximum RSS and 2.09
seconds under a 1 GiB address-space cap.

### Branch A continuous point

```text
scratch/explore_k16_width45_c103_capacity_sep5_lp_20260730.py
  SHA-256 08bb455f295afc242944dd31e3d26f8fc8755f59628cf32283c9b438366c6668
scratch/branchA_capacity_sep5_lp.audit.json
  SHA-256 0449e356f803875e000454551f4d4aecd86142cf60754a48efd268760f484f84
scratch/exactify_r_k16_width45_c103_branchA_fractional_20260730.py
  SHA-256 dbeb78ee6383dc21b7272a63ac00526a729c204c1efcd00684fd5638f95faf56
scratch/branchA_exact_fractional_point.json
  SHA-256 1771bfb2a0a56c909571962b302eaf1068df75b6fb3223bfca03f9224196e9f2
scratch/branchA_exactification.audit.json
  SHA-256 99040c785f69ce93c7c91238eb794fcc42da6f4c55fc8dd2aba4ff29cd0ab828
  payload e5c9108da74c1bf656624c70a9c51a75695056769cbca1b80d278722b1c99730
scratch/branchA_exact_fractional_point.independent.audit.json
  SHA-256 a41765e946d7a2f53a639ef5e84ae57fae6774d39edea437fb79327d341a9c57
  payload 2cc4db378fadacc81f93d814282b3d247232c40e3e62e6d9ed123450cc0cfbc7
```

The LP used one H100 CPU and 104 seconds.  Exactification used 68,740 KiB
maximum RSS and 2.81 seconds.  Independent exact replay used a 768 MiB cap.

### Branch A complete binary catalogue

```text
scratch/export_r_k16_width45_branchA_cycle_graph_20260730.py
  SHA-256 a77a249a8ac802b386d8e56d0d5261333313494d00a36012227e58dc447140c1
scratch/export_r_k16_width45_branchB_cycle_graph_20260730.py
  SHA-256 6dc441fa07fde9e4ff06032f6b1c44ff42710d895e519126eea09a3ed79f66b6
scratch/branchA_complete_graph.bin
  SHA-256 25a4d4ed48386ad88f95e8a2a470018779ffc2a1e8c6f79327058cdee959d0aa
scratch/branchA_complete_graph.replay.stdout
  SHA-256 e58f5e7652fe97d5f21cbc81f7ffe01e67a45b650933ab242a607d8f6923990e
scratch/branchA_complete_graph.replay.resource
  SHA-256 8c9bc509d8fcbf16be51e3f72ac2cd75b4fe0a523edfc2331aa92d1736e7e96a
scratch/r_k16_width45_branchA_single_positive_cycle_pricer_20260730.cpp
  SHA-256 30ce082f166bfb7006b72a3457d22ca5a8332a5b94c3c01ed6ae5450addd28ca
scratch/r_k16_width45_safe_cycle_pricer_20260730.cpp
  SHA-256 3637dea27c2ed59720873f926ad6017822f6a1fd13079e051c0b0073eadf0b07
scratch/branchA_mixed_cycles_smoke.json
  SHA-256 87d84518310e34ab454f216c6eac9cd0caeac1470707d5657a5831188da9d860
scratch/solve_r_k16_width45_c103_restricted_cycle_column_master_20260730.py
  SHA-256 a3c1628f13873c3eb0b4b6cd1628cd55647c05fdcee6b198d6dad4b87e8a280e
scratch/branchA_complete385_master.audit.json
  SHA-256 1640abbc624dbd1fad2d405b8fe68c4a1859020063b7d8fb6e815482e3839784
  payload 76cf1cdac19dc73d38f552d231d295873232c196a0f42f8a04da987da442f9f1
scratch/audit_r_k16_width45_c103_branchA_complete_safe_cycles_20260730.py
  SHA-256 1fd4f4af5eef16725cc80f698f58a5514eae71cdc80a7479da5519ced60fb135
scratch/branchA_complete_safe_cycle_exhaustion.audit.json
  SHA-256 e3088a39a4157469c7287c531f5c9443a2236c6e68c89385e7c71311ce08b817
  payload ffaee2e6e50a0956525b64440aaad8bb346a1efccc4507656f6ea720cf7df777
```

The independent branch-A enumeration and exact-cover exhaustion used one
H100 CPU, 285,240 KiB maximum RSS and 10.46 seconds under a 1.9 GiB cap.
