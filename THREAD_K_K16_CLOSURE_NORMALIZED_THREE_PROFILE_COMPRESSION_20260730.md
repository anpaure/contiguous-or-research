# K16 gap one: closure-normalized three-profile collar compression

Date: 2026-07-30  
Lane: K  
Status: exact solver-free reduction; no length-12,873 word and no profile
UNSAT theorem are claimed

## 1. Frozen input and a bookkeeping correction

The authenticated word

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

has length `12874` and covers every nonzero 16-bit target.  It lies in the
three-collar template

\[
 A_5\mid G_1\mid B_9\mid G_2\mid C_4,                 \tag{1.1}
\]

where the variable ranges are

\[
 [0,5),\qquad[6436,6445),\qquad[12870,12874).         \tag{1.2}
\]

Relative to `scratch/k16_append0200_12874_onehole.word`, the answer changes
exactly twelve cells.  The phrase “fourteen changed cells” is not consistent
with the frozen words.  The four cells newly exposed beyond the old
`(4,7,3)` atlas are `4,6436,6444,12870`; only `4` and `6436` change.

The current exact bracket is

\[
                         12873\le \nu(16)\le12874.      \tag{1.3}
\]

## 2. Deletion/fusion quotient

### Theorem 2.1 (three-profile quotient)

Shorten exactly one of the three variable collars in (1.1) by one cell,
retain both fixed gaps verbatim, and then assign arbitrary nonzero masks to
all seventeen surviving collar cells.  The resulting word family is exactly
the union of the three profile families

\[
                    (4,9,4),\qquad(5,8,4),\qquad(5,9,3).       \tag{2.1}
\]

The location of the deleted cell inside the shortened collar is immaterial.
The same conclusion holds if two adjacent cells inside that collar are first
fused and the resulting cell, together with every other surviving collar
cell, is then allowed to vary arbitrarily.

#### Proof

The fixed word outside a collar is unchanged.  After one slot is removed,
the surviving cells of that collar form an arbitrary ordered word of length
one less; hence neither their old values nor the old location of the removed
slot constrains the family.  Exactly one of the three widths falls by one,
giving (2.1).  If an adjacent pair is fused but its surviving slot is then
arbitrary, the same arbitrary shorter word family results.  This proves the
claim. \(\square\)

The last sentence does **not** identify this family with bare OR fusion, in
which the fused cell is forced to be the old pair OR.  Bare fusion is a much
smaller, already audited fibre.

## 3. Common fixed-gap repair family

Let \(F\) be the targets witnessed by intervals lying wholly in either fixed
gap.  Direct suffix-OR replay gives

\[
 |F|=65478,qquad |R|=57,qquad
 R=\{1,\ldots,65535\}\setminus F.                     \tag{3.1}
\]

The same set \(R\) occurs in all three profiles because the fixed gaps are
identical.  Their total ORs are

\[
                    \bigvee G_1=\mathtt{7fff},qquad
                    \bigvee G_2=\mathtt{ffff}.          \tag{3.2}
\]

No target in \(R\) contains either gap OR.  For `0xffff` this is immediate.
For `0x7fff`, the only containing 16-bit masks are `0x7fff` and `0xffff`,
both already in \(F\).

### Lemma 3.1 (exact local decomposition)

Every \(R\)-witness meets exactly one collar.  Within that collar it consists
of a nonempty consecutive variable subinterval, optionally preceded by a
suffix of the left adjacent fixed gap and optionally followed by a prefix of
the right adjacent fixed gap.

#### Proof

An interval meeting two collars contains the complete intervening gap, so its
OR contains the corresponding value in (3.2), impossible for a target in
\(R\).  Every interval meeting one collar has the displayed unique form.
\(\square\)

Consequently the numbers of local variable subintervals are

\[
\begin{array}{c|c}
\text{profile}&\text{local subintervals}\\ \hline
(4,9,4)&10+45+10=65,\\
(5,8,4)&15+36+10=61,\\
(5,9,3)&15+45+6=66.
\end{array}                                             \tag{3.3}
\]

## 4. Maximal-context reduction

Fix a repair target \(T\), a collar, and a nonempty variable subinterval
\(I\).  Let \(L\) be the suffix-OR chain of the adjacent left fixed gap if
\(I\) reaches the left collar boundary, and \(L=\{0\}\) otherwise.  Define
the right prefix chain \(P\) symmetrically.  Retain only values contained in
\(T\), and let \(\ell_T\) and \(p_T\) be their respective largest elements.
They exist and are unique because a suffix-OR chain and a prefix-OR chain are
nested.  Put

\[
                         b_T(I)=\ell_T\vee p_T.          \tag{4.1}
\]

### Lemma 4.1 (context domination)

For a collar assignment \(z\), some literal interval with variable part
exactly \(I\) has OR \(T\) if and only if

\[
                  b_T(I)\vee\bigvee_{i\in I}z_i=T.      \tag{4.2}
\]

#### Proof

Every allowable physical context OR is \(\ell\vee p\) with
\(\ell\subseteq\ell_T\) and \(p\subseteq p_T\), and is therefore contained
in \(b_T(I)\).  If it, together with the variable OR, equals \(T\), then the
larger context (4.1) also gives \(T\).  Conversely (4.1) itself is realized
by literal fixed suffix and prefix choices. \(\square\)

Thus there is exactly one undominated interval form for each pair \((T,I)\),
not one form for every fixed suffix/prefix combination.

## 5. Common target-closure normal form

For a nonzero mask \(v\), put

\[
 \mathcal S(v)=\{T\in R:v\subseteq T\},
 \qquad
 \operatorname{cl}(v)=\bigcap_{T\in\mathcal S(v)}T       \tag{5.1}
\]

when \(\mathcal S(v)\ne\varnothing\).  If \(\mathcal S(v)=\varnothing\),
send \(v\) to the sentinel `0x0001`.  Define

\[
 D=\{v\ne0:\mathcal S(v)\ne\varnothing,
                  \operatorname{cl}(v)=v\}.             \tag{5.2}
\]

### Theorem 5.1 (closure normalization)

Every feasible collar assignment can be normalized cellwise into \(D\)
without destroying any target witness.  Hence restricting every variable
cell to \(D\) is equisatisfiable with the unrestricted nonzero-mask model.
For the common family (3.1),

\[
             |D|=245,qquad
             \#\{v\ne0:\mathcal S(v)\ne\varnothing\}=10015.   \tag{5.3}
\]

#### Proof

If a chosen \(T\)-witness contains a value \(v\), then
\(v\subseteq\operatorname{cl}(v)\subseteq T\).  Replacing \(v\) by its
closure adds no bit outside \(T\) and cannot remove a bit already supplying
\(T\), so that interval still has OR exactly \(T\).  A dead value belongs to
no exact \(R\)-witness and can be replaced by the sentinel.  Targets in
\(F\) retain their fixed-gap witnesses.  The finite counts in (5.3) are
obtained independently both from fixed points of (5.1) and by closing the 57
targets under pairwise intersection. \(\square\)

An exact bit-CNF for \(D\) has 257 clauses and 932 literals per cell.  Direct
truth-table replay over all 65,536 masks verifies that its models are exactly
the 245 values in \(D\).  This normalization does not preserve Hamming
distance from an incumbent and must not be inserted into an exact-change
face without a separate argument.

The old `(4,7,3)` repair family has 43 targets and a 150-mask closure domain.
The number 150 therefore must not be reused for the present 57-target
length-12,873 models.

## 6. Necessary-and-sufficient finite CSP

For a profile \(\lambda=(a,b,c)\), take seventeen variables
\(z_{j,i}\in D\), one for each collar position.  Then the profile contains a
universal word if and only if

\[
 \boxed{
 \forall T\in R\ \exists j\in\{1,2,3\},\ I\subseteq[\lambda_j]
 \text{ a nonempty interval}:\quad
 b_T(I)\vee\bigvee_{i\in I}z_{j,i}=T.}                 \tag{6.1}
\]

Necessity follows from Lemma 3.1 and context domination.  Sufficiency follows
because every form in (6.1) is a literal interval, while every target outside
\(R\) retains a fixed-gap witness.  Thus (6.1) is an exact occurrence-level
model, not a target-marginal relaxation.

There is also an exact collar-signature formulation.  Let
\(\mathcal C_j(z_j)\subseteq R\) be the targets served by collar word \(z_j\)
through (6.1).  Feasibility is precisely

\[
              \mathcal C_1(z_1)\cup\mathcal C_2(z_2)
                    \cup\mathcal C_3(z_3)=R.            \tag{6.2}
\]

Each signature family can be generated by a layered finite automaton whose
state is the current suffix-OR spectrum together with the accumulated
57-bit coverage set.  Appending \(z\in D\) sends every suffix OR \(s\) to
\(s\vee z\), adds the singleton suffix \(z\), and records newly hit targets;
the final right-prefix chain closes the boundary forms.  For equal suffix
spectra, a state with smaller coverage is dominated.  Equation (6.2) is the
final three-way union node.  This gives an exact dynamic-programming/flow
alternative, but no enumeration of that automaton is claimed here.

## 7. Exact value-free interval section

The value variables can be eliminated completely after literal witness
intervals are selected.  For every \(T\in R\), choose one collar and one
nonempty local interval \(I_T\) in that collar, with its maximal context
\(b_T(I_T)\) from (4.1).  For a variable position \(p\), put

\[
 \mathcal A(p)=\{T:p\in I_T\},\qquad
 C_p=\bigcap_{T\in\mathcal A(p)}T,                     \tag{7.1}
\]

with \(C_p=\mathtt{ffff}\) when \(\mathcal A(p)=\varnothing\).

### Theorem 7.1 (literal interval-section criterion)

The selected target intervals are simultaneously realizable by nonzero
collar cells if and only if

\[
 C_p\ne0\quad\hbox{for every variable position }p,     \tag{7.2}
\]

and

\[
 \forall T\in R\ \forall e\in T\setminus b_T(I_T)\quad
 \exists p\in I_T:\quad e\in C_p.                     \tag{7.3}
\]

When these conditions hold, set \(z_p=C_p\) at every used position and use
the fixed nonzero sentinel \(\mathtt{0001}\) at an unused position.

#### Proof

Suppose cells \(z_p\) realize the selected witnesses.  If \(p\in I_T\),
then \(z_p\subseteq T\), so \(z_p\subseteq C_p\).  Cell nonzeroness gives
(7.2).  Every bit of \(T\) absent from the fixed context must be supplied by
some variable cell of \(I_T\); that bit then lies in \(C_p\), proving (7.3).

Conversely, set every used cell to \(C_p\).  For \(p\in I_T\), definition
(7.1) gives \(C_p\subseteq T\), so no forbidden bit enters the witness.
Condition (7.3) supplies every bit missing from \(b_T(I_T)\), while the
context supplies the remaining bits.  Hence

\[
 b_T(I_T)\vee\bigvee_{p\in I_T}C_p=T.
\]

Condition (7.2) makes every used cell nonzero, and unused cells meet no
selected witness.  This proves sufficiency.  Moreover every nonzero used
\(C_p\) is an intersection of repair targets and hence belongs to the
245-mask closure domain from Theorem 5.1. \(\square\)

There is an equivalent non-cover form.  For a coordinate \(e\), define

\[
 Z_e=\bigcup_{T:\ e\notin T}I_T.                       \tag{7.4}
\]

Then \(e\in C_p\) exactly when \(p\notin Z_e\), and (7.2)--(7.3) become

\[
 \bigcap_e Z_e=\varnothing,                            \tag{7.5}
\]

and

\[
 I_T\nsubseteq Z_e
 \quad(T\in R,\ e\in T\setminus b_T(I_T)).             \tag{7.6}
\]

Thus the remaining fixed-gap question is a finite interval-section problem,
not a fractional cell-capacity problem.  Bits may be reused at a position;
after interval choices, (7.2)--(7.3) are the complete Hall condition.  Since
the three collars are disjoint, their only coupling is the partition of
targets among them.

### Corollary 7.2 (six exact sunflower tolls)

The repair family contains six single-bit three-petal sunflowers:

\[
\begin{array}{c|ccc}
\text{core}&\multicolumn{3}{c}{\text{targets}}\\ \hline
\mathtt{142d}&\mathtt{146d}&\mathtt{542d}&\mathtt{942d}\\
\mathtt{286d}&\mathtt{287d}&\mathtt{2c6d}&\mathtt{a86d}\\
\mathtt{2879}&\mathtt{287d}&\mathtt{6879}&\mathtt{a879}\\
\mathtt{246d}&\mathtt{2c6d}&\mathtt{346d}&\mathtt{a46d}\\
\mathtt{146d}&\mathtt{346d}&\mathtt{546d}&\mathtt{946d}\\
\mathtt{542d}&\mathtt{546d}&\mathtt{562d}&\mathtt{d42d}
\end{array}
\]

For any displayed target \(T=Q\cup\{e\}\), either its chosen fixed context
already contains the petal bit \(e\), or \(I_T\) has a position outside the
chosen intervals of both sibling petals.  Indeed, both sibling targets omit
\(e\), so their intervals lie in \(Z_e\); (7.6) gives a point of
\(I_T\setminus Z_e\).  This is an exact boundary-context/private-point toll.
If none of the three petal bits is context-supplied, the three witness
intervals have empty triple intersection.  Indeed, three intervals with a
common point are covered by the union of the one with leftmost left endpoint
and the one with rightmost right endpoint, leaving the third no private
point.  If a core bit also is not context-supplied, at least two distinct
variable positions must therefore carry it.  This is coordinatewise core
replication, not a claim of two complete core witnesses.  The six tolls alone
are not asserted to prove profile UNSAT.

### Theorem 7.3 (saturated first-collar curvature fork)

The right-prefix chain of the first fixed gap is

\[
\mathtt{0000},\mathtt{1009},\mathtt{5429},\mathtt{5629},
\mathtt{56a9},\mathtt{56b9},\mathtt{56bd},\mathtt{56bf},
\mathtt{76bf},\mathtt{7ebf},\mathtt{7fbf},\mathtt{7fff}. \tag{7.7}
\]

Call the first collar saturated when three of its suffix variable ORs
\(U_A,U_B,U_C\), together with contexts from (7.7), serve

\[
\begin{aligned}
\mathcal P_A&=\{\mathtt{142d},\mathtt{542d},
                 \mathtt{562d},\mathtt{56ad}\},\\
\mathcal P_B&=\{\mathtt{146d},\mathtt{546d}\},\\
\mathcal P_C&=\{\mathtt{246d},\mathtt{346d},\mathtt{766d}\}.
\end{aligned}                                           \tag{7.8}
\]

Then \(U_C=\mathtt{246d}\), and the physically possible pairs
\((U_A,U_B)\) are exactly

\[
\begin{gathered}
(\mathtt{0424},\mathtt{0464}),\
(\mathtt{0424},\mathtt{0465}),\
(\mathtt{0424},\mathtt{046d}),\\
(\mathtt{0425},\mathtt{0465}),\
(\mathtt{0425},\mathtt{046d}),\
(\mathtt{042d},\mathtt{046d}).                         \tag{7.9}
\end{gathered}
\]

For a width-four first collar, saturation has the following exact fork:

* retaining both \(\mathtt{4879}\) and \(\mathtt{6879}\) exports
  \(\mathtt{2c6d}\);
* serving \(\mathtt{2c6d}\) exports both
  \(\mathtt{4879}\) and \(\mathtt{6879}\).

#### Proof

The four equations in \(\mathcal P_A\) give
\(U_A=\mathtt{0424}\vee s\), \(s\subseteq\mathtt{1009}\);
the two equations in \(\mathcal P_B\) give
\(U_B=\mathtt{0464}\vee t\), \(t\subseteq\mathtt{1009}\);
and \(\mathcal P_C\) forces \(U_C=\mathtt{246d}\).  Suffix ORs form a
chain.  Since \(U_C\) contains \(\mathtt{2000}\) and omits
\(\mathtt{1000}\), comparability removes the optional \(\mathtt{1000}\)
bit and gives \(s,t\subseteq\mathtt{0009}\), \(s\subseteq t\).

Every repair target containing \(\mathtt{0008}\) also contains
\(\mathtt{0001}\).  The same implication holds in every closure-domain cell
and in every OR of such cells.  Hence the formal cores \(\mathtt{042c}\)
and \(\mathtt{046c}\) are physically impossible.  The remaining choices
\(s,t\in\{0,1,9\}\), \(s\subseteq t\), give exactly (7.9).  They are all
realized, reading cells from the boundary outward, by

\[
\begin{gathered}
(0424,0060,2069),\ (0424,0061,2069),\
(0424,0069,2069),\\
(0425,0060,2069),\ (0425,0069,2069),\
(042d,0060,2069).
\end{gathered}
\]

If the width-four collar also serves any of
\(\{\mathtt{2c6d},\mathtt{4879},\mathtt{6879}\}\), then the three strict
packet cores occupy its inner three suffix levels; otherwise \(U_C\) would
be the full collar OR, which contains neither the required
\(\mathtt{0800}\) nor \(\mathtt{4000}\) bit.  The sole outer cell is
therefore the only possible source of either bit.  The three targets have no
nonzero fixed context.  A \(\mathtt{2c6d}\) witness forces the outer cell to
contain \(\mathtt{0800}\) and omit \(\mathtt{4000}\), while a
\(\mathtt{4879}\) or \(\mathtt{6879}\) witness forces the outer cell to
contain both \(\mathtt{0800}\) and \(\mathtt{4000}\).
This proves the fork. \(\square\)

The fork is sharp.  The D-valued collars

\[
(\mathtt{4879},\mathtt{2069},\mathtt{0065},\mathtt{0424})
\quad\hbox{and}\quad
(\mathtt{0860},\mathtt{2069},\mathtt{0065},\mathtt{0424})
\]

both serve all nine rows in (7.8).  The first additionally serves
\(\mathtt{4879},\mathtt{6879}\) and the second serves
\(\mathtt{286d},\mathtt{2c6d}\); each covers exactly eleven repair rows.
A global completion may escape by moving one packet or the exported debt to
another collar, so this is not profile UNSAT.

### Theorem 7.4 (sharp three-cell terminal-collar bound)

Let

\[
\begin{split}
\mathcal S_C=\{&
\mathtt{8c62},\mathtt{8c67},\mathtt{8ce6},\mathtt{8ce7},
\mathtt{9ce6},\mathtt{bcef},\\
&\mathtt{cc61},\mathtt{cc63},\mathtt{cc67},\mathtt{cce7},
\mathtt{ce61},\mathtt{ce63}\}.
\end{split}                                             \tag{7.10}
\]

Every three-cell terminal collar covers at most ten members of
\(\mathcal S_C\).  Equality is attained by

\[
(\mathtt{8c62},\mathtt{0003},\mathtt{cc61}).            \tag{7.11}
\]

Consequently every \((5,9,3)\) completion must migrate at least two of these
twelve canonical targets to the first or middle collar.

#### Proof

The left suffix-context chain at the terminal collar is

\[
\mathtt{0000},\mathtt{8c44},\mathtt{8cc6},\mathtt{9cc6},
\mathtt{bcc6},\mathtt{bcce},\mathtt{bdce},\mathtt{bfce},
\mathtt{ffce},\mathtt{ffde},\mathtt{fffe},\mathtt{ffff}. \tag{7.12}
\]

For a variable prefix OR \(u\), let \(P(u)\) be the targets in
\(\mathcal S_C\) completed by their maximal context.  If the three cells are
\(x_0,x_1,x_2\), their coverage of \(\mathcal S_C\) is exactly

\[
\begin{split}
P(x_0)\cup P(x_0\vee x_1)\cup P(x_0\vee x_1\vee x_2)\\
\cup\bigl(\mathcal S_C\cap
\{x_1,x_2,x_1\vee x_2\}\bigr).                         \tag{7.13}
\end{split}
\]

Every prefix packet has size at most three.  The only three-target packet
boxes are

\[
\begin{array}{c|c}
\{\mathtt{8c62},\mathtt{8ce6},\mathtt{9ce6}\}
  &u=\mathtt{8c62}\\
\{\mathtt{8c67},\mathtt{8ce7},\mathtt{bcef}\}
  &\mathtt{0023}\subseteq u\subseteq\mathtt{8c67}\\
\{\mathtt{cc63},\mathtt{cc67},\mathtt{cce7}\}
  &u=\mathtt{cc63}.
\end{array}                                             \tag{7.14}
\]

Thus the three nested prefix ORs cover nine distinct targets only for

\[
\mathtt{8c62}\subset\mathtt{8c63}\subset\mathtt{cc63}. \tag{7.15}
\]

In that case the three context-free interior forms add only
\(\mathtt{cc61}\) beyond those nine targets, giving ten.  If all three
interior forms are distinct members of \(\mathcal S_C\), the exact
unordered-OR table has twelve rows; direct substitution in (7.13) gives
respective total maxima

\[
8,7,6,9,9,8,7,6,8,7,7,8,
\]

so this case gives at most nine.  In every other case the interior forms add
at most two; if the prefix part gives at most eight the total is at most ten,
and the nine-prefix case was already handled.  This proves the bound.
Substitution of (7.11) gives the nine packets in (7.14) plus
\(\mathtt{cc61}\), so the bound is sharp. \(\square\)

This is a bound for the fixed twelve-row family (7.10), not all 57 repair
targets: for example \((\mathtt{8c62},\mathtt{0841},\mathtt{c421})\)
covers eleven repair targets overall.

### Lemma 7.5 (anchor localization)

All 57 repair targets omit coordinate bit 8.  Exactly
\(E=\mathtt{8000}\) and \(N=\mathtt{9009}\) omit bit 5.  The target \(E\)
has zero context at every interface, so its witness interval consists only
of cells equal to \(\mathtt{8000}\); all eighteen bit-15-free target
intervals are disjoint from it.  Outside \(I_E\cup I_N\), condition (7.2)
is automatic from common bit 5.  On \(I_N\setminus I_E\), it reduces
exactly to

\[
(I_N\setminus I_E)\cap Z_0\cap Z_3\cap Z_{12}\cap Z_{15}
=\varnothing.                                          \tag{7.16}
\]

These finite claims, the 115 context-signature types, the three ledger
hashes, and Theorem 7.4 have an independent solver-free replay:

\[
\begin{array}{ll}
\text{script SHA-256}&
\mathtt{41664c00d922bf4da47880c299568118ba00e9dda794043b50750222d6ca52bb},\\
\text{audit SHA-256}&
\mathtt{768964f4539792ce7b358d867453062a3c6711d292c344e72760df126ee02eb8},\\
\text{payload SHA-256}&
\mathtt{f887d435b39d062182648d3deae76aee453d5577511c573b0ca61cd8b29cf54f}.
\end{array}
\]

## 8. Compact exact CNFs

Introduce sixteen bit variables per collar cell and one selector
\(w_{T,I}\) for each undominated pair \((T,I)\).  For every selector impose:

* `not w OR not z_(i,q)` for every \(i\in I\) and bit \(q\notin T\);
* `not w OR OR_(i in I) z_(i,q)` for every bit
  \(q\in T\setminus b_T(I)\).

One at-least-one selector row is imposed for each target, and the 257
closure-domain clauses are copied to each cell.  That domain CNF already
contains the cell-nonzero clause, so a duplicate standalone copy is omitted.
Lemma 4.1 and Theorem 5.1 prove equisatisfiability.

After eliminating dominated physical contexts, the exact dimensions are:

| profile | local forms | variables | base clauses, including 17 nonzero rows | closure-domain clauses, including those same 17 rows | total after replacing the 17 rows |
|---|---:|---:|---:|---:|---:|
| `(4,9,4)` | 65 | 3,977 | 120,206 | 4,369 | 124,558 |
| `(5,8,4)` | 61 | 3,749 | 104,916 | 4,369 | 109,268 |
| `(5,9,3)` | 66 | 4,034 | 122,849 | 4,369 | 127,201 |

Thus the last column is `base + closure - 17`, not the sum of the two
preceding columns: the closure-domain CNF replaces, rather than duplicates,
the standalone nonzero row at each of the seventeen cells.

These are the dimensions of the compact direct scheme having one selector
per target and undominated local variable interval.  No CNF-size minimality
claim is made.

The older raw `(4,9,4)` emitter retains every compatible fixed-context form:
4,739 variables and 145,704 clauses.  Context domination reduces its 4,467
physical context terms to 3,705 exact local forms before the closure clauses
are added.  The generated raw CNF has SHA-256
`206581940afea13d9be331cf4d44f028dda9f79c7ffc705dea3dd2a1c928cf80`;
this identifies the live finite model but supplies no verdict.

## 9. Exact operational status

The pre-existing H100 CaDiCaL process on the raw `(4,9,4)` CNF ended at its
wall-clock limit with exit code `124`.  It left a `1,662,013,440`-byte partial
DRAT stream and zero-byte stdout/stderr; an interrupted proof stream is not
an UNSAT certificate.  A separate capped CP-SAT process disappeared with
zero-byte stdout/resource logs, no audit JSON, and no exit-status file.  The
kernel journal contained no OOM or segfault record.  A later full CP-SAT
attempt on the same raw `(4,9,4)` model also hit its outer 3,600-second
timeout with exit `124`, 88,560 KiB peak RSS, empty stdout/stderr, and no
audit JSON or candidate.  All attempts therefore have proof-safe status
**UNKNOWN**, not UNSAT.

The retained CP-SAT timeout ledger has SHA-256
`612cbeccec26e755416902486f55e2f05157f74024eef923cc80ed749c6ce488`;
its driver and pinned map have SHA-256 values
`6bc2e6559d1221942dd1bc3a0fa1a5a66c3a1f570bf6e2f63f37db6aeb6fe97e`
and
`914c4bd9758e710d8cd9a832e9c90f4feabf380b8cb4732fd4132fc7ba9e556e`.

No additional remote job was launched by Lane K during this proof work:
`/dev/shm` had only about 1.9 GiB free and swap was fully used.  A future
run should use a persistent detached
wrapper, a private non-`/dev/shm` proof path if DRAT growth is expected, and
must retain its exact command, resource cap, exit code, model hash, and
decoded full-word replay.

## 10. Scope and remaining boundary

SAT plus literal replay for any one of the three profiles proves
\(\nu(16)=12873\).  Proof-checked UNSAT for all three closes exactly the
fixed-gap shortening class (2.1).  It does not close:

* deletion or rethreading of a fixed-gap cell;
* movement of a full separator;
* a braid mixing cells across a fixed gap;
* arbitrary length-12,873 words; or
* the all-\(k\) GCR/PAPC existence theorem.

Thus the finite collar problem is now an exact 17-variable, 57-row CSP.  The
general shadow-braid problem begins precisely when one changes a fixed gap or
routes through it; that operation lies outside the decomposed product
language (6.2).

## 11. Frozen solver-free audit

```text
scratch/audit_k16_12873_three_profile_closure_model_20260730.py
SHA-256 29b4b252b3014abf7e9f0c28747b2ffdd02636f73ace645985794d5f0034b7d2

scratch/k16_12873_three_profile_closure_model_20260730.audit.json
SHA-256 2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892
payload SHA-256 d33f79a5dbbc002471828cd286a482609b5780ec032daf13dc966f58252c0b47
```

The audit is solver-free.  It reconstructs the common repair family,
exhausts the closure implication over every nonzero mask and every repair
target, truth-table checks the domain CNF, proves unique context maxima for
every target/local interval, and recomputes every displayed model dimension.
