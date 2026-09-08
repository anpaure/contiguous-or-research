# Thread D: exact transport of Pascal flag packages under the adjacent-row lifts

Date: 2026-07-28

Status: theorem-level preservation audit and conditional induction lemma.  No
unconditional recurrence is claimed.

## 0. Verdict

The Pascal flag package of
`MATH_PASCAL_FLAG_PACKAGE_AND_CATALAN_LIQUIDITY_20260728.md` is a sufficient
normal form, but in its present depth-`d(k)` form it is **not closed** under
either adjacent-row lift.

What is functorial is substantial but limited:

1. the child middle labels split into the advertised Pascal rows exactly;
2. fixed-coordinate copies preserve Johnson edges, nested flag identities,
   natural-pin freeness, and a homogeneous trace-two owner realization;
3. on every uncut first-shadow interval, lower flags move one row downward
   and upper flags move one row upward in the precise sense proved below;
4. in the complement-antipodal odd-graph model, all parent upper ranks are
   one descending flag cover, so their complete **label supply** transports
   at every depth, not merely at the `q=2` turn row;
5. the deadline and Catalan counts transport exactly.

The forced point-degree marginals are also no longer an open rankwise gate:
whenever `0<=gamma_(q,x)<=e_q`, hypersimplex integer decomposition produces
a hole-free multiset with those exact degrees.  The unresolved issue is
lifting the separately feasible rows to one chronology and one owner core.

For the PBBS asymptotic lane, pure segment topology is now separated even
more sharply: reconnecting `J` cut slots changes the short-return packing
number by at most `J`, independently of the residence scale.  Hence any
`O(Cat_m)` pure Hamiltonization preserves the critical `ST_A` condition in
both directions; it transfers that gate but cannot prove it.

The nonfunctorial data are exactly the data that mix pieces:

* sufficient residence on the eroded shore;
* Johnson seams and seam-composed run lengths;
* survival or replacement of occurrences destroyed by cuts and selectors;
* compatible nested endpoint flags;
* one common child spill/deep-owner table after all sectors are superposed.

The strongest honest induction statement is therefore a
**certificate-to-package lemma**.  A parent package supplies all homogeneous
bulk data.  A finite seam/occurrence certificate and one combined trace-two
owner certificate then produce a child package.  These certificates are not
consequences of parent optimality or even of the unbuffered parent package.

## 1. Notation and the strict meaning of package preservation

Let

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W_k=\binom{k}{r},
 \qquad \Lambda_k=\sum_{j=1}^{r-1}\binom{k}{j},
\]

and let `d(k)` be the least nonnegative integer satisfying

\[
 \Lambda_k\le d(k)W_k+\binom{d(k)+1}{2}.
\tag{1.1}
\]

For a Johnson chronology

\[
 T=(T_0,\ldots,T_{W-1}),
 \qquad T_{i+1}=T_i-\{a_i\}+\{b_i\},
\]

write

\[
 L_T^{(q)}(i)=\bigcap_{h=0}^{q}T_{i+h},
 \qquad
 U_T^{(q)}(i)=\bigcup_{h=0}^{q}T_{i+h}.
\tag{1.2}
\]

The strict Pascal ladder has a fixed rank at every row.  Consequently a
concatenated child chronology is a strict Pascal-package chronology only if
every transition, including every final seam, is a Johnson edge.  A seam of
rank distance `s>1` may be useful in the seam-relaxed direct compiler, but
its first intersection has rank `R-s`, not `R-1`; it therefore does not
preserve the strict package of Section 8 of the package note.

This distinction will be maintained throughout:

* **strict lift:** outputs another Pascal flag package and requires Johnson
  seams;
* **seam-relaxed lift:** may output an optimal literal word after a direct
  multirow compiler, but does not by itself output the same induction
  invariant.

## 2. The exact flag functor on homogeneous pieces

Let `S` be disjoint from the ground set of a row `R`, and put

\[
 \iota_S(X)=S\cup X.
\]

### Lemma 2.1 (fixed-signature flag transport)

For every window contained in a fixed-signature piece,

\[
 L_{\iota_S R}^{(q)}(i)=S\cup L_R^{(q)}(i),
 \qquad
 U_{\iota_S R}^{(q)}(i)=S\cup U_R^{(q)}(i).
\tag{2.1}
\]

The same statement holds after reversing a piece, up to reversal of the
window starts.  Moreover, `\iota_S` preserves Johnson adjacency.

#### Proof

Because `S` is present in every term,

\[
 \bigcap_h(S\cup R_h)=S\cup\bigcap_hR_h,
 \qquad
 \bigcup_h(S\cup R_h)=S\cup\bigcup_hR_h.
\]

Reversal changes only the order of the same window vertices.  Finally,
adjoining the same disjoint set does not change the symmetric difference of
two vertices.  \(\square\)

### Lemma 2.2 (row-of-row identities)

On every natural interior on which the indicated rows are defined,

\[
 L_{L_T^{(a)}}^{(q)}(i)=L_T^{(a+q)}(i).
\tag{2.2}
\]

If `T` is lower-`1`-fresh, then for `q>=1`,

\[
 U_{L_T^{(1)}}^{(q)}(i)=U_T^{(q-1)}(i+1).
\tag{2.3}
\]

Thus a first-shadow shore shifts every lower flag down by one and every
positive upper flag up by one.

#### Proof

For (2.2), the index intervals `[i+h,i+h+a]`, `0<=h<=q`, have union
`[i,i+a+q]`; repeated intersections are immaterial.  Hence

\[
 \bigcap_{h=0}^{q}\bigcap_{j=0}^{a}T_{i+h+j}
 =\bigcap_{u=0}^{a+q}T_{i+u}.
\]

Put `Q_i=L_T^(1)(i)=T_i\cap T_(i+1)`.  Lower-`1`-freshness excludes an
immediate deletion of the newly inserted element, and therefore

\[
 T_j=Q_{j-1}\cup Q_j.
\tag{2.4}
\]

Every `Q_(i+h)` in the left side of (2.3) is contained in one of
`T_(i+1),...,T_(i+q)`, while (2.4) puts every one of those middle vertices
in the union of the `Q` window.  This proves (2.3).  \(\square\)

Equations (2.2)--(2.3) concern the natural first-shadow row.  An inserted
completion vertex, a cut, or a join creates a collar where the equations
must be checked directly.  No completion or collar identity is hidden in
the lemma.

### Lemma 2.2a (exact endpoint completion of the first-shadow row)

Suppose `T` is a Johnson Hamilton path, the sets

\[
 X_i=T_i\cap T_{i+1}\qquad(0\le i<W-1)
\]

are distinct, and their unique missing rank-`r-1` set `H` is contained in
`T_0` after orienting the path.  Put

\[
 Q=(H,X_0,X_1,\ldots,X_{W-2}).
\tag{2.6}
\]

Then `Q` is a Johnson Hamilton path through the rank-`r-1` layer.  For
`q>=1`,

\[
 L_Q^{(q)}(0)=H\cap X_0\cap\cdots\cap X_{q-1},
\tag{2.7}
\]

while, for `t>=1`,

\[
 L_Q^{(q)}(t)=L_T^{(q+1)}(t-1).
\tag{2.8}
\]

At every valid start,

\[
 U_Q^{(q)}(t)=U_T^{(q-1)}(t).
\tag{2.9}
\]

In particular, the endpoint completion is lower-rank-correct through depth
`e` exactly when

\[
 |H\cap X_0\cap\cdots\cap X_{q-1}|=r-1-q
 \qquad(1\le q\le e).
\tag{2.10}
\]

#### Proof

The two terms at every `Q` transition are distinct rank-`r-1` facets of a
common rank-`r` set (`T_0` at the first transition and the appropriate
`T_i` thereafter), so they are Johnson adjacent.  The labels are all
distinct and exhaust the layer.

Equation (2.8) is associativity of intersection.  For upper rows,
`H union X_0=T_0` and

\[
 X_{j-1}\cup X_j=T_j.
\]

Taking consecutive unions proves (2.9), including the completed endpoint.
Equation (2.7) is the definition, and its required row rank is (2.10).
\(\square\)

Thus endpoint accessibility closes the upper completion exactly, but the
lower endpoint flag still has the explicit rank tests (2.10).  Neither the
one-hole count nor parent residence alone implies those tests.

### Lemma 2.3 (homogeneous owner transport)

Suppose a parent interval realization has maximal envelope `E_p`, active
owners `O_p^1,O_p^2` (with repetitions or omissions allowed), and core

\[
 C_p=E_p\cap O_p^1\cap O_p^2.
\]

Inside a fixed-signature child piece, transport every set by `\iota_S`.
Then

\[
 (S\cup E_p)\cap(S\cup O_p^1)\cap(S\cup O_p^2)
 =S\cup C_p.
\tag{2.5}
\]

Thus pointwise owner meet dimension at most two, nonemptiness, central
positive hits, target positive hits, and natural-pin freeness are preserved
inside that homogeneous piece.

#### Proof

Identity (2.5) is distributivity of intersection over a common fixed set.
Unions over any transported interval satisfy

\[
 \bigcup_p(S\cup C_p)=S\cup\bigcup_pC_p.
\]

Hence all parent equalities and private hits transport.  A natural pin did
not shrink `E_p`, and its transported copy does not shrink `S\cup E_p`.
\(\square\)

This lemma does **not** combine owner tables from different signatures.
At a mixed seam, owners which were harmless separately can meet in an empty
set.  For example, with envelope `{1,2}`, the separate cuts `{1}` and `{2}`
are nonempty, while their common core is empty.  The common-child-owner
condition below is therefore logically necessary.

## 3. Exact depth arithmetic

### 3.1 Odd to even

Let the parent have size `2r-1`, and put

\[
 W=\binom{2r-1}{r},\qquad
 \Lambda=\sum_{j=1}^{r-1}\binom{2r-1}{j},\qquad
 d=d(2r-1),
\]

\[
 t_d=\binom{d+1}{2},\qquad
 \sigma=dW+t_d-\Lambda.
\]

The even child has

\[
 W_e=2W,
 \qquad
 \Lambda_e=2\Lambda-W+1.
\tag{3.1}
\]

### Proposition 3.1 (exact odd-to-even deadline dichotomy)

For `r>=2`,

\[
 \boxed{d(2r)\in\{d-1,d\}.}
\tag{3.2}
\]

More precisely,

\[
 \boxed{
 d(2r)=d-1
 \iff
 2\sigma\ge W+\frac{d(d+3)}2+1.}
\tag{3.3}
\]

Otherwise `d(2r)=d`.

#### Proof

Pascal's identity and symmetry give

\[
 \begin{aligned}
 \Lambda_e
 &=\sum_{j=1}^{r-1}
   \left(\binom{2r-1}{j}+\binom{2r-1}{j-1}\right)\\
 &=\Lambda+(\Lambda+1-W),
 \end{aligned}
\]

which proves (3.1).  Since `d<=r-1`,

\[
 W=\binom{2r-1}{r-1}
 \ge\binom{r+1}{2}
 \ge t_d+1.
\]

Consequently

\[
 2dW+t_d-\Lambda_e
 =2\sigma+W-t_d-1\ge0,
\]

so the child depth is at most `d`.

If `d>=2`, minimality of `d` gives

\[
 \Lambda>(d-1)W+t_{d-1},
\]

and therefore

\[
 \Lambda_e>(2d-3)W+2t_{d-1}+1
            >(d-2)(2W)+t_{d-2}.
\]

Thus the child depth is at least `d-1`; the case `d=1` is immediate.  It
remains to test depth `d-1`.  Its exact slack is

\[
 \begin{aligned}
 (d-1)(2W)+t_{d-1}-\Lambda_e
 &=2\sigma-W-\bigl(2t_d-t_{d-1}\bigr)-1\\
 &=2\sigma-W-\frac{d(d+3)}2-1.
 \end{aligned}
\]

This is nonnegative exactly under (3.3).  \(\square\)

This arithmetic explains the observed distinction between the successful
same-source bulk lifts with a depth drop and the failed unchanged-depth
bulk lifts.  It says nothing about seams or owners.

### 3.2 Odd to odd by adjoining two coordinates

For `k=2r-1`, retain the notation above and put

\[
 b=C_r=\frac{2W}{r+1},
 \qquad W^+=\binom{2r+1}{r+1},
 \qquad d^+=d(2r+1).
\]

The exact identities from the four-sector audit are

\[
 W^+=4W-b,qquad \Lambda^+=4\Lambda+3,
\tag{3.4}
\]

and

\[
 \boxed{d^+\in\{d,d+1\},}
\tag{3.5}
\]

with

\[
 \boxed{
 d^+=d
 \iff
 4\sigma\ge db+3t_d+3.}
\tag{3.6}
\]

Indeed, the depth-`d` child slack is exactly

\[
 dW^++t_d-\Lambda^+=4\sigma-db-3t_d-3,
\]

and the adjacent-depth bounds give (3.5).  Again, this is a scalar capacity
recurrence, not a labelled Hall theorem.

## 4. Signature-by-signature flag transport

It is useful to record ranks before considering chronology.  A signed rank
offset is measured from the parent middle rank.

### 4.1 Odd to even

The child middle rank and parent middle rank are both `r`.  If a child set
has signed offset `epsilon` and contains `s` copies of the single new
coordinate `z`, its old trace has signed offset

\[
 \epsilon-s.
\tag{4.1}
\]

For the exact deck

\[
 T\ \sqcup\ (z+\widehat L_T^{(1)}),
\tag{4.2}
\]

the natural bulk rows therefore obey:

| child shore | child lower depth `q` uses | child upper depth `q` uses |
|---|---:|---:|
| `A=T` | parent lower `q` | parent upper `q` |
| `B=z+L^(1)` | parent lower `q+1` | parent upper `q-1` |

The upper entry for `B` is Lemma 2.2 and is meant for `q>=1`; at `q=1`
the parent row is simply `T`.

Let `e=d(2r)`.  The `A` bulk is lower-`e`-fresh whenever the depth-`d`
parent is, because `e<=d`.  The `B` bulk requires parent lower freshness
through `e+1`:

* if `e=d-1`, the parent package has exactly the needed bulk buffer;
* if `e=d`, one additional residence/flag level is required.

The completion vertex and all cuts remain direct endpoint/collar checks in
both cases.

### 4.2 The `k -> k+2` four-sector deck

The child middle rank is `r+1`.  If a child set has signed offset `epsilon`
and contains `s` of `{x,y}`, its parent trace has signed offset

\[
 \epsilon+1-s.
\tag{4.3}
\]

For lower depth `q`, this gives parent lower depth `q+s-1`; for upper depth
`q`, it gives parent upper depth `q+1-s`.  Hence:

| child sector | present new tags | lower depth `q` uses | upper depth `q` uses |
|---|---:|---:|---:|
| `A=xy+L^(1)` | 2 | parent lower `q+1` | parent upper `q-1` |
| `X=x+T` | 1 | parent lower `q` | parent upper `q` |
| `Y=y+T` | 1 | parent lower `q` | parent upper `q` |
| `U=U_*` | 0 | parent lower `q-1` | parent upper `q+1` |

An entry is asserted only when that signature class is nonempty.  At an
extreme rank where the old trace size is outside the parent Boolean lattice,
there is no target in that class to transport.

The `A,X,Y` entries are realized on natural bulk intervals by Lemmas
2.1--2.2.  The `U` entries are only a **rank/label identity**: `U_*` chooses
one occurrence of each rank-`r+1` parent target.  Choosing representatives
and rethreading them need not preserve any consecutive occurrence interval.
Thus the entire `U` chronology is an exceptional routing sector unless a
stronger occurrence-preserving selector is exhibited.

At the deepest child lower row:

* `X` and `Y` require parent freshness through `d^+`;
* `A` requires parent freshness through `d^++1`;
* `U` requires a direct selector/residence audit.

If `d^+=d`, the parent package suffices for the `X/Y` bulk but is one level
short for `A`.  If `d^+=d+1`, it is one level short for `X/Y` and two levels
short for `A`.  This is a literal obstruction to closure of the unbuffered
depth-`d` invariant.

## 5. The complement-antipodal all-depth flag tower

Theorem 2.6 of
`MATH_K15_COMPLEMENT_ANTIPODAL_MIDDLE_LEVELS_REDUCTION_20260728.md` removes
an ambiguity in the phrase “parent upper support.”  Let an antipodal
middle-levels lift be encoded by an odd-graph cycle, put `B_i=A_(2i)`, and
write its missing-element edge colours as `z_j`.  Define

\[
 F_i^{(q)}=\bigcap_{h=0}^{q-1}B_{i+h}.
\tag{5.1}
\]

Then

\[
 \boxed{
 F_i^{(q)}
 =B_i\setminus\{z_{2i+1},z_{2i+3},\ldots,z_{2i+2q-3}\}.}
\tag{5.2}
\]

As multisets, the complements of the parent upper depth-`q-1` traces are
exactly the `F_i^(q)`.  Thus parent upper universality is equivalent to

\[
 \{F_i^{(q)}:i\in\mathbb Z_W\}
 \supseteq \binom{[2m+1]}{m-q+1}
\quad\hbox{for every }q.
\tag{5.3}
\]

The `q=2` turn-surjectivity condition is only the first nontrivial row of
this full descending tower.

Combining (5.3) with the signature table gives the exact parent flag rows
whose occurrences must be retained:

| lift sector | child upper depth `q` is dual to parent flags |
|---|---:|
| odd-even `A` | `F^(q+1)` |
| odd-even `B` | `F^q` |
| `k+2` sector `A` | `F^q` |
| `k+2` sectors `X,Y` | `F^(q+1)` |
| `k+2` sector `U` | `F^(q+2)` |

For the odd-to-even lift this is the following collar-free flag square:

\[
\begin{array}{c|cc}
 &\text{child lower depth }q
 &\text{old-ground complement of child upper depth }q\\ \hline
 A&T\text{-row }F^{(q)}&F^{(q+1)}\\
 B=z+L^{(1)}&z+F^{(q+1)}&F^{(q)}.
\end{array}
\tag{5.5}
\]

Thus the adjacent rows are exchanged across the two shores.  This is the
all-depth form of the turn-map duality.

Therefore an audited all-depth PBBS support factor closes the **parent
upper-label supply** for all these rows.  What it does not close is survival
under a cut, selection of the `U_*` representatives, or rethreading into the
child chronology.  A correct lift must transport occurrences of the entire
flag tower (5.1), not only `q=2` turns.

There is an equally exact residence interpretation.  If

\[
 z_{2i}=b_i,\qquad z_{2i+1}=a_{i+1},
\]

then depth-`h` residence is equivalent to

\[
 z_{2i}\ne z_{2i+2t-1}\qquad(1\le t\le h).
\tag{5.4}
\]

For an antipodal odd-graph lift, `t=1` is automatic.  Hence the extra
first-shadow buffer required by an unchanged-depth odd-even lift is exactly
the additional forbidden odd distance `2e+1`.  In the two-coordinate lift,
the `A` bulk through child depth `d^+` likewise requires exclusion through
distance `2d^++1`, while `X/Y` require exclusion only through
`2d^+-1`.  These memory distances depend on the deadline, not on divisors of
the dimension.

## 6. Locality of the nonfunctorial part

Suppose a source path is cut into pieces of lengths
`ell_1,...,ell_c`.  At depth `q`, the number of internal windows is exactly

\[
 I_q=\sum_{j=1}^{c}(\ell_j-q)^+.
\tag{6.1}
\]

If every piece is longer than `q`, joining the pieces creates exactly

\[
 (c-1)q
\tag{6.2}

crossing windows relative to their disjoint union.  Every lost or new
witness lies in a `q`-collar of a cut or join.  For short pieces, (6.1), not
the simplified count (6.2), is the valid formula.

This localizes, but does not solve, the support problem.  If a target has a
unique parent occurrence and that occurrence crosses a cut, a correct label
count cannot save it.  It needs a retained second occurrence or a named
seam/collar witness.  Likewise, the scalar `2q` endpoint capacity does not
place holes on compatible nested endpoint chains.

The exception in the four-sector lift is the selected `U` shore: a
representative selector can alter occurrences throughout that shore, so its
support audit is not confined to a bounded seam collar unless the selector
itself has an occurrence-preserving theorem.

## 7. A noncircular certificate-to-package theorem

We now state the strongest common induction lemma supported by the exact
functorial identities.

### Definition 7.1 (certified strict tagged lift at depth `e`)

A certified strict tagged lift consists of the following explicit finite
data.  Write its assembled child chronology as

\[
 T^+=(T_0^+,\ldots,T_{W_K-1}^+).
\]

1. **Exact deck and pieces.**  Every child middle label occurs once.  The
   deck is partitioned into oriented pieces.  Each ordinary piece is a
   fixed-signature segment of `T` or of its natural completed first-shadow
   row; any selected/rethreaded sector is declared exceptional and supplied
   explicitly.
2. **Strict ports and residence.**  Every internal edge and every final join
   is Johnson.  In the fully assembled chronology, every maximal coordinate
   one-run has length at least `e+1`, including runs which cross several
   joins through one or more all-one intermediate pieces.  Completion
   vertices are included.  Terminal/initial ports are merely a compressed
   way to perform this global run check.
3. **All-depth upper occurrence ledger.**  For every child upper target and
   every upper depth, the ledger names either
   * a parent flag occurrence whose entire child window survives inside one
     ordinary piece, or
   * an explicitly verified exceptional or seam-crossing child window.
   In the antipodal model the inherited occurrences are indexed by the
   appropriate `F^(q)` row from the table in Section 5.
4. **Nested lower endpoint/collar ledger.**  For every `1<=q<=e`, all
   inherited natural lower flags away from cuts are retained.  Every lower
   flag entry destroyed by a cut, completion, or join is either duplicated
   elsewhere or assigned to an actual compatible endpoint/spill cell.  The
   named endpoint values obey the same intersection recursion and are
   nested across `q`.
5. **One common owner certificate.**  Natural retained shadow pins are
   declared free.  Every remaining lower, spill, seam, boundary, and deep
   target `S` is assigned injectively to an eligible physical interval
   `I_S`.  With `E_p` the maximal child envelope, put

   \[
   C_p=E_p\cap\bigcap_{S:p\in I_S}S.
   \tag{7.1}
   \]

   The combined family, not each sector separately, satisfies:

   \[
   C_p\ne\varnothing\quad\hbox{for every }p;
   \tag{7.2}
   \]

   \[
   \forall i\ \forall x\in T_i^+
   \quad\exists p\in[i,i+e]\quad x\in C_p;
   \tag{7.3}
   \]

   \[
   \forall S\ \forall x\in S
   \quad\exists p\in I_S\quad x\in C_p;
   \tag{7.4}
   \]

   and at every `p`, the intersection in (7.1) is already attained by at
   most two active nonfree owners.

The interval eligibility in item 5 includes the rank/derivative-row rule;
an actual injective assignment is stronger than merely asserting its Hall
inequalities.

### Theorem 7.2 (strict adjacent-row lift lemma)

If a parent Pascal flag package supplies the ordinary rows of a certified
strict tagged lift at the child deadline `e=d(K)`, then the certified data
form a depth-`e` Pascal flag package on the child ground set.  Consequently

\[
 \boxed{\nu(K)=B(K).}
\tag{7.5}
\]

#### Proof

The exact deck and strict ports give a path cover with the specified seam
order and a global Johnson chronology.  The port-run test is the exact
coordinatewise residence criterion, so the chronology is lower-`e`-fresh.
The Pascal ladder theorem then generates every natural nested lower row.
Lemmas 2.1--2.2 identify all inherited interior flags; item 4 supplies the
only entries that those lemmas do not address.  This proves the completed
endpoint-flag part of the package.

The upper occurrence ledger gives complete consecutive-union support at
every upper rank.  It is crucial here that the ledger names surviving
occurrences rather than merely parent labels.

For the lower compiler, every natural pin is free.  The explicit injection
of all remaining targets proves the corresponding containment Hall and
liquidity inequalities.  Since `C_p` is contained in every active target and
in every central envelope, (7.3)--(7.4) imply exactly

\[
 \bigcup_{p=i}^{i+e}C_p=T_i^+,
 \qquad
 \bigcup_{p\in I_S}C_p=S.
\tag{7.6}
\]

Together with (7.2) and the trace-two hypothesis, these are precisely the
three conditions of the trace-two realization criterion.  Hence the spill
and deep ideals are realized by one nonzero physical word, and all six
package properties hold.  Package sufficiency proves (7.5).  \(\square\)

The theorem is noncircular.  Its hypotheses are checkable statements about
an explicit deck, ports, windows, flag occurrences, and interval
intersections.  It assumes neither a child universal word nor the conclusion
that a child package exists.  Its unresolved content is an existence theorem
for items 2--5, not another scalar inequality.

If item 2 allows rank-distance seams and items 3--5 are replaced by the
exact cross-depth `(US*)` ledger and direct multirow compiler, the same final
literal-word argument yields one-step optimality.  It does **not** prove
strict package preservation, because the global rank-by-rank Pascal ladder
is broken at those seams.

## 8. Specialization to the odd-to-even lift

### Corollary 8.1 (buffered six-piece package lift)

Let `e=d(2r)`.  Suppose:

1. an `A` source supplies a rank-`r` Johnson chronology `T` that is
   lower-`e`-fresh;
2. a `B` source supplies an endpoint-completable first-shadow path
   `\widehat L^(1)` enumerating every parent rank-`r-1` set, whose natural
   part comes from a lower-`(e+1)`-fresh chronology;
3. the two exact shores are cut into an alternating six-piece order with
   five Johnson seams and the exact port-run test;
4. the all-depth upper occurrence ledger retains the corresponding parent
   occurrences (`F^(q+1)` on `A` and `F^q` on `B` in an antipodal source),
   and supplies every completion/collar exception;
5. the nested endpoint ledger and one common owner certificate of Definition
   7.1 are given.

Then the even child has a depth-`e` Pascal flag package and

\[
 \nu(2r)=B(2r).
\]

#### Proof

The deck identity gives every child middle set exactly once.  Lemmas
2.1--2.2 give all ordinary bulk flags and owner transports.  The remaining
hypotheses are exactly the exceptional data in Theorem 7.2.  \(\square\)

The `A` and `B` sources may be different.  If `e=d-1`, a depth-`d` parent
has the exact natural bulk buffer required on `B`.  If `e=d`, a depth-`d`
package alone does not: a parent run of length `d+1` becomes a first-shadow
run of length `d`, which is too short.  This is the sharp one-run obstruction
behind the failed same-depth calibrations.  Even in the favourable depth-drop
case, the five seams, collars, endpoint alignment, and common owner table
remain additional hypotheses.

## 9. Specialization to the `k -> k+2` lift

The exact child deck is

\[
 (xy+\widehat L^{(1)})
 \sqcup(x+T)\sqcup(y+T)\sqcup U_*.
\tag{9.1}
\]

Immediate parent upper completeness permits one occurrence of every
rank-`r+1` set to be selected for `U_*`, so (9.1) is an exact middle-owner
partition.  This says nothing about the order of `U_*`.

There is one further inherited object under a stronger first-face
hypothesis.  If `\widehat L^(1)` is a Johnson Hamilton path and its edge
intersections cover every rank-`r-2` set, choose one edge of each such
colour.  The selected subgraph has

\[
 W-\binom{2r-1}{r-2}=C_r
\]

components and, after adjoining `x,y`, realizes every both-new
immediate-lower target exactly once.  This is the exact Catalan `A` forest.
Neither second-shadow completeness nor this selected forest follows from
the six-item package definition alone.

### Corollary 9.1 (buffered four-sector package lift)

Let `d^+=d(2r+1)`.  Suppose the exact deck (9.1), optionally retaining the
exact Catalan `A` forest, is supplied with:

1. parent lower freshness through `d^+` on `X/Y` and through `d^++1` on the
   natural `A` shore;
2. an explicit one-copy ordering of `U_*`, all final Johnson seams, and the
   exact child port-run test;
3. an all-depth occurrence ledger which, in the antipodal model, transports
   `F^q,F^(q+1),F^(q+2)` on `A`, `X/Y`, and `U`, respectively;
4. compatible nested endpoint/collar flags and one common trace-two owner
   certificate for all four sectors.

Then the child has a depth-`d^+` Pascal flag package and

\[
 \nu(2r+1)=B(2r+1).
\]

#### Proof

The signature table and Lemmas 2.1--2.2 discharge the `A/X/Y` bulk.  The
explicit `U` order and the three remaining certificates give Definition
7.1.  Apply Theorem 7.2.  \(\square\)

This is strictly stronger in its seam conclusion than the existing
seam-relaxed four-sector theorem.  The latter is an exact and useful
one-step theorem, but arbitrary-rank seams and an unrestricted direct
compiler do not return the strict invariant needed for induction.

## 10. Property-by-property audit

| Pascal-package datum | odd `->` even | `k -> k+2` |
|---|---|---|
| exact child middle labels | automatic from `T` and completed `L^(1)` | automatic from completed `L^(1)`, two copies of `T`, and an immediate-upper selector `U_*` |
| internal Johnson edges | automatic on fixed-tag `T/L^(1)` pieces | automatic on `A/X/Y`; not on selected `U` |
| final Johnson seams | not inherited | not inherited |
| target lower freshness | `A` inherited; `B` needs one more parent unit | `X/Y` need `d^+`; `A` needs `d^++1`; `U` direct |
| natural nested lower flags | transported in collar-free pieces | transported in `A/X/Y`; `U` direct |
| completed endpoint flags | not inherited through cuts/joins | not inherited; the Catalan `A` forest is only a first-face partial result |
| all-depth upper label supply | transported from the full parent flag tower | transported by signed depth, including `F^(q+2)` labels for `U` |
| upper occurrence survival | requires a collar ledger | requires a collar ledger and a global `U` selector audit |
| scalar deadline/Catalan liquidity | exact dichotomy (3.2)--(3.3) | exact recurrence (3.4)--(3.6) |
| labelled spill/Hall | not inherited | not inherited |
| natural-pin freeness | inherited in homogeneous pieces | inherited in homogeneous pieces and at actual maximal seam cells |
| trace-two owner realization | inherited only before sectors interact | inherited only before sectors interact |
| common physical owner core | new child gate | new child gate |
| defect point-degree transport of handoff Section 339 | applies once the child is resident; the hypersimplex theorem removes every rankwise marginal hole when its coordinate bounds hold | same; separate zero-hole rows still need one synchronized chronology and owner core |

## 11. Exact seam and owner assumptions that may not be suppressed

For a child middle seam `M|N` of rank `R`, put

\[
 s=R-|M\cap N|.
\]

Then the seam exposes `M union N` at upper depth `s` and `M intersection N`
at lower depth `s`.  It preserves the strict first Pascal row exactly when
`s=1`.  Even then, the lower seam cell is only a free **negative** pin: after
all other owners are imposed, it still needs its positive hits in the common
core.

Accordingly a strict induction proof must state all of the following.

1. Every final seam is Johnson.
2. Every seam-composed coordinate run has length at least the child deadline
   plus one.
3. At every lower depth through the deadline, cut and join collars are
   reconciled on the actual nested endpoint chains.
4. At every upper depth, each target has a named surviving internal or seam
   occurrence.  A side-size count and the `q=2` turn row are insufficient.
5. Every transported pin interval that crosses a cut is either moved wholly
   into a homogeneous piece or reclassified as a child seam/spill pin.
6. Spill, seam, boundary, and deep pins are combined before owner dimension
   is measured.  Separate rankwise or sectorwise cores do not suffice.
7. The combined cores satisfy nonemptiness, central private hits, target
   private hits, and meet dimension at most two.

These are exact hypotheses, not technical conveniences.

## 12. Circularity audit and surviving induction gate

The following implications are invalid:

\[
 \nu(k)=B(k)\quad\Longrightarrow\quad
 \hbox{a Pascal flag package exists};
\]

positive deadline slack does not force a flat resident Johnson chronology.
Likewise,

\[
 \hbox{parent package}\quad\Longrightarrow\quad
 \hbox{child package under either raw deck lift}
\]

is false because the first-shadow shore needs one more flag/residence level
and the shared owner table is absent.

The complete-antipodal/PBBS all-depth flag theorem improves the situation in
one precise way: it removes parent upper **support generation** from the list
of open tasks.  The required flags are already present at every depth.  The
surviving problem is to route whole flag occurrences through cuts, the
`U_*` selection, and strict seams while simultaneously preserving one
trace-two owner core.

Thus the exact induction gate is:

> **Simultaneous hypersimplex/flag lift and common-owner theorem.**  Starting
> from the separately feasible hole-free rank rows and an all-depth parent
> flag factor, construct one child deletion chronology which realizes those
> rows compatibly, retains the required descending-flag occurrences, passes
> the exact residence/Johnson-port tests, completes the nested endpoint
> collars, and admits one combined trace-two residual assignment.

Theorem 7.2 proves that this gate is sufficient and iterative.  Sections 8
and 9 identify the exact buffer and selector burden in the two lifts.  No
remaining scalar or `q=2` reformulation proves it.

## 13. What the PBBS all-depth theorem closes

The parent-support input in Section 5 is not conjectural for the canonical
PBBS factor.  Theorem 21.2 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, independently audited in
`MATH_AUDIT_PBBS_ALLQ_CORRIDOR_AND_FIXED_BAND_WORDS_20260726.md`, proves the
following stronger statement.

### Theorem 13.1 (audited PBBS canonical flag paths)

For every `1<=q<=m` and every

\[
 S\in\binom{[2m+1]}{m-q},
\]

the oriented PBBS map `g=f^2` contains a canonical `q`-edge path

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q
\]

such that

\[
 \bigcap_{t=0}^{q}B_t=S.
\tag{13.1}
\]

The number of correctly ranked oriented occurrences of any fixed `S`
satisfies

\[
 1\le \mu_{P,q}^{\rm corr}(S)\le\binom{2q+1}{q}.
\tag{13.2}
\]

Together with the complement-antipodal identity (5.3), this supplies the
complete lower and upper flag towers on the PBBS cycle factor.  In
particular, a new `q=2` turn-surjectivity argument is neither needed nor
sufficient: all depths already have canonical support.

The upper bound in (13.2) must not be misread as redundancy.  It gives no
lower bound larger than one.  A target whose unique canonical occurrence
crosses a cut can still be lost.  What remains is occurrence-preserving
routing, residence, and owners.

The published Middle-Levels Hamiltonization does not close that routing
problem.  The source audit in
`MATH_AUDIT_PBBS_VERSUS_LEXICAL_MIDDLE_LEVELS_HAMILTONIZATION_20260726.md`
proves that the Gregor--Mütze--Nummenpalo connector theorem starts from the
`0/1` lexical factor, not the PBBS factor.  The two factors are already
nonisomorphic at `m=2`.  Thus its Hamilton cycle cannot inherit (13.1) by
identification.

## 14. A local connector invariant for all flag depths and residence

The next lemma is the useful conclusion available without a new PBBS
Hamiltonization theorem.

Let a directed cycle factor be cut at a set `C` of `J` directed edges.
Reconnect the resulting directed blocks in any order using `J` new seams,
preserving each block interior up to reversal of the whole block.  A
`q`-flag occurrence means a path of `q` consecutive directed edges.  For a
PBBS factor, let
`I_H(P)` be its consecutive-omitted-label return intervals of positive
residence length at most `H`, and let `nu_H(P)` be their edge-disjoint
packing number.  Under the authoritative PBBS convention, such an interval
contains at most `H+1` projected transition edges: insertion, internal
residence, and removal.

### Lemma 14.1 (cut/splice Lipschitz lemma)

Under the preceding block splice:

1. at most `qJ` old `q`-flag occurrences are destroyed, and at most `qJ`
   new `q`-flag occurrences cross new seams;
2. the symmetric difference of the old and new short-return families has
   size at most `2(H+1)J`;
3. consequently

   \[
   \boxed{|\nu_H(P')-\nu_H(P)|\le J.}
   \tag{14.1}
   \]

#### Proof

A fixed directed cut edge belongs to exactly `q` cyclic windows of `q`
edges, counted with their starts.  Taking a union bound over `C` proves the
old-occurrence assertion; the same argument applies to new seams.

A consecutive-label return interval of residence length at most `H` which
is altered by cutting a block must cross one of the cut edges.  It contains
at most `H+1` transition edges.  For a fixed cut, its start therefore lies
among the preceding `H+1` transition positions, and each start has only one
next equal-label return.  Hence at most `H+1` old short returns cross that
cut.  The same argument bounds new short returns crossing each new seam.
All return intervals lying wholly inside a block are unchanged, so the
symmetric difference has size at most `2(H+1)J`.

Let `A` be the common subfamily consisting of the return intervals wholly
inside one segment.  Any member of an edge-disjoint old packing outside `A`
crosses an old cut edge.  Assign to it any old cut edge which it contains.
The assignment is injective, because two packed intervals cannot contain
the same transition edge.  Thus an old packing has at most `J` members
outside `A`.  The identical argument with the `J` new seam edges applies to
a new packing.  Hence

\[
 \nu(A)\le\nu(P)\le\nu(A)+J,
 \qquad
 \nu(A)\le\nu(P')\le\nu(A)+J,
\]

which proves (14.1).
\(\square\)

The argument includes an interval crossing several seams: it still contains
at least one seam edge, and edge-disjointness still makes the chosen-edge
map injective.  It also includes cyclic boundary intervals, because a
return not contained in an opened segment necessarily contains a cut edge.
Finally, independently reversing a segment does not change `A`: the two
consecutive equal-label occurrences and the intervening physical transition
edges are merely read in reverse.  Thus (14.1) is valid for arbitrary block
orders and orientations, provided segment interiors themselves are not
edited.

For a local connector which also changes `t` directed slots inside the
blocks, one adds the corresponding `q`-collars and short-return intervals
to the same ledger.  The important point is that a block splice is not a
pointwise change of only its new edges: for each label it can change the
return spanning a block boundary.  The `H` factor in the raw
symmetric-difference bound is therefore real.  The seam-edge injection is
what removes it from the packing-number bound (14.1).

### Corollary 14.2 (Catalan-splice invariance of the critical gate)

If `J=O(B_m)` and `H=ceil(A sqrt(m))`, then

\[
 \frac{|\nu_H(P')-\nu_H(P)|}{B_m\sqrt m}=O(m^{-1/2})=o(1).
\tag{14.2}
\]

Consequently the `ST_A` condition

\[
 \nu_H=o_A(B_m\sqrt m)
\]

holds before the splice if and only if it holds afterward.  The stronger
big-oh condition `nu_H=O_A(B_m)` is also preserved.

#### Proof

Substitute `J=O(B_m)` into (14.1).  The assertions follow in both directions
by the triangle inequality.  \(\square\)

This is a transfer theorem, not a proof of `ST_A`: Catalan-many pure splices
cannot remove a failure at the critical scale.

### Corollary 14.3 (exact occurrence connector criterion)

For a lower target `S` at depth `q`, let `O_q(S)` be the family of **all**
correctly ranked old PBBS `q`-window occurrences, let `W_q(C)` be the
`q`-edge windows meeting the cut set, and let `N_q(S)` be the family of new
seam-crossing occurrences of `S`.  Then `S` remains covered after the block
splice if and only if

\[
 \boxed{
 \bigl(O_q(S)\setminus W_q(C)\bigr)\cup N_q(S)\ne\varnothing.}
\tag{14.3}
\]

Applying this to all targets, and then complementing with the one-row shift
of Section 5, gives the exact all-depth lower/upper flag-safe connector
criterion.

#### Proof

Every old occurrence disjoint from `C` lies wholly in an unchanged block and
survives verbatim.  Every destroyed old occurrence meets `C`, and every
occurrence not inherited from an old block crosses a new seam.  These are
exactly the two families in (14.3).  \(\square\)

The criterion is deliberately occurrence-level.  If one tracks only a
chosen canonical subfamily `P_q(S) subseteq O_q(S)`, the corresponding
avoidance condition is sufficient but not necessary, because an unreserved
old witness may survive.  The cap (13.2), marginal target counts, and
point-degree balance do not imply (14.3).

There is also a sharp one-coordinate seam orientation in the odd-to-even
braid.  At a mixed Johnson seam

\[
 T_i\mid(z+Q_j),\qquad Q_j\subset T_i,
\]

the two new colours are

\[
 T_i\cap(z+Q_j)=Q_j,
 \qquad
 T_i\cup(z+Q_j)=z+T_i.
\tag{14.4}
\]

Thus mixed seams can replace a no-`z` lower occurrence or a `z`-upper
occurrence.  They cannot replace a `z`-lower occurrence or a no-`z` upper
occurrence.  In the flag-square notation, the latter two classes must retain
internal `F^(q+1)` occurrences.  This is an exact local connector invariant,
not a side-size estimate.

## 15. Topology versus residence and owners

Put

\[
 W=\binom{2m+1}{m},
 \qquad B_m=\operatorname{Cat}_m=\frac{W}{2m+1}.
\]

The PBBS projected factor has at most `B_m` cycles.  Opening one edge per
cycle therefore has at most Catalan many purely topological seams.  The
dominance-staircase theorem of Section 24 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` gives an exact `O(H)` literal
chart per active cut, simultaneously across all depths through `H`; it does
not pay separately for each `q`.  Its global ledger is

\[
 \boxed{
 L_H\le W+2HB_m+2(5H-1)\nu_H(P_m).}
\tag{15.1}
\]

The cycle-linearization term is already

\[
 2HB_m=O\!\left(\frac{HW}{m}\right).
\tag{15.2}
\]

At `H=Theta(sqrt(m))`, this is `O(W/sqrt(m))=o(W)`.  Hence a PBBS
Hamilton cycle is **not necessary** for asymptotic coefficient one.  One may
open all PBBS cycles and retain them as long components.  The sharp
remaining sufficient input for this separate-cut/dominance-staircase
architecture is the short-residence transversal/packing condition

\[
 \boxed{
 \nu_{\lceil A\sqrt m\rceil}(P_m)
   =o_A(B_m\sqrt m),}
\tag{15.3}
\]

for every fixed `A`, equivalently the `ST_A` condition of Theorem 24.4.
This theorem proves sufficiency for coefficient one, not necessity among all
possible architectures.

Lemma 14.1 makes the separation stronger.  With `J=O(B_m)` pure block
splices,

\[
 |\nu_H(P')-\nu_H(P)|=O(B_m)
   =o(B_m\sqrt m)
\]

uniformly at `H=Theta(sqrt(m))`.  Therefore `(ST_A)` holds for the original
factor if and only if it holds after any `O(B_m)` pure segment-splice
Hamiltonization.  Such a Hamiltonization cannot create a critical
short-residence obstruction, but it also cannot remove one: its entire
possible change is negligible on the `B_m sqrt(m)` scale.  Conversely,
opening the factor at a residence transversal solves topology and residence
in the correct order and needs no merge.

The exact finite formula has a different burden.  An `o(W)` appended chart
is asymptotically harmless but does not fit automatically into the exact
deadline word `W+d(k)`.  Every finite seam must instead be absorbed by the
available endpoint/spill palette and the one common owner core of
Definition 7.1.  For the asymptotic lane, a pure `O(B_m)` block-splice merge
only transfers the residence gate; it cannot prove that gate.  A materially
residence-improving connector would have to alter more than the segment
topology controlled by Lemma 14.1.  For the exact finite lane, a connector
must simultaneously satisfy:

1. **flag safety:** the occurrence criterion (14.3) at every required depth;
2. **target-depth residence:** the exact internal and port-run test; and
3. **owner compatibility:** its complete seam/collar ledger embeds in the
   exact child spill/deep assignment and preserves the common trace-two
   private hits.

Residence improvement alone does not absorb an exact seam, and owner
compatibility without flag safety or residence is likewise insufficient.
Pure Hamiltonization supplies none of these three conclusions.  The sharp
remaining PBBS
statements are accordingly:

* for asymptotic coefficient one, prove the short-residence packing bound
  (15.3) (or a stronger residence-improving connector theorem);
* for the exact finite package induction, prove a flag-safe strict splice
  satisfying (14.3), the target-depth run test, and the combined owner
  equations (7.2)--(7.4).

This is the promised separation between cheap connector topology and the
potentially decisive residence/owner effect.

## 16. Hypersimplex completion and the exact simultaneous lift gate

`MATH_HYPERSIMPLEX_MARGINAL_COMPLETION_AND_CHRONOLOGY_GATE_20260728.md`
removes the remaining rankwise-marginal ambiguity in handoff Section 339.
Let the depth-`q` trace row have target rank

\[
 s_q=r-q,
 \qquad N_q=\binom{k}{s_q},
 \qquad e_q=W-q-N_q,
\]

and let `gamma_(q,x)` be its forced excess point-degree vector after the
first-shadow defects and endpoint correction are inserted into the exact
degree-transport law.

### Theorem 16.1 (rankwise hypersimplex completion)

If

\[
 0\le\gamma_{q,x}\le e_q\qquad(x\in[k]),
\tag{16.1}
\]

then there is a multiset of `W-q` rank-`s_q` blocks which contains every
target at least once and has exactly the forced trace point degrees.
Moreover, it is connected to the actual trace multiset by symmetric
two-block exchanges.

#### Proof

The degree sum is

\[
 \sum_x\gamma_{q,x}=s_qe_q.
\]

The integer-decomposition property of the hypersimplex decomposes
`gamma_q` into `e_q` incidence vectors of `s_q`-sets.  Add these excess
blocks to one copy of every rank-`s_q` target.  The resulting multiset has
the required size, no holes, and the forced degrees.  Two uniform block
multisets with the same point degrees differ by alternating cycles in their
incidence bipartite graphs, which decompose into symmetric two-block
exchanges.  \(\square\)

For the frozen `k=15` Hall-29 carrier, the hypotheses have large slack:

\[
 e_2=1428,qquad 568\le\gamma_{2,x}\le574,
\]

\[
 e_3=3429,qquad 1138\le\gamma_{3,x}\le1147.
\tag{16.2}
\]

Thus its depth-two and depth-three holes are not forced by scalar counts,
point degrees, boundary marginals, or the complete rankwise two-block trade
lattice.

What is missing is simultaneous liftability.  A resident chronology has one
deletion/insertion word and necessarily satisfies

\[
 L_i^{(q)}
 =T_i\setminus\{a_i,a_{i+1},\ldots,a_{i+q-1}\},
\tag{16.3}
\]

\[
 L_i^{(q+1)}=L_i^{(q)}\cap L_{i+1}^{(q)},
 \qquad
 L_{i+1}^{(q)}=L_i^{(q)}-\{a_{i+q}\}+\{b_i\}.
\tag{16.4}
\]

Independent hypersimplex decompositions at two depths need not admit an
indexing satisfying (16.4), much less the same seam ports and upper flag
tower.

### Corollary 16.2 (exact remaining simultaneous hypersimplex-lift problem)

Assume (16.1) at every required lower depth and choose hole-free rankwise
completions from Theorem 16.1.  If one can orient and index their blocks so
that:

1. one Johnson deletion/insertion word realizes all recursions (16.3)--(16.4);
2. that word passes the target-depth residence and strict seam tests;
3. its all-depth upper occurrences satisfy the flag criterion (14.3); and
4. all natural, spill, seam, boundary, and deep pins satisfy the one common
   owner equations (7.2)--(7.4),

then the resulting object is a Pascal flag package and the exact optimum
follows from Theorem 7.2.

This corollary is a reduction, not an existence proof.  It identifies the
correct coupled fibre: the product of the rankwise hypersimplex fibres must
meet the image of one resident Johnson deletion word and one physical owner
core.  Another rankwise balancing or two-block connectivity lemma cannot
advance this gate.
