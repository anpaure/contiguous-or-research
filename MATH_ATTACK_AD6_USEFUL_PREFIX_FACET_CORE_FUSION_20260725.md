# Master-redirect AD: useful-prefix fusion of the facet braid

Date: 2026-07-25

## 0. Outcome

Put

\[
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is sufficiently large that
\(1\le H\le m/2\).

This report proves a strict improvement to the literal adaptive-MTF route.
Full residual-state synchronization is unnecessary.  To expose every band
rank \(m-H,\ldots,m+H\), one needs only the ordered **useful prefix**
consisting of the lower core and the next \(2H\) singleton blocks.  The
residual tail may remain arbitrarily refined.

The exact minimum positive bridge length from a source state \(\Sigma\) to
a prescribed useful prefix \(\Lambda\) is

\[
\boxed{
d_{\rm pref}^+(\Sigma,\Lambda)=\max\{1,t_*(\Sigma,\Lambda)\},}
\tag{0.1}
\]

where \(t_*\) is the least target-prefix length whose deletion makes the
surviving source state begin with the remaining useful target suffix.

Consequently, if \(H\)-legal pieces partition the \(W\) middle owners and
their actual prefix-bridge lengths are \(b_j\), one integral literal word
has exact raw length

\[
\boxed{
W+\widehat{\mathfrak P}_H,
\qquad
\widehat{\mathfrak P}_H
=2H+\sum_{j=1}^{C-1}(b_j-1).}
\tag{0.2}
\]

This is one letter less per independent component than the full-state
ledger and can be arbitrarily smaller at depleted seams.

The literal first-band braid is not merely retained as a set of masks.  If

\[
L_j=\bigcap_{r=0}^{H}T_{j+r}
\]

is the rank-\((m-H)\) core along an \(H\)-legal path, then in the guarded
bulk

\[
T_t\cap T_{t+1}
=\bigcup_{j=t-H+1}^{t}L_j,
\qquad
T_t=\bigcup_{j=t-H}^{t}L_j,
\qquad
T_{t-1}\cup T_t
=\bigcup_{j=t-H-1}^{t}L_j.
\tag{0.3}
\]

Thus the old facet, middle, and upper witnesses are exactly the
\(H\)-, \((H+1)\)-, and \((H+2)\)-letter windows of the same low core word.
Adjacent facet witnesses still overlap, and their interval hulls are still
the old middle and upper masks.  No zero-run condition is needed.

Let \(\mathcal H_{\ge2}\) be the remaining higher-depth hole family and let
\(\Phi_Z\) be the audited fixed-trace repair functional.  If \(e\) certified
forest edges have pairwise distinct lower colours and separately pairwise
distinct upper colours, then

\[
\boxed{
L_{\rm band}
\le
W+\widehat{\mathfrak P}_H
+2\left(\binom{2m}{m-1}-e\right)
+\Phi_Z(\mathcal H_{\ge2}).}
\tag{0.4}
\]

For the exact odd complementary-geodesic factor,

\[
C=\frac{W}{m+1},\qquad e=\binom{2m}{m-1},
\]

and independent useful-prefix starts give the unconditional exact raw
length

\[
\boxed{
W+2HC
=W+\frac{2HW}{m+1}
=W+o_A(W).}
\tag{0.5}
\]

Therefore the literal first band, pervasive core fusion, \(H\)-legality,
integrality, and portal length defect are all solved.  In this exact
odd-factor specialization, the remaining sufficient condition is

\[
\boxed{
\widehat{\mathfrak P}_H+\Phi_Z(\mathcal H_{\ge2})=o_A(W).}
\tag{Pref-PTAD\(_A\), UNPROVED}
\]

For every fixed \(A\), this condition composes with the audited outer tails;
taking \(m\to\infty\) first and then \(A\to\infty\) proves

\[
\nu(k)\le(1+o(1))W(k).
\]

The improvement has a sharp limit.  In a raw word of length \(W+E\), one
principal letter \(L_t\) of rank \(m-H\) ends at every middle owner.  Hence

\[
\boxed{
|\mathcal R_{m-H}|
\le |\{L_t\}|+E.}
\tag{0.6}
\]

So any coefficient-one completion forces

\[
|\{L_t\}|\ge N_H-o(W).
\tag{0.7}
\]

Residual-tail fusion cannot manufacture deepest support.  The only
unproved part of this lane is genuinely global cross-component
near-surjectivity/trace compression for the forced cores and their higher
flags.

No web search, finite search, computation, fractional ownership, or
cross-factor operation is used.

---

## 1. Exact useful-prefix bridge metric

Let an ordered-partition MTF state be

\[
\Sigma=(C_1,\ldots,C_r).
\]

We use the standard augmented last-occurrence convention: coordinates not
yet occurring in the physical word form one trailing unseen residual block.
That block costs no letter and is never part of a useful prefix.  Thus every
useful-prefix block below has a positive last occurrence and every one of
its prefix unions is a literal suffix OR.  This convention is also what
allows the first piece to start by writing only its useful blocks; its
unseen complement remains in the trailing residual.  Only this first
complement is genuinely unseen.  Later resets leave the inherited or
refined source tail behind the newly written useful prefix, and Lemma 2.1
accepts that arbitrary tail.

### Lemma 1.0 — uncharged unseen tail is literal

For a nonempty physical word \(X_1,\ldots,X_\ell\), put

\[
\tau(x)=\max\bigl(\{i:x\in X_i\}\cup\{0\}\bigr).
\]

Order the nonempty positive level sets of \(\tau\) by decreasing level and
put the zero level set last when it is nonempty.  Appending a nonempty mask
\(X\) performs exactly the MTF update

\[
(C_1,\ldots,C_r)\longmapsto
(X,C_1\setminus X,\ldots,C_r\setminus X),
\]

with empty blocks deleted.  Moreover, if \(C_a\) has positive level \(t_a\),
then

\[
C_1\cup\cdots\cup C_a
=\bigcup_{i=t_a}^{\ell}X_i.
\tag{1.0}
\]

Hence every prefix ending before the unseen residual is a literal
contiguous-OR interval, while the residual costs no position.

#### Proof

Appending \(X\) gives every coordinate of \(X\) the new common last time
\(\ell+1\) and leaves all other last times unchanged, proving the update
formula.  A coordinate lies in the suffix \(X_{t_a},\ldots,X_\ell\) exactly
when its last time is at least \(t_a\), which is exactly membership in
\(C_1\cup\cdots\cup C_a\).  \(\square\)

For a mask \(X\), write

\[
D_X(\Sigma)
=(C_1\setminus X,\ldots,C_r\setminus X),
\tag{1.1}
\]

deleting empty blocks.

Fix pairwise disjoint nonempty target blocks

\[
\Lambda=(B_1,\ldots,B_s),
\qquad s=2H+1.
\tag{1.2}
\]

They need not partition the ground set.  In the band application, \(B_1\)
is the rank-\((m-H)\) lower core and \(B_2,\ldots,B_s\) are the \(2H\)
lower and upper singleton markers.  The blocks beyond \(B_s\) form an
arbitrary partition of the remaining \((m-H)\)-set.

Put

\[
U_t=B_1\cup\cdots\cup B_t,
\qquad 0\le t\le s,
\tag{1.3}
\]

with \(U_0=\varnothing\).  Let \(t_*(\Sigma,\Lambda)\) be the least
\(t\in\{0,\ldots,s\}\) such that

\[
D_{U_t}(\Sigma)
\text{ begins with }
(B_{t+1},\ldots,B_s).
\tag{1.4}
\]

The condition for \(t=s\) is empty and hence always holds.

### Theorem 1.1 — exact useful-prefix distance

The minimum length of a nonempty MTF word which carries \(\Sigma\) to any
state beginning with \(\Lambda\) is

\[
\boxed{
d_{\rm pref}^+(\Sigma,\Lambda)
=\max\{1,t_*(\Sigma,\Lambda)\}.}
\tag{1.5}
\]

#### Proof: upper bound

Suppose \(t=t_*>0\).  Append the cumulative masks

\[
U_t,U_{t-1},\ldots,U_1.
\tag{1.6}
\]

Their positive-last-occurrence blocks are, in order,

\[
U_1=B_1,\quad
U_2\setminus U_1=B_2,\quad\ldots,\quad
U_t\setminus U_{t-1}=B_t.
\]

Their total union is \(U_t\), so the surviving old state is
\(D_{U_t}(\Sigma)\), which begins with \(B_{t+1},\ldots,B_s\) by (1.4).
The final state therefore begins with \(\Lambda\).

If \(t_*=0\), then \(\Sigma\) already begins with \(\Lambda\).  The
one-letter update \(B_1\) is idempotent on this useful prefix: after deleting
\(B_1\), the surviving state begins with \(B_2,\ldots,B_s\).  Hence one
positive update suffices.

#### Proof: lower bound

After updates \(X_1,\ldots,X_b\), the final ordered partition is

\[
\begin{aligned}
(&X_b,
X_{b-1}\setminus X_b,
\ldots,
X_1\setminus\textstyle\bigcup_{j>1}X_j,\\
&D_{\cup_jX_j}(\Sigma)),
\end{aligned}
\tag{1.7}
\]

with empty blocks deleted.  Thus every update-generated nonempty block
precedes every surviving source block.

Let \(a\) be the number of update-generated nonempty blocks before the
surviving source state.  If \(a\ge s\), then \(b\ge a\ge s\ge t_*\).
If \(a<s\) and the final state begins with \(\Lambda\), those generated
blocks must be exactly \(B_1,\ldots,B_a\), their union is \(U_a\), and the
surviving source state begins with \(B_{a+1},\ldots,B_s\).  Hence

\[
t_*\le a\le b.
\]

Every admissible bridge is nonempty, so \(b\ge1\).  This proves (1.5).
\(\square\)

### 1.1 Strict separation from full-state synchronization

Let \(R_1,R_2\) be nonempty disjoint blocks completing the useful prefix,
and put

\[
\Sigma=(B_1,\ldots,B_s,R_1,R_2).
\]

For the useful target prefix \(\Lambda\), (1.5) gives

\[
d_{\rm pref}^+(\Sigma,\Lambda)=1.
\tag{1.8}
\]

For the full compact target

\[
\Pi=(B_1,\ldots,B_s,R_1\cup R_2),
\]

the exact full-state bridge metric gives

\[
d_{\rm MTF}^+(\Sigma,\Pi)=s+1=2H+2.
\tag{1.9}
\]

Indeed, deleting any proper target prefix leaves \(R_1,R_2\) as two old
blocks rather than the single target residual.  Only deleting the whole
target makes the required suffix condition vacuous.  Conversely, updating
the residual union and then the useful blocks realizes \(\Pi\) in \(s+1\)
steps.

This example has the same useful prefix on both sides, so it is not by
itself an owner-changing seam between vertex-disjoint pieces.  Its exact
purpose is to prove that full-state distance can overcharge literal useful-
prefix realization by \(2H+1\) updates.  In particular, the full-residual
depletion lower bound does not apply to prefix portals.

---

## 2. Tail-insensitive canonical evolution

Let

\[
T_{i+1}=T_i-\{p_i\}+\{q_i\},
\qquad T_i\in\binom{[2m]}m,
\tag{2.1}
\]

be \(H\)-legal: every internal positive coordinate run contains at least
\(H+1\) middle states (equivalently, if it enters on transition \(i\) and
leaves on transition \(j\), then \(j-i\ge H+1\)).  Use compatible future
dummy departures near a finite
right boundary and define

\[
L_i=T_i\setminus\{p_i,\ldots,p_{i+H-1}\}.
\tag{2.2}
\]

The displayed departures are distinct members of \(T_i\), so
\(|L_i|=m-H\).  A useful-prefix state has the form

\[
\Pi_i=\bigl(
L_i,
\{p_{i+H-1}\},\ldots,\{p_i\},
\{u_{i,1}\},\ldots,\{u_{i,H}\},
\mathcal C_i
\bigr),
\tag{2.3}
\]

where \(\mathcal C_i\) is an arbitrary ordered partition of the remaining
\((m-H)\)-set.  Its first \(s=2H+1\) blocks are the useful prefix.

### Lemma 2.1 — tail insensitivity

Put

\[
L_{i+1}=L_i-\{p_{i+H}\}+\{q_i\}.
\tag{2.4}
\]

Then one update by \(L_{i+1}\) produces another state of the form (2.3)
with middle owner \(T_{i+1}\), regardless of the internal partition of
\(\mathcal C_i\).

#### Proof

Direct block subtraction gives the new lower core followed by the shifted
future-departure queue.  The old marker \(p_i\) enters the upper candidate
queue.  If \(q_i\) is one of the exposed upper singletons, it is deleted
there; together with \(p_i\), exactly \(H\) exposed upper singletons remain.
If \(q_i\) lies in \(\mathcal C_i\), it is deleted from its unique tail
block; \(p_i\) is prepended to the upper queue and its oldest exposed marker
is demoted as a singleton into the refined tail.  In both cases the first
\(2H+1\) blocks have the required form.  No merger of tail blocks is used.
\(\square\)

Every rank \(m-H,\ldots,m+H\) is a prefix rank of (2.3).  Therefore all
these masks are literal suffix ORs at the state endpoint.  This proves that
Theorem 1.1 synchronizes exactly the data needed by the band word.

---

## 3. Facet--core coarea theorem

Assume that every displayed index lies in the actual \(H\)-legal Johnson
path.  The same identities hold across a boundary only when the padding is
itself an \(H\)-legal Johnson extension.  Arbitrary dummy MTF departures do
not suffice.  In the fusion theorem below we use the identities only in the
guarded bulk and treat cut colours separately in Section 4.1.  Define

\[
L_j=\bigcap_{r=0}^{H}T_{j+r}.
\tag{3.1}
\]

The no-short-positive-run condition gives

\[
L_j
=T_j\setminus\{p_j,\ldots,p_{j+H-1}\},
\qquad |L_j|=m-H.
\tag{3.2}
\]

### Theorem 3.1 — exact union/intersection coarea identities

For every \(a\le b\),

\[
\boxed{
\bigcup_{j=a-H}^{b}L_j
=\bigcup_{r=a}^{b}T_r.}
\tag{3.3}
\]

If additionally \(b-a\le H\), then

\[
\boxed{
\bigcup_{j=b-H}^{a}L_j
=\bigcap_{r=a}^{b}T_r.}
\tag{3.4}
\]

#### Proof

Fix one coordinate \(x\).  Its indicator along the path is a union of
positive runs.  Every relevant internal run has at least \(H+1\) states,
and

\[
x\in L_j
\quad\Longleftrightarrow\quad
[j,j+H]\text{ lies inside one positive run of }x.
\tag{3.5}
\]

A positive run meets \([a,b]\) if and only if it contains an
\((H+1)\)-state window whose start lies in \([a-H,b]\).  The forward
direction follows by sliding any such window within the run until it meets
the chosen point of \([a,b]\); the reverse direction is immediate because
every interval \([j,j+H]\) with \(j\in[a-H,b]\) meets \([a,b]\).
This proves (3.3), coordinate by coordinate.

Suppose \(b-a\le H\).  A positive run contains all of \([a,b]\) if and
only if it contains an \((H+1)\)-state window whose start lies in
\([b-H,a]\).  Indeed, the possible start interval for an \(H\)-window
inside a run containing \([a,b]\) intersects \([b-H,a]\); conversely every
such window contains \([a,b]\).  This proves (3.4).  \(\square\)

### Corollary 3.2 — exact literal first-band braid

In the guarded bulk,

\[
\boxed{
C_t:=T_t\cap T_{t+1}
=\bigcup_{j=t-H+1}^{t}L_j,}
\tag{3.6}
\]

\[
\boxed{
T_t=\bigcup_{j=t-H}^{t}L_j,}
\tag{3.7}
\]

and

\[
\boxed{
U_{t-1}:=T_{t-1}\cup T_t
=\bigcup_{j=t-H-1}^{t}L_j.}
\tag{3.8}
\]

Thus the old facet witness \(C_t\) is exactly the \(H\)-letter interval
\([t-H+1,t]\) of the core word.  The interval hull of the adjacent facet
witnesses \(C_{t-1},C_t\) is \([t-H,t]\), whose OR is \(T_t\).  The hull
of three consecutive facet witnesses is \([t-H,t+1]\), whose OR is
\(T_t\cup T_{t+1}\).

Therefore pervasive rank-\((m-H)\) recoding preserves the full interval-
hull geometry of the singleton-capped two-sided-rainbow facet braid.  It
does not preserve the old facet letters as a subsequence; it replaces them
by overlapping core windows, which is forced by the endpoint barriers in
Section 7.  No zero-run hypothesis is used.

### 3.1 Higher adaptive upper flags: exact scope

Suppose that at time \(t\), at least \(q\) currently absent coordinates
have finite latest departure times.  Let \(r_{t,q}\) be the \(q\)-th largest
such departure time.  If \(r_{t,q}-H\) lies in the padded core domain, then

\[
\boxed{
P^+_{t,q}
=\bigcup_{j=r_{t,q}-H}^{t}L_j.}
\tag{3.9}
\]

Indeed, (3.3) identifies the right side with
\(\bigcup_{r=r_{t,q}}^tT_r\), which is \(T_t\) together with exactly the
\(q\) currently absent coordinates last departed at or after
\(r_{t,q}\).

The refresh hypothesis is necessary.  An untouched initial-complement
coordinate can remain in an exposed upper marker although it lies in no
actual core \(L_j\).  The general MTF last-occurrence theorem still gives
every useful flag a literal suffix at the same endpoint, but not always a
core-only interval of the form (3.9).

On a no-return complementary geodesic, every \(2H\)-guarded state is
refreshed and

\[
r_{t,q}=t-q.
\]

Thus all its signed depths are fixed-length sliding windows of the one core
word.

---

## 4. Exact prefix-portal word ledger

Let \(\mathcal P_1,\ldots,\mathcal P_C\) be vertex-disjoint \(H\)-legal
pieces which partition all \(W\) middle masks.  Let piece \(j\) have
\(K_j\) middle owners, so \(\sum_jK_j=W\).  Choose an order and let

\[
b_j=d_{\rm pref}^+
(\Pi_j^{\rm end},\Lambda_{j+1}^{\rm start}),
\qquad 1\le j<C.
\tag{4.1}
\]

Define

\[
\boxed{
\widehat{\mathfrak P}_H
=2H+\sum_{j=1}^{C-1}(b_j-1).}
\tag{4.2}
\]

### Theorem 4.1 — exact useful-prefix fusion ledger

There is one integral nonzero literal word of exact length

\[
\boxed{W+\widehat{\mathfrak P}_H}
\tag{4.3}
\]

which exposes the whole useful radius-\(H\) prefix at every designated
middle endpoint.

#### Proof

Reverse-write the \(s=2H+1\) useful blocks of the first piece, use its
\(K_1-1\) principal core updates, insert an exact shortest prefix bridge,
and continue.  Tail insensitivity permits every subsequent principal
transition.  The length is

\[
\begin{aligned}
s+\sum_{j=1}^C(K_j-1)+\sum_{j=1}^{C-1}b_j
&=W+(s-1)+\sum_{j=1}^{C-1}(b_j-1)\\
&=W+\widehat{\mathfrak P}_H.
\end{aligned}
\]

All update masks and useful blocks are nonempty.  Every flag is a prefix
union of the final MTF state and therefore a literal suffix OR ending at
the corresponding physical position.  \(\square\)

The initial \(2H=s-1\) term is sharp for this architecture.  A common right
endpoint exposing the \(s\) distinct ranks \(m-H,\ldots,m+H\) needs \(s\)
distinct interval starts, hence at least \(s\) physical positions through
that endpoint.

If at every seam we discard any possible shortening and use an independent
useful-prefix reset, then a bridge of length \(s\) is available.  Consequently
\(b_j\le s\) for the shortest bridge and

\[
\boxed{
\widehat{\mathfrak P}_H\le 2HC.}
\tag{4.4}
\]

The explicit reset construction itself has exact excess \(2HC\); equality
in (4.4) for the *shortest* portal is neither asserted nor needed.

### 4.1 Cut-edge first-band colours

For a cut edge

\[
T\longrightarrow T'=T-\{p\}+\{q\},
\]

prescribe \(p\) as the first terminal dummy departure of the left piece and
as the first initial upper singleton of the right piece.  The left terminal
lower depth-one mask is \(T-\{p\}=T\cap T'\), and the right initial upper
depth-one mask is \(T'\cup\{p\}=T\cup T'\).  Both are literal useful-prefix
flags, and no new physical position is needed.

The left dummy is legal after cutting every short positive run at its entry:
otherwise \(p\) would have entered within the preceding \(H\) steps and
that entry edge would also be a cut.  The remaining \(H-1\) dummies are
chosen from the common intersection of the final \(H+1\) states.  Incoming
upper and outgoing lower prescriptions on the same piece are independent.

Thus every certified two-sided-rainbow first-band edge colour, including a
deleted cut edge, survives arbitrary piece ordering.

---

## 5. Trace repair and the coefficient-one implication

Let \(e\) be the number of certified edges whose lower colours are pairwise
distinct and whose upper colours are separately pairwise distinct.  Put

\[
N_1=\binom{2m}{m-1}.
\]

Let \(\mathcal H_{\ge2}\) be the family of masks in signed depths
\(2,\ldots,H\) absent from the useful-prefix flags.  For a proper marked
coordinate set \(Z\), let \(h_R\) count holes with trace \(R\subseteq Z\)
and define the audited fixed-trace functional

\[
\Phi_Z(\mathcal H_{\ge2})
=\sum_{R\subseteq Z}
\min\left\{
h_R,
\nu(2m-|Z|)+\mathbf 1_{R\ne\varnothing}
\right\}.
\tag{5.1}
\]

The fixed-trace cylinder word covers every hole at that cost.  Appending the
missing first-band masks individually and then this cylinder word gives:

### Theorem 5.1 — facet--prefix--trace composition

\[
\boxed{
L_{\rm band}
\le
W+\widehat{\mathfrak P}_H
+2(N_1-e)
+\Phi_Z(\mathcal H_{\ge2}).}
\tag{5.2}
\]

Everything in (5.2) belongs to one chronology, one set of prefix bridges,
one boundary choice, and one literal word.  No separately optimized factor
or fractional owner is used.

### Corollary 5.2 — useful-prefix sufficient theorem

Assume that for every fixed \(A>0\), there is a sequence of common choices,
one for every sufficiently large \(m\), such that

\[
\widehat{\mathfrak P}_H
+2(N_1-e)
+\Phi_Z(\mathcal H_{\ge2})
=o_A(W).
\tag{5.3}
\]

Then

\[
\boxed{\nu(k)\le(1+o(1))W(k).}
\tag{5.4}
\]

#### Proof

Equation (5.2) gives a \(W+o_A(W)\) word for the fixed Gaussian band.  The
audited SCD-product tails outside that band have normalized cost

\[
T(A)=O((1+A^2)e^{-A^2}),
\]

so

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}{W}
\le1+T(A).
\]

Let \(A\to\infty\) only after taking the fixed-\(A\) limsup.  Sperner's
lower bound gives equality.  Finally

\[
\nu(2m+1)\le2\nu(2m)+1,
\qquad
\binom{2m+1}{m}
=\frac{2m+1}{m+1}W,
\]

which transfers coefficient one to odd dimensions.  \(\square\)

Its synchronization requirement and numerical ledger are weaker than
full-state PTAD: for every seam,

\[
d_{\rm pref}^+(\Sigma,\Lambda)
\le d_{\rm MTF}^+(\Sigma,\Pi)
\]

for every full target state \(\Pi\) extending \(\Lambda\), and (1.8)--(1.9)
show that the abstract endpoint-state gap may equal \(2H+1\).  Since that
example is not an owner-changing seam, strict existential separation on
realizable vertex-disjoint spanning path systems is not claimed.

### 5.1 Exact odd-factor application

The cut exact odd factor has

\[
C=\frac{W}{m+1}
\]

no-return complementary geodesics and exactly partitions both first-band
edge-colour ranks, so \(e=N_1\).  By (4.4), shortest useful-prefix bridges
satisfy

\[
\boxed{
\widehat{\mathfrak P}_H
\le\frac{2HW}{m+1}=o_A(W).}
\tag{5.5}
\]

Equivalently, using the explicit independent reset at every seam gives a
word of exact length

\[
\boxed{
W+\frac{2HW}{m+1}.}
\tag{5.6}
\]

It covers the complete first band literally, its component paths have no
finite positive runs, and all residual tails may be inherited/refined.  The
only unproved term in (5.2) is now

\[
\boxed{
\Phi_Z(\mathcal H_{\ge2})=o_A(W).}
\tag{5.7}
\]

---

## 6. Sharp support obstruction after prefix fusion

The useful-prefix theorem removes a state-synchronization obstruction; it
does not create target support.

### Theorem 6.1 — deepest-core endpoint bound

Suppose a raw useful-prefix word has length \(W+E\) and has one designated
principal endpoint per middle owner.  The letter at principal endpoint
\(t\) is a core

\[
L_t\in\binom{[2m]}{m-H}.
\]

Then its represented rank-\((m-H)\) family satisfies

\[
\boxed{
|\mathcal R_{m-H}|
\le |\{L_t\}|+E.}
\tag{6.1}
\]

#### Proof

If a rank-\((m-H)\) target \(S\) has a witness ending at principal position
\(t\), then the endpoint letter satisfies \(L_t\subseteq S\).  Since both
sets have size \(m-H\), necessarily \(S=L_t\).  At each of the remaining
\(E\) physical positions, all intervals ending there form a nested chain,
so at most one distinct rank-\((m-H)\) target can end there.  Summing proves
(6.1).  This includes arbitrary seam-crossing intervals.  \(\square\)

If a completion appends \(R\) further positions and covers all \(N_H\)
targets, (6.1) gives

\[
E+R\ge
N_H-|\{L_t\}|.
\tag{6.2}
\]

Since also \(E+R\ge E\), every such completion obeys

\[
\boxed{
L-W\ge
\max\left\{
E,
N_H-|\{L_t\}|
\right\}.}
\tag{6.3}
\]

Therefore \(E=o(W)\) and coefficient-one length force

\[
\boxed{
|\{L_t\}|\ge N_H-o(W).}
\tag{6.4}
\]

The lower sandwich \(\Phi_Z\ge M_H^-\) is the same obstruction in trace
language.  Neither an inherited residual tail nor incidental cross-interval
witnesses can conceal a linear deepest-core collapse.

### 6.1 Frozen-chronology support stability at every depth

For a fixed no-return chronology, all lower flags before the final \(H\)
states of a component are forced future-deletion intersections.  After the
first \(H\) transitions, the useful upper queue is forced to

\[
(p_{t-1},\ldots,p_{t-H}),
\]

independently of every inherited tail and prefix bridge.  Thus at most
\(HC\) principal endpoints per sign and depth are boundary-variable.

Fix one sign and depth \(q\), and let

\[
D_q=N_q-|\mathcal S_{q,\rm int}|
\]

be the defect of the stable interior canonical support.  If the raw prefix-
portal excess is \(E\), every literal completion satisfies

\[
\boxed{
L-W\ge\max\{E,D_q-HC\}.}
\tag{6.5}
\]

Indeed, a stable principal endpoint already ends its designated canonical
rank-\((m\pm q)\) suffix.  All intervals ending there form a chain, so it
cannot end a second distinct target of the same rank.  Boundary principal
endpoints can add at most \(HC\) missing targets, and every nonprincipal or
repair position can add at most one.  If stable certificates are
surrendered, their number must be added to the boundary/nonprincipal
capacity; (6.5) is explicitly a fixed-certificate theorem.

For the exact odd factor,

\[
HC=\frac{HW}{m+1}=o_A(W).
\]

Hence any \(\Omega(W)\) interior defect at one rank survives every
useful-prefix, residual-tail, and shared-endpoint fusion of that frozen
chronology.

---

## 7. Exact pervasive-recoding and endpoint-reuse barriers

The preceding construction is necessarily a pervasive overlapping recoding
of the old facet word.  The following theorem quantifies that necessity
without assuming private blocks.

Let \(B_1,\ldots,B_n\) be a template word.  Suppose exactly \(b\) template
letters have size at most \(r\), while the remaining \(h=n-b\) high
template letters are pairwise distinct.  Let a final word
\(A_1,\ldots,A_L\) cover all \(N\) distinct rank-\(r\) targets.  For every
template letter choose a nonempty designated interval \(I_i\) of the final
word whose OR is \(B_i\).  The intervals may overlap arbitrarily.

Put

\[
E=L-n,
\qquad
R=\#\{j:j\notin I_i\text{ for all }i\},
\tag{7.1}
\]

and define total interval-incidence reuse

\[
O=\sum_{i=1}^{n}|I_i|-\left|\bigcup_{i=1}^{n}I_i\right|.
\tag{7.2}
\]

### Theorem 7.1 — overlapping interval-recoding trilemma

\[
\boxed{
2E+O\ge N-b+R.}
\tag{7.3}
\]

#### Proof

Let

\[
P=\#\{j:|A_j|\le r\}.
\]

Fixed-rank endpoint injection gives \(P\ge N\), so at most \(L-P\)
physical letters are high.  If a high template letter has a singleton
witness interval, it equals that high physical letter.  Since the high
template letters are pairwise distinct, at most \(L-P\) of them can have
singleton witnesses.  Thus at least

\[
x\ge h-L+P\ge h-L+N
\]

high template intervals have length at least two.  Therefore

\[
\sum_i(|I_i|-1)\ge x\ge h-L+N.
\tag{7.4}
\]

On the other hand,

\[
\begin{aligned}
\sum_i(|I_i|-1)
&=(L-R)+O-n\\
&=E+O-R.
\end{aligned}
\tag{7.5}
\]

Since \(h=n-b\) and \(L=n+E\), combining (7.4)--(7.5) gives (7.3).
\(\square\)

### 7.1 Exact application to the singleton-capped facet braid

For a globally lower-rainbow spanning forest, let \(c_+\) be the number of
nontrivial components.  Its singleton-capped template has

\[
n=W+c_+,
\qquad b=2c_+.
\]

The other \(W-c_+\) letters are the pairwise distinct lower facets together
with the isolated middle masks; they are pairwise distinct even across the
two ranks.

Take \(r=m-H\), \(N=N_H\), and write the final length as \(L=W+d\).  Then
\(E=d-c_+\), and (7.3) simplifies exactly to

\[
\boxed{
2d+O\ge N_H+R.}
\tag{7.6}
\]

At Gaussian depth,

\[
\frac{N_H}{W}=e^{-A^2}+o_A(1).
\]

Hence any \(d=o(W)\) fusion retaining every old template letter as some
interval requires

\[
O\ge(e^{-A^2}+o_A(1))W.
\tag{7.7}
\]

This rules out append-only fusion, private refinement, and every recoding
with sublinear total overlap.  The facet--core word in Section 3 escapes
exactly by using pervasive overlapping \(H\)-windows.

For depth two,

\[
N_2=\frac{m(m-1)}{(m+1)(m+2)}W,
\]

so (7.6) gives \(O=(1-o(1))W\) whenever \(d=o(W)\).

### 7.2 Endpoint-role version

For every high template interval, count its one endpoint if it is a
singleton and its two distinct endpoints otherwise.  If \(\lambda_j\) is
the number of these endpoint sets containing physical position \(j\), put

\[
\Omega_\partial=\sum_j(\lambda_j-1)_+.
\tag{7.8}
\]

The same singleton count gives total endpoint incidence at least
\(2h-(L-P)\).  Its union uses at most \(L\) positions.  Therefore

\[
\boxed{
\Omega_\partial\ge2h+N-2L.}
\tag{7.9}
\]

For the singleton-capped braid this becomes

\[
\boxed{
2d+\Omega_\partial\ge N_H-2c_+.}
\tag{7.10}
\]

At depth two, if \(e=N_1-\delta\), then

\[
c_+\le W-e=\frac{W}{m+1}+\delta,
\]

and the exact cancellation yields

\[
\boxed{
2d+\Omega_\partial
\ge\frac{m-4}{m+2}W-2\delta.}
\tag{7.11}
\]

Thus a coefficient-one depth-two fusion must have total endpoint-role reuse
multiplicity \(\Omega_\partial=(1-o(1))W\).  This reuse may concentrate at
high-degree positions.  If every physical position has endpoint-role
multiplicity at most \(D\ge2\), then the number of shared positions is at
least \(\Omega_\partial/(D-1)\).  The conclusion is compatible with, and
in fact explains, the overlapping facet-braid geometry of Section 3; it is
not an obstruction to that pervasive braid.

---

## 8. Audit and exact remaining scope

The decisive statements were independently reconstructed as follows.

1. The useful-prefix distance audit checked the positive-last-occurrence
   decomposition, the \(t_*=0\) convention, the \(s=2H+1\) block count,
   and the exact ledger \(2H+\sum(b_j-1)\).  No off-by-one remains.
2. The residual-splitting example was checked against the exact full-state
   bridge metric.  Its scope is explicitly limited to strictness of the two
   metrics, not an owner-changing seam theorem.
3. The facet--core identities were proved coordinatewise and independently
   checked.  The upper formula (3.9) now includes the necessary refresh and
   padded-domain hypotheses; no unqualified raw-history claim remains.
4. The deepest-core bound uses the physical endpoint letter itself, not an
   occurrence ledger.  It therefore includes arbitrary cross-seam
   intervals and proves the exact lower sandwich (6.3).
5. The all-depth frozen-support bound (6.5) is stated only for stable
   principal endpoints retaining their designated suffix certificates.
6. The overlap trilemma and endpoint-role inequality were derived from
   fixed-rank endpoint injection with no private-block or bounded-overlap
   assumption.
7. The one-letter initialization saving uses an explicit unseen-residual
   convention.  Every useful block still has positive last occurrence, so
   every advertised flag remains a literal suffix OR; no residual block is
   charged or used as a target witness.

What is proved:

* exact literal fusion of the first-band facet braid into one prefix-portal
  word, with every guarded path interior realized by low-core windows;
* exact useful-prefix portal distance and word length;
* strict removal of compact-residual synchronization;
* preservation of all certified cut-edge first-band colours;
* an unconditional \(W+2HW/(m+1)\) exact odd-factor core word;
* the precise Prefix-PTAD implication to coefficient one;
* exact deepest-support and pervasive-overlap necessities.

What remains **unproved** is only the existence, for every fixed \(A\), of
one common chronology and trace set with

\[
\widehat{\mathfrak P}_H
+2(N_1-e)
+\Phi_Z(\mathcal H_{\ge2})=o_A(W).
\]

For the exact odd factor the first two terms are already \(o_A(W)\), leaving
only \(\Phi_Z=o_A(W)\).  Theorem 6.1 proves that this cannot be obtained by
residual-tail manipulation when the forced deepest core support has linear
defect.  Any successful chronology—possibly the exact odd factor itself—
must have near-surjective deepest cores together with trace-compressible
higher holes.

No claim of MWB, labelled common-owner synchronization, or the full
coefficient-one theorem is made.
