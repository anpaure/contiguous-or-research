# Reflected natural-shadow statistics do not descend to the compiler

Date: 2026-08-01  
Status: exact theorem and replay on the authoritative `k=11,13,15` optima.
This removes the reflected pair-degree law of the unplanted common-order
packet as a direct compiler obstruction.  The authoritative planted
adjacent-order catalogue can also change that statistic, so no general
safe-carrier-fibre invariant is claimed.

## 0. Outcome

For a fixed depth-`d` carrier `T`, define the natural-deck statistic

\[
 I_{q,x,y}(T)=D_q(x,y;T)-D_{d+2-q}(x,y;T)
\]

It is, tautologically, fixed while `T` is fixed, and it is invariant under
the restricted unplanted common-order coatom moves.  It is **not** invariant
under all authenticated planted safe moves: label-attached adjacent
coatom-order twists change it.  The terminal compiler in any case does not
have to use those natural intersections as its lower targets.  It chooses
arbitrary subsets inside physical erosion caps, subject to one common-`Q`
compatibility condition.

That distinction is decisive, not semantic.

* The exact `k=11` carrier has one natural depth-two hole and no natural
  depth-three hole, while its terminal compiler has `lambda_3(T)=0`.
* The missing depth-two target is supplied at a boundary cell as a proper
  rank-two subset of its rank-six cap.
* Keeping this same carrier fixed, one may change the reflected pair-degree
  signature of the compiler rows while every natural deck and every
  `I_{q,x,y}` remains literally unchanged.
* The same fixed-carrier freedom is large: the retained exact antecedents at
  `k=11,13,15` lie below Boolean intervals of respectively `2^89`, `2^1128`,
  and `2^2657` depth-three antecedents of the identical carrier.

Consequently, nonzero or nonconstant reflected pair statistics do not imply
positive `lambda_d`, and natural-shadow holes need not be compiler holes.
Moreover the planted adjacent-order breaker basis shows that reflection
does not partition the full safe-move graph.  The correct remaining question
is direct: does the reachable component contain one chronology with a
sufficiently expanding cap/subset linkage graph?

## 1. Natural decks and compiler rows are different objects

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be a factor-resident rank-`r` carrier.  Its maximal depth-`d` erosion is

\[
 P_j=\bigcap_{\max(0,j-d)\le i\le\min(j,W-1)}T_i,
 \qquad 0\le j<W+d.                                      \tag{1.1}
\]

The natural depth-`q` deck consists of

\[
 N_{q,i}=T_i\cap\cdots\cap T_{i+q}.                       \tag{1.2}
\]

The reflected pair statistic is computed from the occurrence multiplicities
of (1.2).

By contrast, a compiler antecedent is a nonzero word

\[
 A=(A_0,\ldots,A_{W+d-1}),\qquad D^dA=T,                  \tag{1.3}
\]

and its short cells are

\[
 C_{h,j}(A)=A_j\cup\cdots\cup A_{j+h},qquad 0\le h<d.   \tag{1.4}
\]

Every such cell lies inside the maximal cap

\[
 \widehat P_{h,j}=P_j\cup\cdots\cup P_{j+h},             \tag{1.5}
\]

but it need not equal the cap or any member of (1.2).  Equality is precisely
the assumption which would incorrectly transfer the natural reflection law
to the compiler.

There is also an exact address-count discrepancy.

### Lemma 1.1 (interior natural caps plus `2q` boundary caps)

Fix `1<=q<=d` and put `h=d-q`.  The compiler row `D^hA` has

\[
                              W+q                              \tag{1.6}
\]

physical cells.  They split canonically into

* `W-q` interior cells, indexed by `q<=s<=W-1`, whose maximal caps are

  \[
      \widehat P_{h,s}=T_{s-q}\cap\cdots\cap T_s;             \tag{1.7}
  \]

* `q` left-boundary cells; and
* `q` right-boundary cells.

Thus the natural depth-`q` deck accounts for only the interior addresses.
The physical compiler has exactly `2q` additional clipped boundary caps.

#### Proof

The number of starts in row `h` is

\[
 (W+d)-h=W+q.
\]

For `q<=s<=W-1`, the carrier windows containing the whole physical cell
`[s,s+h]` are exactly `T_{s-q},...,T_s`, giving the inclusion
`widehat P_{h,s}` in the right side of (1.7).  Conversely, if a coordinate
lies in all these owners, their segment lies in one coordinate run.  Factor
residence extends that segment to a carrier interval of length `d+1` (with
the standard clipping at the two global boundaries).  The endpoint of such
an interval may be chosen in `[s,s+d-q]`, so that coordinate belongs to one
of `P_s,...,P_{s+h}`.  This proves the reverse inclusion.  The omitted starts
are precisely `0,...,q-1` and `W,...,W+q-1`.  \(\square\)

The lemma gives two independent ways to bypass a natural-shadow constraint:
choose a proper subset of an interior natural cap, or use one of the `2q`
boundary caps which the natural deck does not count at all.

## 2. A Boolean interval of antecedents inside one carrier fibre

Before using compiler freedom, it is useful to identify exactly what the
natural statistic measures.  For a coordinate pair `{x,y}`, let
`ell_1,ell_2,...` be the lengths of the maximal runs on which both
coordinates belong to `T_i`.  Direct window counting gives

\[
 D_q(x,y;T)=\sum_j(\ell_j-q)_+.                              \tag{2.0}
\]

Hence

\[
 I_{q,x,y}(T)=
 \sum_j\big((\ell_j-q)_+-(\ell_j-(d+2-q))_+\big).           \tag{2.0a}
\]

For `d=3`, this specializes to

\[
 I_{2,x,y}(T)=\#\{\text{pair-cooccurrence runs of length at least 3}\}.
                                                                    \tag{2.0b}
\]

Thus it is a clipped pair-residence statistic of the carrier.
It is not a count of lower targets already installed by the compiler.

### Theorem 2.1 (fixed-carrier Boolean interval)

Suppose `A` is any antecedent of `T`, and `P` is (1.1).  If a word `A'`
satisfies

\[
                         A_j\subseteq A'_j\subseteq P_j
                         \quad\text{for every }j,              \tag{2.1}
\]

then

\[
                              D^dA'=T.                          \tag{2.2}
\]

In particular, every subset of the missing envelope incidences

\[
                  \{(j,x):x\in P_j\setminus A_j\}             \tag{2.3}
\]

may be restored independently without changing the carrier.

#### Proof

Adjacent union, and hence `D^d`, is coordinatewise monotone.  Therefore

\[
                    D^dA\subseteq D^dA'\subseteq D^dP.
\]

The left member is `T` by hypothesis.  Factor residence gives `D^dP=T` for
the maximal erosion.  Both inclusions are therefore equalities.  \(\square\)

### Corollary 2.2 (no inherited compiler reflection law)

Every carrier statistic—including all natural decks and all reflected
pair-degree statistics—is constant on the Boolean interval of Theorem 2.1.
The short compiler rows `D^hA'`, `h<d`, need not be constant on it.

Thus there is no identity which obtains a reflected pair law for compiler
cells merely by replacing natural intersections with short-cell unions.

This is stronger than saying that the compiler has “extra slack.”  It gives
many compiler words with exactly the same physical carrier and exactly the
same value of every fixed-carrier statistic.

## 3. Exact replay on the three retained depth-three optima

The audit uses only

```text
answers/k11.word
answers/k13.word
answers/k15.word
```

and independently reconstructs `T=D^3A`, the maximal erosion, all natural
intersection decks, and one injective literal compiler assignment.  The
assignment selects the first actual occurrence in `A,DA,D^2A` of every
lower target.

### 3.1 Natural decks and reflected pair invariants

For `d=3`, the only nontrivial reflected pair is `q=2 <-> q=3`.  Let

\[
 I_{xy}=D_2(x,y;T)-D_3(x,y;T).                              \tag{3.1}
\]

| `k` | natural holes `(q1,q2,q3)` | histogram of `I_xy` | pairs differing from the complete-simple-layer baseline |
|---:|:---:|:---|---:|
| 11 | `(1,1,0)` | `22^11 24^2 25^10 26^21 27^11` | 44/55 |
| 13 | `(1,0,0)` | values `81..93`, twelve occupied values | 78/78 |
| 15 | `(2,0,0)` | values `292..332`, fifteen occupied values | 105/105 |

All three carriers nevertheless have `lambda_3(T)=0`, witnessed by their
literal optimal words.  In particular, neither vanishing nor constancy of
the reflected invariant is necessary for a perfect compiler.

There is an exact algebraic contrast.  Once a compiler chooses one witness
for every target at ranks `r-2` and `r-3`, the selected **target labels** have
pair-degree difference

\[
 \binom{k-2}{r-4}-\binom{k-2}{r-5}                         \tag{3.2}
\]

for every pair, simply because each complete rank layer is used once.  The
values of (3.2) are `27,110,429` for `k=11,13,15`.  Yet the corresponding
natural occurrence vectors have the nonconstant histograms in the table.
Thus the actual zero-deletion compiler converts a nonuniform natural pair
profile into the uniform complete-layer profile by selecting proper subsets
of physical caps.  The reflected natural vector is not conserved even at
the level of the selected target labels.

### 3.2 Cap/subset use in the actual compilers

| `k` | lower targets assigned | exact-cap targets | proper-subset targets | missing envelope incidences |
|---:|---:|---:|---:|---:|
| 11 | 1023 | 953 | 70 | 89 |
| 13 | 4095 | 3611 | 484 | 1128 |
| 15 | 16383 | 14440 | 1943 | 2657 |

Thus cap/subset use is not confined to the seam.  It occurs hundreds or
thousands of times in the actual zero-deletion compilers.

The natural holes are paid as follows.

| `k` | natural hole | literal compiler witness | maximal cap | cap gap |
|---:|---:|:---|---:|---:|
| 11 | `q1:155` | `D^2A[0]` and `D^2A[462]` | `219` and `159`, rank 6 | 1 |
| 11 | `q2:154` | `DA[463]` | `159`, rank 6 | 2 |
| 13 | `q1:2135` | `A[1718]` | `2167`, rank 7 | 1 |
| 15 | `q1:18553` | `A[0]` | `26745`, rank 8 | 1 |
| 15 | `q1:18033` | `A[6437]` | `20081`, rank 8 | 1 |

The `k=11` line is the sharp counterexample: the reflected natural decks
have hole counts `(1,0)` at depths `(2,3)`, yet the compiler deletion number
is zero.  The target `154` is not restored as a natural depth-two
intersection; it is carved as a proper subset of a boundary cap.

### 3.3 The compiler pair signature changes with the carrier fixed

Define the analogous short-row signature

\[
 \widehat I_{xy}(A)
  =\sum_j\mathbf1_{\{x,y\}\subseteq (DA)_j}
   -\sum_j\mathbf1_{\{x,y\}\subseteq A_j}.                  \tag{3.3}
\]

The following single envelope-bit restorations preserve `D^3A=T` but change
(3.3):

```text
k=11: position 0, coordinate 1, 137 -> 139; one pair changes 26 -> 27.
k=13: position 1, coordinate 0, 320 -> 321; five pair entries change.
k=15: position 0, coordinate 13, 18553 -> 26745; seven pair entries change.
```

Every one of the 89 admissible single additions at `k=11` changes (3.3), as
do 1125/1128 at `k=13` and 2657/2657 at `k=15`.  Meanwhile (3.1) is
unchanged because `T` is unchanged.

### Theorem 3.1 (reflection is not a direct `lambda` obstruction)

There exists a flat factor-resident upper-complete carrier with

1. nonconstant reflected pair invariant;
2. unequal natural hole counts at reflected depths; and
3. terminal compiler deletion number zero.

Moreover, within that fixed carrier, the corresponding compiler-row pair
signature is not invariant.

#### Proof

Take the audited `k=11` carrier.  Sections 3.1--3.3 verify the three claims
and give explicit witnesses.  The fixed-carrier statement follows from
Theorem 2.1 and the displayed `137 -> 139` restoration.  \(\square\)

This theorem refutes only a **direct** obstruction.  It remains possible
that some other reflected fibre contains no low-`lambda` carrier reachable
from the recursive seed.

## 4. A sufficient linkage bound inside any reflected fibre

Here “fibre” means only a level set of the displayed natural statistic with
the carrier held fixed during compilation.  It is not asserted to be a
connected component of the full planted safe-move graph.

There is a clean way to formulate the positive target without breaking the
reflection invariant.

Fix any carrier `T` in any reflected fibre, a nonzero antecedent `C` with
`D^dC=T`, and a protected lower-pin family `F_0` with chosen witnesses
`I_X`.  Let

\[
                       R=\mathcal L\setminus F_0.
\]

For `S in R`, put an edge `S~p` when

\[
 C_p\subseteq S\subseteq P_p                                      \tag{4.1}
\]

and, for every protected witness containing `p`,

\[
                         p\in I_X\Longrightarrow S\subseteq X.    \tag{4.2}
\]

Call this the **transparent cap-linkage graph** `G(C,F_0)`.

This is the fixed-fibre reading of the repository's robust-core Hall
augmentation theorem; it is restated here because it answers exactly what
kind of linkage can bypass the reflected natural-shadow law.

### Theorem 4.1 (fibre-relative cap-linkage bound)

If `G(C,F_0)` has a matching saturating all but `c` targets of `R`, then

\[
                              \lambda_d(T)\le c.                  \tag{4.3}
\]

Equivalently,

\[
 \lambda_d(T)\le
 \max_{X\subseteq R}\bigl(|X|-|N_{G(C,F_0)}(X)|\bigr)_+.        \tag{4.4}
\]

Relative to any current matching `M`, it is enough that the graph contain
enough vertex-disjoint `M`-augmenting paths to leave at most `c` unmatched
target vertices.

#### Proof

For every matched edge `S~p`, replace `C_p` by `S`; matched positions are
distinct.  The right inclusion in (4.1) preserves every central window, and
the left inclusion means no old central coordinate is removed.  Condition
(4.2) inserts no forbidden coordinate into a protected lower witness, while
all its old positive witnesses survive because letters only grow.  The new
singleton letter at `p` realizes `S`.  Hence all of `F_0` and all matched
members of `R` are realized by one antecedent of `T`.  Hall deficiency gives
(4.4), and Berge's theorem gives the augmenting-path formulation.  \(\square\)

The theorem is deliberately fibre-relative: it never changes `T`, so it
automatically respects every reflected pair invariant.  It also identifies
the only kind of obstruction relevant to this monotone sub-atlas: a genuine
Hall cut in physical cap addresses, not a pair-degree imbalance of natural
shadows.

The full common-`Q` compiler is more flexible than this one-cell monotone
sub-atlas, so a large deficiency in (4.4) would not by itself lower-bound
`lambda_d(T)`.  Conversely, a bounded deficiency proves the desired bound
immediately.

### Proposition 4.2 (the genuine cap-capacity obstruction)

For a coordinate set `Q`, let

\[
 L_Q=\sum_{s=|Q|}^{r-1}\binom{k-|Q|}{s-|Q|}                 \tag{4.5}
\]

be the number of lower targets containing `Q`, and let

\[
 C_Q(T)=\#\{(h,j):0\le h<d,\ Q\subseteq\widehat P_{h,j}\}  \tag{4.6}
\]

be the number of physical short-cell caps which can possibly carry such a
target.  Then

\[
 \boxed{\lambda_d(T)\ge
        \max_Q\bigl(L_Q-C_Q(T)\bigr)_+.}                    \tag{4.7}
\]

#### Proof

If a compiler omits `c` lower targets, it realizes at least `L_Q-c` distinct
targets containing `Q`.  Their chosen witness intervals are distinct, and
the maximal cap of each must contain `Q`.  Hence
`L_Q-c<=C_Q(T)`.  Rearranging and maximizing over `Q` gives (4.7).
\(\square\)

This is a genuine fibre-level obstruction, unlike the natural reflected
pair vector.  At `|Q|=2`, however, it is very far from binding on the exact
zero-deletion carriers:

| `k` | pair-target demand `L_Q` | minimum pair-cap slack | maximum pair-cap slack |
|---:|---:|---:|---:|
| 11 | 130 | 27 | 40 |
| 13 | 562 | 113 | 136 |
| 15 | 2380 | 386 | 479 |

So the known `lambda=0` fibres do not merely evade the reflected invariant
at a boundary anomaly; every coordinate pair has substantial aggregate cap
room.  Any negative fibre theorem must find a higher-order/common-`Q` Hall
cut, not a pair-capacity deficit.

The complete capacity hierarchy makes the location of tightness explicit:

```text
minimum C_Q-L_Q by |Q|
k=11: 118,  27,  2, 0, 0
k=13: 394, 113, 19, 1, 0, 0
k=15:1246, 386, 90,12, 0, 0, 0
```

Low-order cuts, including every pair cut, have growing room.  Tight caps
first occur only near the top of the lower ideal.  Those high-order tight
addresses are exactly where occurrence-labelled common-`Q` correlation can
matter; they are invisible to the reflected pair-degree invariant.

### Lemma 4.3 (reflection fixes the difference mode, not capacity)

Let `B_{q,Q}(T)` count the `2q` boundary caps in the depth-`q` row which
contain `Q`, and let

\[
 D_q(Q;T)=\#\{i:Q\subseteq T_i\cap\cdots\cap T_{i+q}\}.
\]

Then the total cap capacity has the exact decomposition

\[
 \boxed{C_Q(T)=\sum_{q=1}^d\bigl(D_q(Q;T)+B_{q,Q}(T)\bigr).} \tag{4.8}
\]

For an interior **unplanted common-order** coatom move, the boundary terms
are unchanged.  On a
reflected pair `q'=d+2-q`, the move satisfies

\[
 \Delta D_q(\{x,y\})=\Delta D_{q'}(\{x,y\}).                 \tag{4.9}
\]

It therefore fixes the antisymmetric mode `D_q-D_q'` but changes the
symmetric capacity contribution by

\[
 \Delta(D_q+D_{q'})=2\Delta D_q.                             \tag{4.10}
\]

#### Proof

Equation (4.8) is Lemma 1.1 summed over all compiler rows: its interior caps
are exactly the natural depth-`q` intersections and its remaining caps are
the two boundary banks.  Equations (4.9)--(4.10) are the coatom reflected
pair law and its sum.  \(\square\)

This explains algebraically why routing inside one restricted reflected
fibre remains possible.  The statistic freezes a difference coordinate
there, while the pair-capacity Hall cut lives primarily in the sum
coordinate.  In the full planted catalogue even the difference coordinate
can be changed by adjacent-order twists.

## 5. Consequence for the serial `B+O(1)` route

The reflected pair statistic should not be treated as an obstruction.  The
exact finite data show that zero-deletion terminal compilers already occur
at nontrivial values and routinely use proper subsets of natural caps; the
planted adjacent-order variants additionally supply a saturated projected
breaker lattice.

The sharp next target is one of the following.

1. Reach a carrier `T` possessing a protected base compiler whose
   transparent cap-linkage deficiency is `O(1)`.
2. More generally, prove the same bounded augmenting-linkage conclusion in
   the complete common-`Q` conflict hypergraph.
3. Couple the planted adjacent-order filler squares to literal compiler
   augmenting ears while retaining nonnegative occurrence counts.

What remains open is therefore **nonnegative physical reachability plus
compiler augmentation**, not reflection cancellation.

## 6. Replay

Run

```text
python3 scratch/audit_reflection_fibre_compiler_bypass_20260801.py
```

The output is

```text
scratch/reflection_fibre_compiler_bypass_20260801.audit.json
```

with expected status

```text
PASS_REFLECTION_FIBRE_COMPILER_BYPASS
```

No all-`k` bounded-deletion theorem or safe-component reachability theorem
is claimed.
