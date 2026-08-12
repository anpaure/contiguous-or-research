# Structure of the verified `R=6` and `R=7` triangular certificates

## 1. Outcome

The length-38 `R=7` certificate is not an isolated search artefact.  It
contains an exact `S=6` completion-core structure, and its multiset is an
almost exact fold lift of the certified `V_5` core from
`LINEAR_TRIANGULAR_FOLD_BRAID.md`.

The main facts are:

1. The `R=6` word is the core completion of the length-15 edge-balanced
   core `V_5`; its excess is five.
2. From the `R=7` word one can extract a length-24 `7`-completion core
   `C_6` with one top-row hole `E_(6,3)` and core excess nine.
3. As a multiset,
   
   \[
   C_6=\iota_5(V_5)\uplus
      \{E_{2,1},E_{3,1},E_{4,1},E_{5,1},E_{6,1},P_0\}
      \uplus\{P_1,P_4,P_5\}.                    \tag{1.1}
   \]
   
   The first two terms are exactly the order-free lift from
   `EDGE_BALANCED_CORE_RECURSION.md`.  Thus the only excess over the
   conjectural edge-balanced lift is **three extra star portals**.
4. The actual `R=7` word therefore supports the exact multiset recursion and
   a linear-overhead braid.  It neither proves nor contradicts the sharper
   conjecture `rho(R)<=R-1`: at `R=7` it gives excess nine, while that
   conjecture asks for excess six.
5. There is a precise candidate three-occurrence reduction.  Delete one
   extra copy each of `E_(3,2)`, `P_4`, and `P_5`, and rebraid the remaining
   multiset.  The resulting length-21 multiset has exactly the edge-balanced
   ledger and passes the known multiplicity and star-cover obstructions.
   Deletion without reordering does not work.

All finite checks used here are exhaustive interval enumeration on words of
length at most 24, cell counting, and eight prescribed deletion tests.  No
long search was run.

## 2. Conventions

Write

\[
P_s=E_{s,0}=(s,0),\qquad
D_x=E_{x+1,x}=(x+1,x).
\]

The triangle has

\[
|\mathcal T_R|=1+\frac{R(R+1)}2.                    \tag{2.1}
\]

An `(S+1)`-completion core lives on rows at most `S`, ends in `P_0`, covers
all strict-positive targets, has a perfect suffix fan through height `S-1`,
and contains every nonpeak except its stated top-row holes.  For one hole,
its compulsory baseline is

\[
\binom S2-1+1=\binom S2,                            \tag{2.2}
\]

so a core of length `n` has

\[
\kappa=n-\binom S2.                                 \tag{2.3}
\]

## 3. Exact `R=6` ledger

The first 15 letters of `scratch/triangular_r6_plus5.txt` are

```text
V5 =
E54 E53 E42 E51 P4 E31 E21 P1
E43 E41 E32 P3 E21 P1 P0.
```

They form the certified `6`-completion core with hole

\[
H_5=\{E_{5,2}\}.                                    \tag{3.1}
\]

Its exact occurrence ledger is:

* every required nonpeak occurs once, except `E_(2,1)`, which occurs twice;
* the nonzero peaks are `P_1^2,P_3,P_4`;
* `P_0` occurs once;
* `|V_5|=15` and \(\kappa=15-\binom{5}{2}=5\).

The perfect suffix fan is:

| height `x` | zero-based suffix start | first letter |
|---:|---:|---|
| 1 | 12 | `E_(2,1)` |
| 2 | 10 | `E_(3,2)` |
| 3 | 8 | `E_(4,3)` |
| 4 | 0 | `E_(5,4)` |

There are four peak runs and seven physical peak/nonpeak portals in the
core.  Assigning every one of the 30 strict-positive targets to the first
portal in a shortest witness gives the following exact check ledger:

| boundary | adjacent letters | assigned strict targets |
|---:|---|---:|
| 3 | `E51 | P4` | 16 |
| 4 | `P4 | E31` | 3 |
| 6 | `E21 | P1` | 2 |
| 7 | `P1 | E43` | 1 |
| 10 | `E32 | P3` | 7 |
| 11 | `P3 | E21` | 1 |
| 12 | `E21 | P1` | 0 |

The counts sum to 30.  This assignment is only a convenient certificate;
portal capacity is not uniquely determined by shortest witnesses.

Appending the peak spine and the sixth-row arm, with the hole parked after
height three, gives the 27-letter word.  Since `|T_6|=22`, its excess is
five.  Its only repeated cell types are

\[
P_1^3,\quad P_3^2,\quad P_4^2,\quad E_{2,1}^2.       \tag{3.2}
\]

## 4. An exact completion core inside the `R=7` certificate

Number the 38 letters of `scratch/triangular_r7_plus9.txt` from zero.  Define

```text
G = w[0..4]
  = P2 D2 E52 P5 E41
```

and

```text
Q = reverse(w[18..36])
  = E42 P1 P2 E31 P4 P5 E61 E62 E53 E64
    E65 E54 E51 E43 P4 D2 E21 P1 P0.
```

Then put

```text
C6 = G || Q
   = P2 D2 E52 P5 E41
     E42 P1 P2 E31 P4 P5 E61 E62 E53 E64
     E65 E54 E51 E43 P4 D2 E21 P1 P0.
```

This is a genuine `7`-completion core.

### 4.1 Exact defect decomposition

The 19-letter word `Q` covers 50 of the 55 strict-positive targets on
`T_6`.  Its missing set is exactly

\[
\begin{split}
&(2,3,2),\quad(2,5,2),\quad(3,5,2),\\
&(4,5,1),\quad(4,5,2).                              \tag{4.1}
\end{split}
\]

The five-letter word `G` covers exactly these five targets, using

| target | interval in `G` |
|---|---|
| `(2,3,2)` | `[0,1] = P2,D2` |
| `(2,5,2)` | `[0,2] = P2,D2,E52` |
| `(3,5,2)` | `[1,3] = D2,E52,P5` |
| `(4,5,1)` | `[3,4] = P5,E41` |
| `(4,5,2)` | `[2,4] = E52,P5,E41` |

Consequently `C_6=G||Q` covers all 55 strict-positive targets.  This is an
exact five-target defect gadget, not a visual resemblance.

### 4.2 Inventory and fan

The core contains every nonpeak of `T_6` except

\[
H_6=\{E_{6,3}\}.                                    \tag{4.2}
\]

Its multiplicities are:

* `E_(3,2)` occurs twice and every other present nonpeak once;
* its nonzero peak multiset is
  
  \[
  P_1^2P_2^2P_4^2P_5^2;                             \tag{4.3}
  \]
* `P_0` occurs once.

The nested perfect suffix fan is especially clean:

| height `x` | zero-based suffix start | first letter |
|---:|---:|---|
| 1 | 21 | `E_(2,1)` |
| 2 | 20 | `E_(3,2)` |
| 3 | 18 | `E_(4,3)` |
| 4 | 16 | `E_(5,4)` |
| 5 | 15 | `E_(6,5)` |

Thus

\[
|C_6|=24,\qquad \kappa(C_6,H_6)=24-\binom62=9.       \tag{4.4}
\]

The core-completion theorem therefore produces a universal `R=7` word of
length

\[
|\mathcal T_7|+9=29+9=38.                           \tag{4.5}
\]

This gives a short mathematical certificate for the length of the supplied
word even though the theorem's canonical ordering is not the supplied
ordering.

### 4.3 Portal ledger

`C_6` has six peak runs and ten physical portals.  The same shortest-witness
assignment as above gives:

| boundary | adjacent letters | assigned strict targets |
|---:|---|---:|
| 0 | `P2 | D2` | 2 |
| 2 | `E52 | P5` | 2 |
| 3 | `P5 | E41` | 2 |
| 5 | `E42 | P1` | 2 |
| 7 | `P2 | E31` | 13 |
| 8 | `E31 | P4` | 6 |
| 10 | `P5 | E61` | 9 |
| 18 | `E43 | P4` | 15 |
| 19 | `P4 | D2` | 2 |
| 21 | `E21 | P1` | 2 |

The counts sum to all 55 strict-positive targets.  The growth from seven to
ten portals from `V_5` to `C_6` is linear and is exactly accounted for by
the three added star occurrences in (1.1).

## 5. How the supplied 38-letter order uses the same structure

The supplied word has the exact full-word multiplicity ledger

\[
P_1^3,P_2^3,P_4^3,P_5^3,E_{3,2}^2,                 \tag{5.1}
\]

with every other cell once.  It has six peak runs and eleven physical
portals.

Its ordering can be read as follows.

* `G` is placed first and repairs the five strict targets in (4.1).
* Positions 5 through 18 are a descending seventh-row arm followed by the
  peak spine.  At height three, `E_(6,3)` replaces `A_3=E_(7,3)` as the
  height provider:
  
  ```text
  A6 A5 A4 E63 A2 A1 P7 P6 ... P0.
  ```
  
  This still represents every target `[u,7] x [0,3]`, because `u<=6` and
  `E_(6,3)` stays inside every such box.  The displaced `A_3` is placed at
  the final position.  This is an exact **hole--arm swap**.
* Starting at `P_0` in position 18, the right side contains the nested
  prefix fan with endpoints `E21,D2,E43,E54,E65`.  Extending left through
  the descending peak spine gives every `u=0` target through height five.

Thus the original ordering is an alternative braid of the same core
multiset: it uses the old hole as one arm provider and parks the displaced
new arm cell, instead of literally applying the safe-parking order in the
core-completion theorem.

## 6. Exact relation to the fold lift

Apply the low-fold map `iota_5` to `V_5`.  The old hole

\[
E_{5,2}\longmapsto E_{6,3}                           \tag{6.1}
\]

becomes exactly the hole of `C_6`.  Insert the compulsory first-column
edges

\[
E_{2,1},E_{3,1},E_{4,1},E_{5,1},E_{6,1}             \tag{6.2}
\]

and the new terminal loop `P_0`.  These 21 letters are the exact
edge-balanced order-free lift.  The actual core has only

\[
P_1,P_4,P_5                                          \tag{6.3}
\]

in addition.  This proves (1.1).

The exact multiplicity comparison is:

| multiset | repeated nonpeak | nonzero star occurrences | `kappa` | status |
|---|---|---|---:|---|
| `V_5` | extra `E21` | `P1^2 P3 P4` | 5 | ordered core |
| naive lifted 21-set | extra `E32` | `P1 P2^2 P4 P5` | 6 | cannot be a core by Theorem 3 |
| reset 21-set below | none | `P1^2 P2^2 P4 P5` | 6 | passes known necessary tests |
| actual `C_6` | extra `E32` | `P1^2 P2^2 P4^2 P5^2` | 9 | ordered core |

The naive lifted multiset has only one `P_1` and only one `E_(2,1)`, so the
low-portal duplication theorem proves that no ordering of that exact
multiset can work.  This pinpoints why a multiplicity reset is necessary.

## 7. Concrete three-occurrence reduction target

Starting with the valid `C_6`, remove

\[
\text{one }E_{3,2},\qquad
\text{one }P_4,\qquad
\text{one }P_5.                                     \tag{7.1}
\]

The remaining multiset `M_6^*` has length 21 and consists of:

* every nonpeak exactly once except the top-row hole `E_(6,3)`;
* one loop `P_0`;
* star multiset
  
  \[
  P_1^2P_2^2P_4P_5.                                 \tag{7.2}
  \]

Hence `kappa=6`, exactly the edge-balanced `R-1` target.  It passes the two
known multiplicity obstructions:

1. `P_1` is duplicated, so the nested-barrier theorem does not force a
   ladder of repeated diagonals.
2. Its star support `{1,2,4,5}` is a vertex cover of
   `1-2-3-4-5-6`.

There is also a concrete compatible local skeleton.  The four defect targets
not equal to `(2,3,2)` can be supplied by

```text
P2 E52 P5 E41 E31,
```

while the remaining defect target and the bottom of the suffix fan can use

```text
P2 E32 E21 P1 P0.
```

The higher suffix starts can be nested in the order

```text
E65 ... E54 ... [first defect block] ... E43 ...
    [second defect block ending E32 E21 P1 P0].
```

Every letter in the first defect block lies inside the height-four suffix
box, and every letter after `E43` lies inside the height-three suffix box.
Thus the desired defect witnesses and perfect fan are locally compatible.
The unresolved issue is preservation of all other transported strict
targets—the same corridor-continuity problem isolated in the edge-braid
note.

Pure deletion is insufficient.  There are two choices for which `E32`, two
for which `P4`, and two for which `P5` to delete.  Exhaustive checking of all
eight order-preserving deletions leaves between 11 and 23 strict-positive
targets uncovered.  Therefore any successful reduction must genuinely
reorder or switch intervals; it cannot merely prune the certificate.

Two individual nonpeak deletions (`E52` or `E42`) happen to preserve strict
coverage, but they create off-top holes.  The safe-parking theorem does not
absorb those holes for free, so they do not reduce the completed word's
length.

## 8. A concrete lift target if exact reduction is too rigid

The valid `C_6` also suggests a slightly weaker but still linear recursive
family.  Apply the order-free lift to `C_6`, insert the six new first-column
edges and a new loop.  The resulting `S=7` multiset has

\[
24+6+1=31,\qquad \kappa=31-\binom72=10=7+3.          \tag{8.1}
\]

Its shifted hole is `E_(7,4)`.  Its sole repeated nonpeak is the shifted
extra `E_(4,3)`, and `P_1` is again unique.  Perform the length-preserving
reset

\[
E_{4,3}^{\rm extra}\longrightarrow P_1^{\rm extra}. \tag{8.2}
\]

The reset multiset has every required nonpeak once, a duplicated `P_1`, and
the same `kappa=10`.  If the edge-braid ordering can be made recursively,
this gives the invariant

\[
\kappa(V_S)=S+3                                      \tag{8.3}
\]

from the present `S=6` base—already enough for a fully explicit linear
triangular overhead.

If the sharper 21-letter `M_6^*` can first be ordered, its lift has length
28 and `kappa=7`.  After lifting, one may redirect one of the duplicated
shifted star occurrences to a second `P_1`; the resulting portal support
still covers the path of star labels.  This is the exact edge-balanced lift
route.

In both routes the remaining theorem is an **ordering theorem**, not a
counting theorem: reconcile the height-one corridor with the inherited
Ferrers witnesses and nested suffix shells.

## 9. Conclusion

The `R=7` certificate gives positive evidence for the fold-braid program in
the following precise sense:

\[
\boxed{
\text{valid lifted core}
=\text{exact order-free lift}+3\text{ star portals}.}
\]

It does not establish the edge-balanced `R-1` conjecture, and its excess
nine is not evidence that six is impossible.  The clean next mathematical
target is the 21-letter reset multiset `M_6^*`.  Either ordering it as a
completion core would prove `rho(7)<=6`, or a genuine ordering obstruction
for that multiset would identify which additional portal type an all-rank
recursion must carry.
