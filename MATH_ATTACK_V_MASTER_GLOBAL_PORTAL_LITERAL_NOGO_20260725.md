# Master redirect V: a global literal no-go for fixed-kernel portal fusion

Date: 2026-07-25

## 0. Outcome

This report addresses the master redirect directly.  It does not prove

\[
\nu(k)\le(1+o(1))W(k).
\]

It proves a global, literal counterexample to the implication on which the
stationary portal-sharing lane depended.

At every fixed Gaussian depth

\[
H=\lceil A\sqrt m\rceil,
\qquad
W=\binom{2m}{m},
\tag{0.1}
\]

there is an explicit global word architecture with all of the following
properties:

1. it has length \(W+o(W)\);
2. it literally represents every middle mask;
3. its canonical middle owners lie, apart from \(o(W)\) exceptions, on
   components of length \(\ell=\Theta(m^{3/4})=\omega(H)\);
4. its total independent MTF initialization and component-separation cost is
   \(o(W)\);
5. after one common coordinate relabelling, all but \(o(W)\) canonical
   endpoint flags are box-rainbow, and the word carries
   \(\Omega_A(HW)\) useful endpoint--target--box incidences; but
6. the set of **all literal contiguous-OR targets** of rank \(m+H\) in the
   complete word has size only \(o(W)\).

Since

\[
\binom{2m}{m+H}
=(e^{-A^2}+o_A(1))W,
\tag{0.2}
\]

the word misses

\[
(e^{-A^2}-o_A(1))W
\tag{0.3}
\]

targets in that single required rank.

The construction uses the audited fixed-kernel translation tiling of long
pair-flip components.  Its canonical depth-\(H\) support was already known
to collapse.  The new point is that the collapse survives an audit of
**every interval in the physical word**, including initialization letters
and component seams.  Put the full mask \([2m]\) between components.  Any
interval crossing a separator then has union \([2m]\), so it cannot produce
a central-band target.  Inside one component, an interval using only
productive low-core updates has rank \(m+H\) if and only if it consists of
exactly \(2H+1\) consecutive updates; its union is precisely a canonical
deepest-upper flag.  Intervals beginning in the initialization prefix add
at most \(2H+1\) further rank-\((m+H)\) targets per component.  Therefore

\[
\boxed{
|\operatorname{OR}_{m+H}(\mathcal W)|
\le
S_H^+ +(2H+1)C,}
\tag{0.4}
\]

where \(S_H^+\) is the global canonical depth-\(H\) support and \(C\) is the
number of long components.  In the fixed-kernel tiling,

\[
S_H^+
\le
\frac{2\ell}{2^H}W+o(W),
\qquad
C\le\frac{W}{2\ell}+o(W/\ell).
\tag{0.5}
\]

For \(\ell=\Theta(m^{3/4})\), both terms in (0.4) are \(o(W)\).

This is a genuine contiguous-OR theorem, not an occurrence ledger.  It
definitively disproves the following proposed portal implication:

\[
\begin{gathered}
\text{super-}H\text{-long legal components}
+o(W)\text{ reset/seam cost}\\
+\Omega(HW)\text{ box-rainbow portal incidence}
\quad\Longrightarrow\quad
\text{Gaussian central-band coverage}.
\end{gathered}
\tag{0.6}
\]

Thus amortizing component portals is not the remaining constant-one
theorem.  In the stationary translated-kernel architecture it can be done
perfectly while a required Gaussian rank is almost entirely absent from the
actual word.  Varying active frames or kernels, or proving a new
cross-component rankwise support theorem, is mathematically necessary.
The portal-metrics package by itself is closed as an independent route.

No web search, finite search, computation, or solver is used.

---

## 1. Literal target notation and separator isolation

For a word

\[
\mathcal W=(A_1,\ldots,A_N),
\qquad
\varnothing\ne A_i\subseteq[2m],
\tag{1.1}
\]

put

\[
\operatorname{OR}_r(\mathcal W)
=
\left\{
\bigcup_{i=a}^{b}A_i:
1\le a\le b\le N,\ 
\left|\bigcup_{i=a}^{b}A_i\right|=r
\right\}.
\tag{1.2}
\]

This is the set of all rank-\(r\) masks literally represented by
contiguous intervals of the physical word.

Let

\[
\Omega=[2m].
\tag{1.3}
\]

### Lemma 1.1 -- full-mask separator

Let

\[
\mathcal W
=
\mathcal B_1,\Omega,\mathcal B_2,\Omega,\ldots,\Omega,\mathcal B_s
\tag{1.4}
\]

be a concatenation of arbitrary nonzero blocks.  For every \(r<2m\),

\[
\boxed{
\operatorname{OR}_r(\mathcal W)
=
\bigcup_{j=1}^{s}\operatorname{OR}_r(\mathcal B_j).}
\tag{1.5}
\]

#### Proof

An interval contained in one block gives the right side.  Every interval
meeting a separator \(\Omega\) has union \(\Omega\), of rank \(2m\), and
therefore contributes nothing to rank \(r<2m\). \(\square\)

The separator costs one nonzero letter per seam.  When the component count
is \(o(W)\), it is an admissible \(o(W)\) addition.  Its role is not to help
coverage; it makes the absence of incidental seam witnesses exact.

---

## 2. The cyclic low-core interval identity

Fix integers

\[
1\le H<\ell,
\qquad
3H<\ell.
\tag{2.1}
\]

Let

\[
\gamma=(z_0,\ldots,z_{2\ell-1})
\tag{2.2}
\]

be a cyclic order on a \(2\ell\)-set \(R\), and fix a disjoint core

\[
C\subseteq[2m],
\qquad
|C|=m-\ell.
\tag{2.3}
\]

For cyclic intervals \(I_\gamma(i,a)\), define the middle owners

\[
T_i=C\cup I_\gamma(i,\ell)
\tag{2.4}
\]

and the productive radius-\(H\) low-core letters

\[
L_i=C\cup I_\gamma(i+H,\ell-H),
\qquad
0\le i<2\ell.
\tag{2.5}
\]

These are the standard cyclic-strip canonical letters.  They satisfy

\[
|T_i|=m,
\qquad
|L_i|=m-H.
\tag{2.6}
\]

### Lemma 2.1 -- exact union growth

For every linear interval of productive letters

\[
L_i,L_{i+1},\ldots,L_{i+t-1}
\tag{2.7}
\]

which stays inside the cut component, one has

\[
\left|
\bigcup_{j=0}^{t-1}L_{i+j}
\right|
=
m-H+\min\{t-1,\ell+H\}.
\tag{2.8}
\]

In particular,

\[
\boxed{
\left|
\bigcup_{j=0}^{t-1}L_{i+j}
\right|
=m+H
\quad\Longleftrightarrow\quad
t=2H+1.}
\tag{2.9}
\]

For \(t=2H+1\), the union is the canonical deepest-upper mask

\[
\boxed{
\bigcup_{j=0}^{2H}L_{i+j}
=
C\cup I_\gamma(i+H,\ell+H).}
\tag{2.10}
\]

#### Proof

The active parts in (2.7) are cyclic intervals of common length
\(\ell-H\), whose starting positions advance by one.  Their union is one
cyclic interval of length

\[
\min\{2\ell,\ell-H+t-1\}.
\tag{2.11}
\]

Adding the fixed core \(C\) gives

\[
(m-\ell)+\min\{2\ell,\ell-H+t-1\}
=m-H+\min\{\ell+H,t-1\},
\]

which is (2.8).  Since \(H<\ell\), the value \(m+H\) is reached before
saturation, and (2.9) follows uniquely from \(t-1=2H\).  Substituting
\(t=2H+1\) gives (2.10). \(\square\)

Thus the physical low-core sequence has no hidden rank-\((m+H)\) interval
targets: at that rank its intervals are exactly the canonical
\((2H+1)\)-letter portal arms.

---

## 3. Initialization cannot create many targets in one rank

Let one literal canonical component word have the form

\[
\mathcal B
=
(R_1,\ldots,R_s,L_0,L_1,\ldots,L_{K-1}),
\tag{3.1}
\]

where \(R_1,\ldots,R_s\) are the nonproductive reverse-initialization
letters and the \(L_i\)'s are productive low-core letters satisfying
Lemma 2.1.  In the audited radius-\(H\) lift,

\[
s=2H+1.
\tag{3.2}
\]

Let

\[
\mathcal S_H^+(\mathcal B)
=
\left\{
\bigcup_{j=i}^{i+2H}L_j:
0\le i,\ i+2H<K
\right\}
\tag{3.3}
\]

be its internal canonical deepest-upper support.

### Lemma 3.1 -- all-interval support bound for one component

\[
\boxed{
|\operatorname{OR}_{m+H}(\mathcal B)|
\le
|\mathcal S_H^+(\mathcal B)|+s.}
\tag{3.4}
\]

#### Proof

An interval whose left endpoint is one of the productive letters \(L_i\)
and which avoids the initialization prefix consists only of consecutive
productive letters.  Lemma 2.1 says that its union has rank \(m+H\) if and
only if it has length \(2H+1\), in which case its target belongs to
\(\mathcal S_H^+(\mathcal B)\).

It remains to count intervals whose left endpoint is an initialization
letter \(R_j\).  Fix \(R_j\).  As the right endpoint advances, the interval
unions are nested by inclusion.  A nested sequence contains at most one
distinct mask of any fixed cardinality: if two comparable sets have the
same cardinality, they are equal.  Hence each of the \(s\) initialization
starts contributes at most one additional rank-\((m+H)\) target.  Summing
over \(j\) proves (3.4). \(\square\)

This proof counts every interval in the component.  No last-occurrence or
designated-witness restriction remains.

---

## 4. Global barrier-isolated support theorem

Let

\[
\mathcal B_1,\ldots,\mathcal B_C
\tag{4.1}
\]

be canonical cyclic-strip component words as in Section 3.  Put

\[
\mathcal W_{\rm main}
=
\mathcal B_1,\Omega,\mathcal B_2,\Omega,\ldots,\Omega,\mathcal B_C.
\tag{4.2}
\]

Let

\[
\mathcal S_H^+
=
\bigcup_{j=1}^{C}\mathcal S_H^+(\mathcal B_j).
\tag{4.3}
\]

### Theorem 4.1 -- exact literal deepest-rank bound

\[
\boxed{
|\operatorname{OR}_{m+H}(\mathcal W_{\rm main})|
\le
|\mathcal S_H^+|+(2H+1)C.}
\tag{4.4}
\]

#### Proof

Lemma 1.1 confines every rank-\((m+H)\) interval to one component.
Apply Lemma 3.1 to each component and take the union bound. \(\square\)

The theorem remains true if one appends additional isolated one-letter
middle blocks, each separated from the rest by \(\Omega\): such a block has
only one internal interval, of rank \(m\), and every interval crossing one
of its separators has rank \(2m\).

### Corollary 4.2 -- portal repair threshold

If

\[
|\mathcal S_H^+|=o(W),
\qquad
HC=o(W),
\tag{4.5}
\]

then

\[
\boxed{
|\operatorname{OR}_{m+H}(\mathcal W_{\rm main})|=o(W).}
\tag{4.6}
\]

Thus cheap component portals and collapsed deepest support cannot be
rescued by incidental intervals inside the initialized component words.

---

## 5. The fixed-kernel global construction

We now apply Theorem 4.1 to the audited translation-kernel tiling.

Choose a power of two

\[
\ell=2^t
\tag{5.1}
\]

with

\[
\ell=\Theta(m^{3/4}).
\tag{5.2}
\]

For fixed \(A>0\), take \(H=\lceil A\sqrt m\rceil\).  Then

\[
3H<\ell,
\qquad
\frac H\ell\longrightarrow0,
\qquad
H-\log_2\ell\longrightarrow+\infty.
\tag{5.3}
\]

The standard pair-flip cycle \(P_\ell\subseteq\mathbb F_2^\ell\) is
translated by

\[
K=\ker\phi,
\qquad
\operatorname{codim}K=t+1.
\tag{5.4}
\]

The fixed-kernel product-extension construction gives a middle-owner family
of size

\[
W-M,
\qquad
M=o(W),
\tag{5.5}
\]

partitioned into cyclic components of length \(2\ell\).  Therefore

\[
C=\frac{W-M}{2\ell}
\le\frac W{2\ell}.
\tag{5.6}
\]

Every component is a legal canonical MTF trajectory because its positive
runs have length \(\ell>H\).  Its literal independently initialized word
has length

\[
2\ell+2H+1.
\tag{5.7}
\]

The audited translation-kernel shadow-collapse theorem gives

\[
\boxed{
|\mathcal S_H^+|
\le
\frac{2\ell}{2^H}W+o(W).}
\tag{5.8}
\]

### Theorem 5.1 -- a global literal support-collapse word

There is a nonzero Boolean word \(\mathcal W_{\rm bad}\) such that:

1. \(\mathcal W_{\rm bad}\) represents every middle mask;
2. 
   \[
   |\mathcal W_{\rm bad}|=W+o(W);
   \tag{5.9}
   \]
3. all but \(M=o(W)\) middle owners lie on legal length-\(2\ell\)
   canonical components, and the total initialization plus separator cost
   is \(o(W)\); and
4.
   \[
   \boxed{
   |\operatorname{OR}_{m+H}(\mathcal W_{\rm bad})|=o(W).}
   \tag{5.10}
   \]

#### Construction

Independently initialize the \(C\) fixed-kernel components and place one
separator \(\Omega\) between consecutive component words.  For each of the
\(M\) omitted middle masks \(T\), append the isolated block

\[
\Omega,T,\Omega.
\tag{5.11}
\]

Repeated adjacent separators may be merged; no estimate uses this saving.

#### Proof

The main components represent their \(W-M\) distinct middle owners at their
canonical state endpoints.  Every omitted middle mask is represented by its
one-letter block.  This proves middle coverage.

The total length is at most

\[
\begin{aligned}
&(W-M)+(2H+1)C+(C-1)+3M\\
&\qquad\le
W+(2H+2)C+2M.
\end{aligned}
\tag{5.12}
\]

By (5.2), (5.5), and (5.6),

\[
\frac{HC}{W}\le\frac{H}{2\ell}=o(1),
\]

so (5.12) is \(W+o(W)\).

The isolated middle blocks contribute no rank-\((m+H)\) target, and their
separators prevent cross-block central intervals.  Apply Theorem 4.1,
(5.6), and (5.8):

\[
\begin{aligned}
|\operatorname{OR}_{m+H}(\mathcal W_{\rm bad})|
&\le
\frac{2\ell}{2^H}W+o(W)
+(2H+1)\frac W{2\ell}\\
&=
\left(
\frac{2\ell}{2^H}
+\frac{2H+1}{2\ell}
\right)W+o(W)
=o(W).
\end{aligned}
\tag{5.13}
\]

This proves all claims. \(\square\)

### Corollary 5.2 -- linear failure in one Gaussian rank

\[
\boxed{
\left|
\binom{[2m]}{m+H}
\setminus
\operatorname{OR}_{m+H}(\mathcal W_{\rm bad})
\right|
=(e^{-A^2}-o_A(1))W.}
\tag{5.14}
\]

#### Proof

The exact ratio is

\[
\frac{\binom{2m}{m+H}}{W}
=
\prod_{j=1}^{H}\frac{m-j+1}{m+j}
=e^{-A^2+o_A(1)}.
\tag{5.15}
\]

Subtract (5.10). \(\square\)

The word is therefore not universal even on the fixed central band
\(m-H,\ldots,m+H\), despite having the optimal leading length and completely
amortized component portals.

---

## 6. The same word has optimal portal incidence

The failure in Theorem 5.1 is not caused by poor product-box geometry.
Assume \(2m=3s\) and fix the audited product of three block SCDs.

At one canonical endpoint, a pair of flag masks separated by \(g\) ranks
has, after a uniform common coordinate permutation, same-box probability at
most

\[
\frac{\binom{g+2}{2}}{\binom{m-H}{g}}.
\tag{6.1}
\]

Summing over the pairs in one radius-\(H\) flag gives

\[
O_A(H/m).
\tag{6.2}
\]

There are \(W-o(W)\) main canonical endpoints.  Hence one common relabelling
has aggregate endpoint same-box collision count

\[
\boxed{O_A(HW/m)=O_A(W/\sqrt m)=o(W).}
\tag{6.3}
\]

Consequently all but \(o(W)\) main endpoints have their \(2H+1\) canonical
targets in \(2H+1\) distinct product boxes.

Let \(\mathcal T\) be the audited dominant-box target family.  For fixed
\(A\), a positive \(A\)-dependent fraction of the signed ranks
\(-H,\ldots,H\) contains a positive-density subfamily of
\(\mathcal T\).  Uniform relabelling is transitive on each rank, so the
expected number of canonical occurrences landing in \(\mathcal T\) is

\[
\Omega_A(HW).
\tag{6.4}
\]

The standard bounded-variable estimate, combined with Markov's inequality
for (6.3), gives one common relabelling satisfying simultaneously

\[
\boxed{
\Omega_A(HW)\text{ distinct endpoint--}\mathcal T\text{--box incidences},
\qquad
o(W)\text{ same-endpoint box collisions}.}
\tag{6.5}
\]

Coordinate relabelling is a bijection on Boolean masks and preserves
contiguous unions.  Therefore (5.10) remains true after this relabelling.

### Theorem 6.1 -- portal metrics do not imply band coverage

For every fixed \(A>0\), the word from Theorem 5.1 may be relabelled so
that it simultaneously has:

\[
\begin{gathered}
|\mathcal W_{\rm bad}|=W+o(W),\\
W\text{ literal middle targets},\\
o(W)\text{ total component initialization/separation cost},\\
\omega(H)\text{-long legal components},\\
\Omega_A(HW)\text{ useful endpoint--box incidences},\\
o(W)\text{ within-flag box collisions},
\end{gathered}
\tag{6.6}
\]

but

\[
|\operatorname{OR}_{m+H}(\mathcal W_{\rm bad})|=o(W).
\tag{6.7}
\]

Hence no theorem whose hypotheses consist only of the quantities in (6.6)
can imply central-band coverage.

#### Proof

All assertions except the compatibility of the two relabelling properties
were proved above.  Let \(X_\sigma\) be the number of useful selected-family
occurrences and \(Y_\sigma\) the within-flag box-collision count.
Equation (6.4) and the deterministic bound
\(X_\sigma\le(2H+1)W\) give a fixed positive lower bound on the probability
that \(X_\sigma\ge c_AHW\).  Equation (6.3) is an expectation bound for
\(Y_\sigma\).  Markov's inequality, with a sufficiently large fixed
constant, makes the bad probability for \(Y_\sigma\) smaller than the first
positive probability.  Thus one permutation has both properties.
Relabelling preserves (6.7). \(\square\)

---

## 7. Portal-endpoint repair cannot fix the example

There is a second exact statement which makes the no-go independent of the
chosen separators.

Let \(Z\) be a set of physical word positions.  Call a witness interval
\(Z\)-anchored if at least one of its two endpoints belongs to \(Z\).

### Lemma 7.1 -- oriented portal capacity in one rank

For every word, every rank \(r\), and every physical portal set \(Z\), the
number of distinct rank-\(r\) targets having a \(Z\)-anchored witness is at
most

\[
\boxed{2|Z|.}
\tag{7.1}
\]

#### Proof

Fix a right endpoint \(z\).  As the left endpoint moves left, the interval
unions form an inclusion chain, and therefore contain at most one distinct
mask of rank \(r\).  Thus witnesses whose right endpoint lies in \(Z\)
contribute at most \(|Z|\) targets.

The same argument with fixed left endpoints contributes at most another
\(|Z|\).  Intervals with both endpoints in \(Z\) may be counted twice,
which only strengthens the upper bound. \(\square\)

### Corollary 7.2 -- linear portal requirement after shadow collapse

Suppose a principal word has \(o(W)\) rank-\((m+H)\) targets and every
additional credited witness is anchored at a portal set \(Z\).  If the
completed word covers rank \(m+H\), then

\[
\boxed{
|Z|
\ge
\left(\frac{e^{-A^2}}2-o_A(1)\right)W.}
\tag{7.2}
\]

In particular, neither

\[
|Z|=O(W/H)
\tag{7.3}
\]

nor any \(o(W)\) component-portal set can repair the collapse.

#### Proof

The number of missing targets is
\((e^{-A^2}-o_A(1))W\).  Apply Lemma 7.1. \(\square\)

This is a global endpoint theorem.  It applies to arbitrary portal arms and
arbitrary intervals anchored at them; no local product-box decomposition is
used.

---

## 8. Exact implication for the constant-one program

The master target requires, for each fixed \(A\), one literal
\(W+o(W)\) word covering every rank in the radius-\(A\sqrt m\) band,
followed by the audited tail argument and then \(A\to\infty\).

Theorems 5.1 and 6.1 show that the following data do not compose into that
target:

* \(W-o(W)\) middle owners on legal components;
* component length \(\omega(H)\);
* component count \(o(W/H)\);
* total exact reset and portal cost \(o(W)\);
* asymptotically maximal endpoint product-box degree;
* \(\Omega(HW)\) useful global portal incidence;
* a literal word of length \(W+o(W)\).

All of these hold simultaneously while an entire Gaussian rank has only
\(o(W)\) literal support.

Therefore a successful constant-one proof must add a hypothesis which
directly controls rankwise Boolean support.  Within the present family that
means varying the active frames or translation kernels so that the
stabilizers

\[
K\cap V_{J(p)}
\tag{8.1}
\]

are small for essentially every depth and position, or replacing the
stationary translation tiling by a genuinely cross-component construction.
Product-box relabelling cannot help: it changes box names but not equality
of Boolean targets.

This closes the stationary fixed-kernel global-portal lane and every
proposed implication using only the metrics in (6.6).  It does not disprove the
contiguous-OR conjecture, and it does not rule out a nonstationary
rank-balanced MTF/SCD construction.  Those are different mathematical
requirements, not unfinished portal amortization.

---

## 9. Audit

1. **All intervals are counted.**  Lemma 3.1 splits intervals by their
   actual left endpoint.  Productive starts are handled by the exact union
   formula; initialization starts are bounded by monotonicity.  There is no
   designated-occurrence restriction.
2. **Seams are literal.**  The separator is the permitted nonzero mask
   \([2m]\).  Every crossing interval has full union, so no central target
   is hidden across a seam.
3. **Unique productive length.**  A low-core interval reaches rank \(m+H\)
   exactly after \(2H+1\) letters.  Longer intervals never return to that
   rank because unions are monotone.
4. **Initialization constant.**  The raw canonical component has exactly
   \(2H+1\) letters before the first productive low-core letter.  Even an
   \(O(H)\) variation would give the same asymptotic theorem.
5. **Length ledger.**  Main owners contribute \(W-M\), independent
   initializations contribute \((2H+1)C\), main separators contribute at
   most \(C-1\), and isolated omitted middles contribute at most \(3M\).
   This gives (5.12).
6. **Gaussian scale.**  With \(\ell=\Theta(m^{3/4})\),
   \(H/\ell=O_A(m^{-1/4})\) and
   \(2\ell/2^H=o(1)\).
7. **Exact rank constant.**  The central-binomial ratio at
   \(H=A\sqrt m+O(1)\) is \(e^{-A^2}+o_A(1)\), not
   \(e^{-A^2/2}\).
8. **Relabelling invariance.**  A common coordinate permutation preserves
   word length, MTF legality, interval unions, and the cardinality of every
   rank support.  It can improve box dispersion but cannot repair (5.10).
9. **Scope.**  The theorem is a no-go for the stationary fixed-kernel
   global-portal architecture and for any proposed implication based only
   on the portal metrics in (6.6).  It is not a lower bound for arbitrary
   contiguous-OR words.

## 10. Final theorem

\[
\boxed{
\begin{gathered}
\text{There are literal }W+o(W)\text{ global MTF portal words with}\\
\omega(H)\text{-long components},\ o(W)\text{ total portal cost, and}\\
\Omega_A(HW)\text{ useful box incidence, but only }o(W)\text{ actual}\\
\text{contiguous-OR targets in rank }m+H,\quad H=A\sqrt m.\\
\text{Therefore fixed-kernel fusion and portal metrics cannot prove constant one.}
\end{gathered}}
\tag{10.1}
\]
