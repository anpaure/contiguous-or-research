# K16: the provider-plus-port-balance service floor is 65

Date: 2026-07-30

Lane: H

Status: proved finite theorem in the authenticated full-C8
source-relative port catalogue.  This compact Hall certificate excludes
exact cut radii 56 through 64 before separation, reverse-edge, q1, or
protected q2/q3 survivor rows are used.  It does not by itself exclude
radius 65.  The separately archived provider-path theorem quantitatively
supersedes it, and the current exact distinct-path cover certificate gives
the stronger floor 70.

## 1. Input and verdict

The source is the full length-eight-orbit factor and its exact collar-safe
seam ledger

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204

scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

There are 93 source holes, namely 45 lower-q2 targets and 48 upper-q3
targets.  Among the 211,604 admissible nonold seams, 5,425 hit at least one
of these holes.  Call these seams **hitful** and write their set as \(H\);
write \(Z=E\setminus H\) for the zero-hit seams.

The provider-only theorem proves that every integral selection covering the
93 holes uses at least 56 hitful seams.  The present theorem adds the missing
tail/head closure cost.  The exact provider minimum, including its realizing
56-seam upper witness, is frozen in

```text
MATH_THEOREM_K16_DEFECT_PROVIDER_EDGE_COVER_FLOOR56_20260730.md
SHA-256 67e314781611225c54016b8b0cdd097f05b12bfe3816b6bdc41bc418561afc8c

scratch/k16_defect_provider_edge_cover_20260730.audit.json
SHA-256 7e0d51edfa2c933eea20808e43ea1445672cfe25e60f68afe3ed11e05c56ed27
```

### Theorem 1.1 (service plus port-balance floor)

Every integral tail/head-balanced port assignment in the authenticated seam
catalogue which covers all 93 source holes has at least

\[
                         \boxed{65}
\]

nonold seams.  Hence exact radii

\[
                         56,57,\ldots,64
\]

are infeasible already from defect service and balanced tail/head closure.

The proof uses none of the following rows:

* source-cut separation;
* physical reverse-edge exclusion;
* lower or upper q1 preservation;
* preservation of any previously covered q2 or q3 target;
* connectivity, voltage, or long-window chronology.

Thus this identifies the first layer killing every exact radius from 56
through 64, and it strictly strengthens the two previously frozen CP
exclusions at 56 and 57.

## 2. Port-balance cuts

Index source transitions by \(I=\{0,\ldots,12869\}\).  A nonold seam is a
directed port arc \(e=(i,j)\), from tail port \(i\) to freed head port \(j\).
For \(S\subseteq I\), put

\[
\begin{aligned}
 \delta^+(S)&=\{(i,j):i\in S,\ j\notin S\},\\
 \delta^-(S)&=\{(i,j):i\notin S,\ j\in S\}.
\end{aligned}
\]

Let \(x_e\in\{0,1\}\) be the selected-seam variables.  The tail and head
assignment equations imply, for every \(S\),

\[
                   x(\delta^+(S))=x(\delta^-(S)).       \tag{2.1}
\]

Indeed, sum the outgoing assignment equations over \(S\), subtract the
incoming equations over \(S\), and cancel internal seams.  Notice that this
is balance in the port graph, not in the physical Johnson graph.

## 3. The 18 forward-closed service sinks

The provider double-hit graph has the following 18 isolated targets:

\[
\begin{split}
&34069,35370,35461,37972,38154,41285,41633,43089,43176,\\
&43540,46811,49802,50498,53410,53584,54312,56173,60854.
\end{split}                                             \tag{3.1}
\]

For one of these targets \(t\), let \(P_t\subseteq H\) be its provider
seams.  Define \(S_t\subseteq I\) explicitly as follows:

1. put into \(S_t\) the head of every seam in \(P_t\);
2. repeatedly, if a hitful seam has its tail in \(S_t\), put its head into
   \(S_t\);
3. stop at the forward-reachability closure.

Thus \(S_t\) is canonical from the finite directed hitful graph.  Exact
ledger replay proves

\[
 P_t\subseteq\delta^-(S_t),\qquad
 H\cap\delta^+(S_t)=\varnothing.                       \tag{3.2}
\]

The first assertion includes the nontrivial fact that no provider tail lies
in its own target's full closure.  The second is immediate from closure but
is separately replayed against all 5,425 hitful seams.

Here is the complete compact census.  The audit JSON contains every member
of every \(S_t\); the hashes below are SHA-256 digests of the canonical
sorted integer lists.

| target \(t\) | providers | \(|S_t|\) | digest of \(S_t\) |
|---:|---:|---:|:---|
| 34069 | 17 | 32 | `541654effa4f59288cae23959b1aecd8c77e78e640f8fa5d0eb5bee604bfb14c` |
| 35370 | 22 | 36 | `2e63095a12bdf265c7fb2ad4fa92776f8165a7cb2b884cba05fb07840a443428` |
| 35461 | 22 | 36 | `cf57a850cc583fd3942d87cd0acdf8a886f1f7989716f153c41ad86d5c0406a2` |
| 37972 | 22 | 36 | `ddd8f72c2797d02f12f5066a9ad89308af2a1fa77b2acbbcf69b9c12d565873c` |
| 38154 | 22 | 36 | `88ae61293a94cf6d415be8e349f0ab3a343afd08bf9c4666de366090454df205` |
| 41285 | 22 | 36 | `35473126906133075472aaee47aa0fe0dae68f79497a42ef8a96a620808a8128` |
| 41633 | 22 | 36 | `97e7e506a6217896650bc9781485edf9bdb3274de56dd01e24504a3e4650a060` |
| 43089 | 22 | 36 | `8988621d65ec1873da0239c1ab61f89b9d46c120f85bb770af0c62984a056a8b` |
| 43176 | 22 | 36 | `ebbe83565f2bff751b90a07b9a632a5c8629f7b35dc83780c306d9dd66cc1822` |
| 43540 | 22 | 36 | `ec11a62837e88a982c3d4af3905460fce4d496846b7590e9ab81d084e5b22ef4` |
| 46811 | 60 | 115 | `4ab1ede15e6607c60d810756e58a14cca85facd07cc5792ae741ab8635f71982` |
| 49802 | 22 | 36 | `a71ba51f531f9f38fbe81eb3831c674d4aaf81ce22c133ac6e25f8928421d333` |
| 50498 | 22 | 36 | `efc89bb25e65d1bcd75de320da7306dd7fbaf801ba1cfc31b34ff66ffbf83262` |
| 53410 | 22 | 36 | `130c539d2749410011711dec503453bb0d298567a50638faeb4eb0a346394a51` |
| 53584 | 22 | 36 | `9796023d88c06bf7eaae0e65d9b37c91ad65f61ce97b7593315a09f25f206358` |
| 54312 | 22 | 36 | `ab918d66cecdda29d348365e6af11c757f140f82587cee02a266314080552db1` |
| 56173 | 60 | 115 | `6e25bd01d0cb8a5f09569b3ad3d8895c9aa4ac4ca60828ebe9c6d19c7cf33052` |
| 60854 | 60 | 115 | `1bf52ccfe3c7d857d5ec12a8012c34c566649b4c8519f884b307400148d192c8` |

The family digest, binding each target to its full sorted set, is

```text
b5487b2c4d358e3f398064298bfe846985124d3c3e2a6a177f5aa02affdcdfd6
```

## 4. Explicit Hall/Farkas inequality

Covering target \(t\) gives \(x(P_t)\ge1\).  From (3.2), nonnegativity and
port balance (2.1),

\[
 1\le x(P_t)
   \le x(\delta^-(S_t))
    =x(\delta^+(S_t))
    =x(Z\cap\delta^+(S_t)).                 \tag{4.1}
\]

This is already a small Hall cut: service entering a forward-closed hitful
sink requires a zero-service return arc.

For a seam \(e=(i,j)\), let

\[
 m_e=|\{t:i\in S_t,\ j\notin S_t\}|.        \tag{4.2}
\]

Exact replay gives the stronger vertex fact

\[
 |\{t:i\in S_t\}|\le2\quad(i\in I),         \tag{4.3}
\]

and hence \(m_e\le2\) for every seam.  The transition-membership histogram
is

```text
membership 0 : 12079 transition indices
membership 1 :   701 transition indices
membership 2 :    90 transition indices
```

Sum (4.1) over the 18 targets.  Using (4.2)--(4.3) gives

\[
 18\le\sum_{e\in Z}m_ex_e\le2\sum_{e\in Z}x_e,
\]

so

\[
                              x(Z)\ge9.       \tag{4.4}
\]

Equation (4.4) is a literal linear Farkas consequence of the 18 target rows,
the 18 free-signed port-balance equalities, nonnegativity and the verified
zero pattern \(H\cap\delta^+(S_t)=\varnothing\).  These become literal
Farkas rows in the strengthened Boolean service projection described below.

There is also a particularly small half-integral dual for the provider
part.  Give weight \(1\) to each of the 18 isolated targets and weight
\(1/2\) to each of the other 75 targets.  A provider seam has total target
weight at most one: a seam hitting an isolated target cannot hit a second
target, while any seam hitting two nonisolated targets has weight exactly
one.  The total dual weight is

\[
                 18+\frac{75}{2}=\frac{111}{2}.
\]

For a binary master assignment, occurrence coverage implies the Boolean
provider rows

\[
                  \sum_{e:\,t\text{ is hit by }e}x_e\ge1. \tag{4.5}
\]

Multiplying these 93 Boolean rows by the target weights and using the
per-seam bound gives the half-integral Hall inequality

\[
                         x(H)\ge\frac{111}{2}.             \tag{4.6}
\]

For integral seam choices this rounds to \(x(H)\ge56\), the provider-only
floor.  The stronger exact value 56 and a realizing provider cover were
proved independently by the matching certificate, but only the displayed
half-integral lower dual is needed here.

The Boolean qualification is essential.  A single seam may create two or
three occurrences of one residual mask, so (4.5) is not implied by the raw
fractional occurrence-multiplicity relaxation.  It is nevertheless a valid
logical row for every integral port assignment and can be inserted as a
strengthening before taking the displayed dual.  The same qualification
applies to the isolated-target service rows used in (4.1).  Thus the full
floor-65 proof is an integer Hall certificate whose port-balance part is
linear once these valid Boolean service rows are present; it is not claimed
as a dual of the unstrengthened occurrence LP.

Combining (4.4) and (4.6), every feasible point of the Boolean-service
strengthened relaxation satisfies

\[
                         x(E)=x(H)+x(Z)\ge\frac{129}{2}.
\]

Hence every integral complete repair satisfies

\[
 x(E)=x(H)+x(Z)\ge56+9=65,
\]

which proves Theorem 1.1.

## 5. Sharpness of the 18-sink relaxation

The coefficient-two bound in (4.4) is sharp.  The following nine zero-hit
seams leave all 18 sinks, exactly two apiece:

| seam | tail | head | sinks left |
|---:|---:|---:|:---|
| 145630 | 8281 | 5972 | 34069, 35461 |
| 116532 | 6537 | 4228 | 35370, 38154 |
| 94706 | 5229 | 4448 | 41285, 41633 |
| 152909 | 8717 | 3440 | 43089, 43176 |
| 87433 | 4793 | 4012 | 37972, 43540 |
| 199539 | 11954 | 2243 | 46811, 49802 |
| 72920 | 3925 | 1372 | 50498, 53584 |
| 116570 | 6541 | 1604 | 53410, 54312 |
| 81647 | 4455 | 3545 | 56173, 60854 |

This proves that the auxiliary problem "choose zero-hit arcs leaving all 18
sinks" has exact minimum nine.  It does **not** say that these nine seams,
together with any 56 providers, satisfy tail/head assignment, separation,
q1, survivor shadows or even mutual port compatibility.  Therefore the
certificate proves the lower bound 65 but makes no feasibility claim at 65.

## 6. Exact layer stratification

The exclusion chain is now:

1. provider coverage alone gives the integral floor 56;
2. balanced tail/head closure of the same service arcs forces nine additional
   zero-hit returns and raises the floor to 65;
3. separation, physical simplicity, q1 and q2/q3 survivor preservation have
   not yet entered.

In particular, the frozen exact-56 result had zero search branches because
the contradiction is already present in this small structural subsystem.
The same certificate gives a solver-free explanation of all five frozen
exact-band CP exclusions currently present:

| radius | audit SHA-256 | branches / conflicts |
|---:|:---|---:|
| 56 | `0d9afcf374fb3b7c4feb27632051a031dad2f2bacd1f1940f0b2304ffeb27b57` | 0 / 0 |
| 57 | `d522b0982270e18702eac86a526c41c742085deb9545781dbe14998077cc266f` | 258245 / 118 |
| 58 | `c59a661fa01534b5a62207bf1bc5bbbf578c8e8df6f9b0eb7750b280fb06f5ec` | 241638 / 77 |
| 59 | `e87d6d0a24f988c71bec91119cd25fd888ab0348f8f65cf00761d134d5fb1066` | 283408 / 25 |
| 60 | `3f4477e8492aca6030ddbd36a975e4a11511929b924cd11f83d0c6fae65ec806` | 281173 / 4 |

All five use frozen q<=3 master SHA-256
`4a420e88ac965b4fdb77123c2035078ef07bbcc2f5a611ff81c071232b3ea246`.
The theorem also excludes radii 61 through 64 without a separate band
solve.

The 18-sink certificate itself stops at radius 65 because its return-cover
relaxation attains nine.  Radius 65 is nevertheless not open in the project.
The provider-condensation analysis first proved the archived floor 66; its
current exact distinct-mask refinement proves more.  Among the 48 defects
outside the provider cyclic core, one provider path services at most four
distinct targets.  The 2,192 achievable path masks cannot cover those 48
targets with even thirteen paths.  Hence at least fourteen zero-hit return
seams are required, giving the stronger total floor \(56+14=70\).

Frozen evidence for the historical floor 66 and current floor 70 is

```text
MATH_THEOREM_K16_PROVIDER_PATH_CAPACITY_FLOOR66_20260730.md
SHA-256 08b21042d785e64d766bf1a03b85a0112b0d2875695658a05900cd2d65bdbcc8

scratch/k16_defect_service_structure_floor66_20260730.audit.json
SHA-256 31314bc077f81fc311b58d3aba483a0a06a77d2d05a4d4d424db606db3e0c4c8

scratch/k16_defect_service_structure_floor70_20260730.audit.json
SHA-256 972d63ce65be989af7b44cacfe6cae8de65c2b68179250b51d9105bb9c82fd27

scratch/audit_k16_defect_service_structure_20260730.py
SHA-256 e37e78140b8ba38fb59bfd81607750a30d26ab03cd9460d0c769576d6055e8be
```

Consequently exact radii 65 through 69 die at the same first layer--defect
service plus balanced tail/head closure--but their proof uses the larger
condensation path-mask certificate rather than the compact 18-sink Farkas
certificate in this note.  Separation, reverse-edge, q1 and survivor rows
remain unused throughout the full floor-70 chain.

Thus the present note should be used as the smaller explicit Farkas/Hall
certificate, not as the quantitative frontier.

## 7. Reproducible audit

```text
scratch/audit_k16_service_port_balance_floor65_20260730.py
SHA-256 7d489832607605c68c083e6f01b946a20e043aa91dd6523f9726946b49662496

scratch/k16_service_port_balance_floor65_20260730.audit.json
SHA-256 57868f47e7075d5644c2cd8f44b9ce1db4e51dfdc6fed4cc7c7119d85a8fd9bc
payload SHA-256 c43b05118027ec4b521fcead8fd753afd2f82d92f38d7f7d2572963e95f77217

imported binary-ledger parser
  scratch/audit_k16_seam_ledger_permutation_20260730.py
  SHA-256 c88f13823c0c57a1934b5fcc541301fa13476bf2ca48b3fc614ed13087604ff2
```

The checker is dependency-free apart from importing the already frozen
binary-ledger parser.  It parses all 211,604 seams, reconstructs all 18
closures, checks every provider direction and every hitful outgoing arc,
verifies the transition-membership bound two, and replays the nine zero-hit
return seams.  Its local audit run took 1.6 seconds; it ran no SAT, CP, LP,
exhaustive search or remote job.
