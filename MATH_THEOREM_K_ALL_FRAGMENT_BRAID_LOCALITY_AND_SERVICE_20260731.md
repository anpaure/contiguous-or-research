# Fragment braids: exact endpoint locality and the remaining global routing gate

Date: 2026-07-31.

This note isolates the part of the construction which remains after the
all-depth PBBS factor and the deadline-staircase theorem.  Its point is not
to assert that a good braid always exists.  It proves that every effect of a
cut and seam has finite endpoint support, and that the residual global
problem is exactly one decorated directed path-cover problem.

Throughout, the carrier vertices are rank-\(r\) subsets of \([k]\).  A
**fragment** is an oriented finite sequence

\[
                         P=(P_0,\ldots,P_{a-1}).
\]

It may have been cut from a cyclic Johnson factor, but none of the first two
lemmas needs that assumption.

## 1. Exact seam service

Define the distinct prefix- and suffix-OR chains

\[
 \operatorname{Pre}(P)=
  \left\{\bigcup_{i=0}^jP_i:0\le j<a\right\},\qquad
 \operatorname{Suf}(P)=
  \left\{\bigcup_{i=j}^{a-1}P_i:0\le j<a\right\}.
\tag{1.1}
\]

### Lemma 1.1 (suffix--prefix seam identity)

After concatenating exactly two fragments \(P|Q\), the interval unions
which use vertices on both sides of their seam are exactly

\[
 \boxed{
 \operatorname{Gain}(P,Q)=
   \{S\cup R:S\in\operatorname{Suf}(P),\ R\in\operatorname{Pre}(Q)\}.}
\tag{1.2}
\]

Moreover,

\[
 |\operatorname{Pre}(P)|,|\operatorname{Suf}(P)|\le k-r+1,
 \qquad
 |\operatorname{Gain}(P,Q)|\le(k-r+1)^2.
\tag{1.3}
\]

#### Proof

An interval crossing the seam is uniquely a suffix of \(P\) followed by a
prefix of \(Q\), proving (1.2).  Along either chain, every strict change
increases rank by at least one.  It starts at rank \(r\) and ends no later
than rank \(k\), proving (1.3). \(\square\)

Thus one seam can have a large number of physical witnesses but only
\(O(k^2)\) distinct upper values.  In particular, if a braid must create
\(H\) targets absent from all retained fragment interiors, then it needs at
least

\[
                    \left\lceil H/(k-r+1)^2\right\rceil
\tag{1.4}
\]

service seams.  This is only a capacity bound; simultaneous compatibility is
the real issue.

### Lemma 1.2 (complete multi-fragment interval formula)

For an ordered braid \(F_1|\cdots|F_b\), every interval union is either
internal to one fragment or has the unique form

\[
 S\cup V(F_{a+1})\cup\cdots\cup V(F_{c-1})\cup P,
 \tag{1.5}
\]

where \(a<c\), \(S\in\operatorname{Suf}(F_a)\),
\(P\in\operatorname{Pre}(F_c)\), and
\(V(F)=\bigcup_{X\in F}X\).  In particular, if every fragment has full OR
\([k]\), every proper upper target crosses at most one seam.

#### Proof

An interval beginning in \(F_a\) and ending in \(F_c\) contains a suffix of
the first fragment, every intermediate fragment in full, and a prefix of the
last.  This proves (1.5), and the final assertion is immediate. \(\square\)

### Lemma 1.3 (unconstrained owner-pair abundance)

Let \(Z\) have rank \(r+t\), \(0\le t\le r-1\).  The number of ordered
pairs \((A,B)\in\binom Zr^2\) with \(A\cup B=Z\) is

\[
 \boxed{
                  \binom{r+t}{t}\binom rt.}
\tag{1.6}
\]

#### Proof

Choose \(A\) in \(\binom{r+t}{r}\) ways.  The set \(B\) must contain the
\(t\) elements of \(Z\setminus A\), and its remaining \(r-t\) elements may
be chosen from \(A\) in \(\binom r{r-t}=\binom rt\) ways. \(\square\)

For \(t=1\), every such pair is a Johnson seam.  For \(t>1\), (1.6) is an
abundance statement only: most singleton-owner pairs are not Johnson and
cannot all be used without spending lower-palette debt.  Retained suffix and
prefix chains are what convert this raw abundance into legal deep service.

## 2. Exact cut and lower-colour ledgers

Suppose the fragments are cut from a cyclic lower-rainbow Johnson factor.
For an edge or seam \(e=UV\), write \(L(e)=U\cap V\) and
\(U(e)=U\cup V\).  The lower colour \(L(e)\) is a rank-\((r-1)\) colour
only when \(|U\triangle V|=2\).

### Lemma 2.1 (lower-palette balance)

Let \({\cal C}\) be the multiset of colours on all cut factor edges and let
\({\cal S}\) be the multiset of colours on all Johnson seams.  Relative to
the original exact lower palette, the final linear chronology has net
lower-colour change

\[
                            -{\cal C}+{\cal S}.
\tag{2.1}
\]

Hence exact restitution is precisely multiset equality after accounting for
the deliberately exposed boundary colours.  A non-Johnson seam supplies no
rank-\((r-1)\) adjacency colour and must be paid by the compiler or by an
explicit defect.

#### Proof

All retained internal adjacencies are unchanged.  The only deleted
adjacencies are the cuts and the only new adjacencies are the seams.  Taking
their intersections proves (2.1). \(\square\)

Suppose \(b\) source edges were cut and \(j\) of the \(b-1\) seams are
Johnson.  Put

\[
 H=\#\{C:\mu^-_{\rm new}(C)=0\},\qquad
 E=\sum_C(\mu^-_{\rm new}(C)-1)^+.
\]

The final chronology has \(W-b+j\) rank-\((r-1)\) adjacency occurrences,
so summing \(\mu^-_{\rm new}(C)-1\) over all colours gives

\[
                         \boxed{H-E=b-j.}
\tag{2.2}
\]

In particular, if every seam is Johnson then \(H=E+1\).  The braid has the
single forced boundary hole exactly when its seam colours are distinct and
recycle \(b-1\) of the \(b\) deleted colours.  Thus arbitrarily many
fragments need not cost arbitrarily many lower colours.

For immediate upper edge colours, the equally exact identity is

\[
 \mu^{+,\mathrm{edge}}_{\rm new}(Z)
 =\mu^{+,\mathrm{edge}}_{\rm old}(Z)
  -\#\{\text{cut }e:U(e)=Z\}
  +\#\{\text{Johnson seam }e:U(e)=Z\}.
\tag{2.3}
\]

For an upper target \(Z\) on a cyclic component \(Q\), define its cut kernel

\[
 B_Q(Z)=\bigcap\{E(I): I\text{ is a cyclic witness interval for }Z\}.
\tag{2.4}
\]

A cut destroys all old witnesses of \(Z\) iff it belongs to \(B_Q(Z)\).
Thus the old-target loss vector and the new-target gain vector (1.2) are both
exact endpoint data.

## 3. Run-state locality

For a binary word \(w\), let \(R_d(w)\) record

* its length and whether it is all ones;
* its positive prefix and suffix lengths, capped at \(d+1\);
* for every \(1\le t\le d\), the latest zero-based start
  \(\rho_t(w)\) of an internal positive run of length at most \(t\), or
  zero if none exists.

For a set-valued fragment \(P\), take the product of these summaries over
the \(k\) coordinate traces.

### Lemma 3.1 (finite-dimensional run monoid)

There is an associative composition rule

\[
                         R_d(uv)=R_d(u)\star R_d(v)
\tag{3.1}
\]

depending only on \(R_d(u)\) and \(R_d(v)\).  In particular, concatenating
two fragments changes only the terminal run of the left trace and the
initial run of the right trace for each coordinate.  The latest-start vector
of every newly completed short run is determined by the endpoint summaries.

#### Proof

If the boundary bits differ, a positive boundary run becomes internal on
the appropriate side.  If both boundary bits are one, merge the two lengths,
cap at \(d+1\), and decide whether it remains a prefix or suffix using the
all-one flags.  Existing internal latest starts are inherited, with the
right-hand starts translated by \(|u|\).  Taking the maximum with the one
new boundary candidate gives every \(\rho_t(uv)\).  These are exactly the
usual run-decomposition rules, hence associative. \(\square\)

For a complete carrier chronology \(T\), apply this summary to every
coordinate trace \(T^{(x)}\).  The terminal-start staircase debt has the
compact exact form

\[
 \boxed{
 \mathfrak D_d(T)=
   \sum_{t=1}^d\max_{x\in[k]}\rho_t(T^{(x)}).}
\tag{3.2}
\]

This is the latest-run formulation of Theorem 3.3 in the deadline-staircase
note.

The flat minimum-residence test is therefore a finite-dimensional path
constraint.
For the actual non-flat problem, augment the summary by the translated list
of short-run positions.  Concatenation retains the two old lists and creates
at most one new boundary run per coordinate, so this augmented replay is
still endpoint-local although its output list is not finite-state.  Feed the
final event list to the exact threshold optimizer in Theorem 3.4 of
`MATH_THEORY_K_ALL_DEADLINE_STAIRCASE_NORMAL_FORM_AND_O1_20260731.md`.
No motif score or support cardinality is a substitute for that replay.

For an arbitrary-start schedule, each internal short run \((a,\ell)\) gives
the exact particle constraint

\[
 \#\{t:H_t\le a-1\}-\#\{t:G_t\le a+\ell\}\le\ell-1.
\tag{3.3}
\]

Old constraints persist under concatenation and each seam creates or
destroys at most one boundary run per coordinate.

## 4. The protected fragment-braid reduction

Take a catalogue of candidate fragment cuts and orientations.  Form a
directed arc \(P\to Q\) for every permitted seam, decorated by

1. its lower colour, or the flag that it is non-Johnson;
2. its one-seam upper gain set (1.2), together with each fragment's full OR
   for the multi-fragment formula (1.5);
3. its run-state composition (3.1);
4. every retained suffix/prefix edge span needed by a chosen witness.

### Theorem 4.1 (exact braid CSP)

A braid using the catalogue is equivalent to a directed path cover with the
following side constraints:

1. every chosen fragment has at most one predecessor and successor, and the
   selected arcs form the desired number of linear paths;
2. the cut/seam colour ledger (2.1) leaves only the lower defects assigned to
   the boundary/compiler budget;
3. for every required upper target, either a retained internal witness or at
   least one protected witness from the complete formula (1.5) survives;
   choosing such a witness forces every edge in its endpoint suffix/prefix
   spans and every intervening fragment to be retained in the displayed
   order;
4. the composed run traces admit thresholds \((G,H)\) satisfying (1.8),
   (1.12), and the exact loss budget (1.10);
5. the resulting staircase passes the common-cap criterion.

If the cut/orientation catalogue and the witness catalogue are exhaustive,
every condition is necessary and sufficient.  Restricting the witness bank
to one-seam witnesses is always sound, and is complete for proper targets
when every selected fragment has full OR.
The only nonlocal combinatorics before the common cap is the directed path
cover/order; every palette and residence effect is an exact local label or a
protected finite span.

#### Proof

Condition 1 is the definition of a fragment braid.  Lemma 2.1 proves the
lower ledger.  Lemmas 1.1--1.2 list all and only cross-fragment upper
witnesses, while
the implication from a selected witness to its retained spans prevents a
later cut from invalidating it.  Lemma 3.1 plus the staircase theorems gives
the exact residence and scalar schedule test.  The common-cap theorem is
necessary and sufficient after the chronology and supports are fixed.
Reversing these implications constructs the braid and its word. \(\square\)

This theorem explains why an ordinary flow is not yet the whole answer.
Once witness choices are fixed, the degree part is a path-cover flow.  Before
that fixing, each target contributes an OR of protected seam-and-span
witnesses, so the problem is a path cover with set-cover side constraints.

## 5. The current \(k=17\) evidence

For the retained 11-component exact-\(q_1\) factor:

* there are 1,838 missing deep targets;
* all 1,838 have cross-component endpoint-state providers;
* after restricting to Johnson seams and forbidding newly completed runs of
  lengths one and two, every hole still has at least 33 cross-component
  providers and at least 82 providers in total;
* one such seam serves at most five of the current holes, so at least 368
  service seams are needed;
* merely maximizing Johnson-compatible seams is insufficient: an audited
  4,643-fragment braid with 4,604 Johnson joins still creates
  \(833,1538,1623\) runs of lengths \(1,2,3\), respectively, and loses
  thousands of palette values.

The provider census removes a genuine possible obstruction: no deep target
is locally stranded.  It does not prove a simultaneous path cover.  The
remaining finite gate is exactly Theorem 4.1, with all coordinate run ages,
lower-colour restitution, and protected suffix/prefix spans carried on the
arcs.

In fact the census already proves a nontrivial simultaneous statement.  Form
the bipartite graph between the 1,838 holes and their run-safe Johnson seam
providers.  Every hole has degree at least 82 and every provider arc serves
at most five holes.  For every hole family \({\cal A}\), double counting its
incident pairs gives

\[
       82|{\cal A}|\le e({\cal A},N({\cal A}))
          \le5|N({\cal A})|.
\]

Thus Hall's condition holds with factor \(82/5\), and there is an injective
assignment of a **distinct** safe Johnson seam provider to every deep hole.
What remains is stronger than service Hall: the chosen arcs must also have
compatible endpoints, form one path cover, recycle the q1 colours, protect
their retained spans, and satisfy the global staircase/common cap.

The current CP-SAT lane is a sound sufficient restriction, not yet the exact
master of Theorem 4.1: it uses one-seam witnesses, protects unique immediate
upper providers individually, enforces only the first run-safety filters,
and searches a cyclic path-cover scaffold.  A positive literal replay is
valid; a negative verdict would exclude only that restricted catalogue.

Audit anchors:

* safe-provider audit payload
  `8dfbf031458356aaaf9eb95a1c72cc4d303dd1167437a1383759ec08a044c97f`
  (audit SHA-256
  `09c9ad092035fce5c222d63923b1cd2f33af3c7b65099fa0f7ea7afcdd30f308`);
* Johnson-only negative-braid audit SHA-256
  `d55f4c3c2cf50dde836d6286e4bb5856cade6af030368e247895a4adc26a34ff`;
* exact staircase/braid audit note
  `MATH_AUDIT_K17_COMPONENT_BRAID_EXACT_STAIRCASE_20260731.md`, SHA-256
  `a38acafe48b30d245ab7e89a06a6baa93f48b3683478dec25b5ef531a347dbbc`.

## 6. Consequence for the all-\(k\) program

The construction problem is now separated into two statements of genuinely
different character.

1. **Local service abundance:** every required target and palette colour has
   many endpoint-compatible protected witnesses.  This is proved at the
   current \(k=17\) state and is a plausible all-dimensional counting
   theorem.
2. **Global decorated routing:** select those witnesses in one path cover
   whose run trace has staircase loss within slack and whose lower labels
   recycle.  This is the missing correlation theorem.

Proving a uniform Hall/absorption theorem for the decorated path-cover in
Theorem 4.1 would establish the protected staircase conjecture and hence
\(\nu(k)=B(k)+O(1)\).  Requiring zero residual defects would give the exact
formula.
