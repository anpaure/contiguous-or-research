# CPCR, MWB, the exact one-sided residual, and the (q=1) saturating-cycle interface

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The load-theoretic hierarchy is correct, with one scope qualification:
all three functionals must be evaluated on the **same load vector and the
same total mass**.  For such a system,

\[
 \boxed{
 \mathrm{CPCR}\Longrightarrow\mathrm{MWB}
 \Longrightarrow\mathrm{missing\ shadows}.}                   \tag{0.1}
\]

Both converses fail already for elementary integer load vectors.  The
counterexamples are algebraic; they do not by themselves assert that the
displayed vectors occur in the restricted compiler orbit.

The diverse-packet CPCR statement uses retained mass \(G\), whereas the
original MWB theorem was stated for a full exact factor of mass \(W\).
Thus CPCR literally implies the \(G\)-quota analogue of MWB.  It implies
the original \(W\)-quota MWB after any compatible completion whose added
mass is \(W-G\), at an extra \(O(H(W-G))=o(W)\) cost; the existence of
that completion is a separate structural issue.  The constant-one
transfer avoids it by appending the leave literally.

The weakest exact direct residual used by that transfer is

\[
 \boxed{
 \mathfrak H=
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}\sum_T
                    (1-L_q^\epsilon(T))_+=o(W).}               \tag{0.2}
\]

For integer loads this is exactly the total number of missing physical
targets.  It imposes no charge at all on a positive load, however large.
Given the proved owner-leave estimate, it is equivalently the linear
repeat excess above the forced cardinality baseline.  A capped upper-tail
surrogate is not equivalent.

For the newest **complement-equivariant fused compiler**, this simplifies
further.  Its occurrencewise identity

\[
                         U_q(X^c)=L_q(X)^c                       \tag{0.2a}
\]

gives \(M_q^+=M_q^-\).  Hence the weakest residual in that specific base
is genuinely one-sided:

\[
 \boxed{
 \mathfrak H^-=
 \sum_{q\le H}\sum_T(1-L_q^-(T))_+=o(W).}                     \tag{0.2b}
\]

The two-sign expression (0.2) is the correct statement without fused
complement symmetry.

The published two-level saturating cycle gives an exact and useful
\(q=1\) result:

* one long Johnson owner cycle covers every lower \((m-1)\)-target exactly
  once while using \(N_1\) distinct middle owners;
* the omitted \(W-N_1=O(W/m)\) owners may be appended literally;
* therefore it closes the **one-sided lower \(q=1\)** transfer with total
  length \(W+O(1)\), and its leave/component scale is
  \(o(W/H)\) whenever \(H=o(m)\).

It does **not** close the two-sided \(q=1\) transfer.  The theorem gives no
near-rainbow statement for the upper unions.  It also gives no
depth-\(q>1\) safety.  A one-facet Hall assignment does insert every
omitted owner into a Hamilton **Johnson** cycle and makes the lower edge
color histogram balanced.  But at each inserted owner the two incident
intersection facets are equal, so their union does not recover that owner.
Thus this Hamilton cycle is not directly compatible with the
distinct-facet lower-word compiler.  The safe transfer use is to retain
the original saturating core and append omitted owners literally.

## 1. One-load ledger

Fix one signed depth.  Let \(N\) be the number of targets, \(G\) the
number of occurrences, and

\[
 L(T)\in\mathbb Z_{\ge0},\qquad \sum_TL(T)=G.                  \tag{1.1}
\]

Put

\[
 c=\left\lfloor{G\over N}\right\rfloor,
\]

\[
 D^- =\sum_T(c-L(T))_+,qquad
 D^+ =\sum_T(L(T)-c-1)_+,                                    \tag{1.2}
\]

and

\[
 O=\max\{D^-,D^+\}.                                           \tag{1.3}
\]

This is the exact balanced-quota overload.  The CPCR energy is

\[
 \Phi=\sum_T(L(T)-c)(L(T)-c-1).                               \tag{1.4}
\]

### Theorem 1.1 (CPCR implies MWB)

For every integer load vector,

\[
                         2O\le\Phi.                            \tag{1.5}
\]

Consequently, if \(c\ge1\),

\[
                         {O\over c}\le{\Phi\over2}.           \tag{1.6}
\]

Thus aggregate CPCR \(o(W)\) implies aggregate MWB \(o(W)\) on the
same load system.

#### Proof

For an integer \(x\),

\[
 (x-c)(x-c-1)
 \ge2(c-x)_++2(x-c-1)_+.                                     \tag{1.7}
\]

Summing gives \(\Phi\ge2(D^-+D^+)\ge2O\). \(\square\)

### Theorem 1.2 (MWB implies missing shadows)

Let \(M=\#\{T:L(T)=0\}\).  Then

\[
                         M\le {D^-\over c}\le{O\over c}.      \tag{1.8}
\]

#### Proof

Every missing target contributes exactly \(c\) to \(D^-\). \(\square\)

Summing Theorems 1.1--1.2 over depths and signs proves (0.1).

## 2. Both algebraic converses fail

### Counterexample 2.1 (missing shadows do not imply MWB)

Let \(N\) be even, \(G=2N\), and \(c=2\).  Give half the targets load
one and half load three.  Then every target is covered, but

\[
                    D^-={N\over2},\qquad D^+=0,qquad
                    {O\over c}={N\over4}.                      \tag{2.1}
\]

Thus the missing cost is zero and the MWB cost is linear.

### Counterexample 2.2 (MWB does not imply CPCR)

Fix any constant \(c\ge1\), put \(G=cN\), and let
\(k=\lfloor\sqrt N\rfloor\).  Give

* \(k\) targets load \(c-1\);
* one target load \(c+k\); and
* every other target load \(c\).

The total load is \(G\).  Moreover,

\[
 D^-=k,qquad D^+=k-1,qquad O=k=o(N),                         \tag{2.2}
\]

whereas

\[
 \Phi=2k+k(k-1)=\Theta(N).                                    \tag{2.3}
\]

For \(c\ge2\), this example has no missing targets at all.  Thus even
MWB plus perfect coverage does not imply CPCR.

These examples separate the numerical load conditions.  A nonconverse
inside the literal compiler state space would additionally require a
reachable state having the displayed degree pattern.

## 3. Retained mass versus full mass

The previous section compares functionals at fixed total mass.  The
following elementary stability lemma handles a completed owner leave.

### Lemma 3.1 (balanced-vector extension)

Let \(L^G\) have total mass \(G\), let \(a\ge0\) have total mass
\(s=W-G\), and put \(L^W=L^G+a\).  If \(O_G,O_W\) are the balanced
overloads at totals \(G,W\), respectively, then

\[
                         O_W\le O_G+s.                          \tag{3.1}
\]

#### Proof

Choose a balanced integer vector \(b_G\) minimizing the \(L^1\) distance
to \(L^G\), so \(\|L^G-b_G\|_1=2O_G\).  Starting from \(b_G\), add one
unit at a time to a currently minimum coordinate.  After \(s\) additions
this gives a balanced vector \(b_W\) of mass \(W\), with

\[
                         \|b_W-b_G\|_1=s.
\]

Since \(\|a\|_1=s\),

\[
 \|L^W-b_W\|_1
 \le\|L^G-b_G\|_1+\|a-(b_W-b_G)\|_1
 \le2O_G+2s.
\]

Divide by two. \(\square\)

Thus any compatible full completion costs at most \(W-G\) extra overload
per signed depth.  Under \(H(W-G)=o(W)\), retained CPCR implies full MWB
after such a completion.  Without a compatible completion, the original
exact-factor MWB statement and retained-packet CPCR are different types
of assertions; the direct missing-mask transfer needs no completion.

## 4. The exact weakest one-sided residual

For integer \(L\),

\[
                         (1-L)_+=\mathbf1_{\{L=0\}}.            \tag{4.1}
\]

Hence (0.2) is literally the aggregate missing-target count.  It is
necessary and sufficient at the physical-load level for the step which
appends every missing target once.

For one signed depth define

\[
 E=\sum_T(L(T)-1)_+,qquad
 F=(N-G)_+,qquad
 X=E-(G-N)_+.                                                  \tag{4.2}
\]

If \(U=\{T:L(T)>0\}\), then

\[
 E=G-|U|,qquad M=N-|U|,qquad M=N-G+E.                        \tag{4.3}
\]

Therefore

\[
                         M=F+X,                                \tag{4.4}
\]

and both \(F,X\) are nonnegative.  If the owner leave obeys
\(H(W-G)=o(W)\), then \(\sum F=o(W)\), so

\[
 \sum M=o(W)\quad\Longleftrightarrow\quad\sum X=o(W).         \tag{4.5}
\]

This is the exact repeat-excess reformulation.  Every overload unit must
be retained in \(E\): one target of load \(\Theta(W)\) can account for
\(\Theta(W)\) holes.  By contrast, when (0.2) is attacked directly, the
entire positive tail may be ignored.

The phrase ``weakest separable functional'' should be read with the
natural normalization that a missing coordinate costs one and all
covered coordinates may cost zero.  Under that normalization, (4.1) is
pointwise minimal.  Without a normalization, scalar rescalings make the
word ``weakest'' meaningless.

## 5. What the two-level saturating cycle proves

Let \(n=2m+1\) and

\[
 W=\binom nm,qquad
 N_1=\binom n{m-1}={m\over m+2}W.                             \tag{5.1}
\]

The two-level saturating-cycle theorem gives a simple alternating cycle

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N_1-1},X_{N_1-1},R_0,              \tag{5.2}
\]

which visits every \((m-1)\)-set \(R_i\) and \(N_1\) distinct middle
owners \(X_i\).  Necessarily

\[
                         X_i=R_i\cup R_{i+1}.                  \tag{5.3}
\]

Therefore the cyclic word

\[
                         R_0,R_1,\ldots,R_{N_1-1}              \tag{5.4}
\]

realizes every lower \(q=1\) target as a one-entry mask and every used
middle owner as a two-entry union, with no lower target missing.

The omitted middle owners number

\[
                         W-N_1={2W\over m+2}=O(W/m).            \tag{5.5}
\]

Append each omitted owner literally.  After repeating the first entry to
linearize (5.4), the total length is

\[
                         N_1+(W-N_1)+O(1)=W+O(1).              \tag{5.6}
\]

This proves the one-sided lower \(q=1\) constant-one interface directly.
If the omitted owners are instead counted as singleton owner components,

\[
                         1+(W-N_1)=o(W/H)                      \tag{5.7}
\]

whenever \(H=o(m)\).

The even-ground calculation is identical with

\[
 N_1=\binom{2m}{m-1}={m\over m+1}W,qquad
 W-N_1={W\over m+1}.                                          \tag{5.8}
\]

## 6. Why this is not the full (q=1) transfer

The upper colors of the projected middle-owner cycle are

\[
                         U_i=X_{i-1}\cup X_i.                  \tag{6.1}
\]

The saturating-cycle theorem supplies no bound on their collisions or
holes.  Thus it proves

\[
                         \mathfrak H_1^-=0,                    \tag{6.2}
\]

but not \(\mathfrak H_1^+=o(W)\).  Using independently a saturating cycle
on the opposite two levels pays the middle baseline twice and does not
give coefficient one.

Accordingly, after this lower saturating core is adopted, the weakest
remaining \(q=1\) residual is simply

\[
                         \mathfrak H_1^+
 =\#\{\text{missing upper unions }X_{i-1}\cup X_i\}=o(W).      \tag{6.2a}
\]

No lower multiplicity or quadratic penalty remains at this depth.

Nor does (5.2) imply the FIFO/tight-window condition required at
\(q\ge2\).  A general Johnson cycle may delete a recently inserted
coordinate or reinsert a recently deleted one.

There is also an interface qualification for the full-owner insertion.  A
Hall assignment of an omitted owner \(Y\) to one lower facet \(R\subset Y\)
does give a Hamilton Johnson cycle with a balanced lower edge-color
histogram: insert \(Y\) into the old edge

\[
                         X_{i-1}-X_i,qquad
 X_{i-1}\cap X_i=R,                                            \tag{6.3}
\]

creates the two intersections

\[
                         X_{i-1}\cap Y=R,qquad
                         Y\cap X_i=R.                           \tag{6.4}
\]

They are the same facet, so their union is \(R\), not \(Y\).  Therefore
the one-facet Hall assignment proves the one-cycle **owner** completion,
but it does not give the distinct-facet compiler identity needed to recover
\(Y\) as the union of its two adjacent emitted lower labels.  Literal
appending, which costs only (5.5), is the currently rigorous OR-word
interface.

The exact missing upgrade is a two-sided tight saturating cycle (or an
\(o(W/H)\)-component factor) with both lower and upper missing hinges
\(o(W)\).  The published theorem supplies one sign at one depth.

In a complement-equivariant factor, a lower theorem would automatically
give the upper theorem.  The published saturating cycle is not known to be
complement-equivariant, so it cannot simply be substituted into the fused
compiler to invoke this shortcut.

### Proposition 6.1 (the exact complement-symmetric (q=1) target)

On even ground \([2m]\), let \(C\) be an oriented spanning Johnson
cycle or two-factor satisfying

\[
                         P(X^c)=P(X)^c.                          \tag{6.5}
\]

Then

\[
 \mu_1^+(U)=\mu_1^-(U^c)                                      \tag{6.6}
\]

for every \((m+1)\)-set \(U\).  In particular, a
complement-equivariant Hamilton Johnson cycle with complete lower support
has complete upper support as well and solves the full signed \(q=1\)
owner-cycle gate in one component.

#### Proof

Complementation sends the edge \(X\to P(X)\) to
\(X^c\to P(X)^c\), and

\[
 (X\cup P(X))^c=X^c\cap P(X)^c.                              \tag{6.7}
\]

The complement-equivariant successor pairs the occurrences bijectively,
which gives (6.6). \(\square\)

Thus the precise strengthening of the published theorem is not another
q1 moment estimate; it is a complement-equivariant lower-saturating
cycle.  No such refinement follows from the two-level saturating-cycle
theorem currently cited.
