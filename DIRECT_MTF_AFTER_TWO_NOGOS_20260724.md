# Direct MTF after the component-noise and three-box no-go results

## Status

This note does **not** prove

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

It gives a strict reduction of the surviving direct-MTF **ledger**.  The old
fixed-window target \(\mathrm{AD}_A\) charged

1. \(2H+1\) fresh initialization entries for every MTF path piece; and
2. every missing canonical mask literally, separately at every depth.

Neither charge is intrinsic.  The first can be replaced by the exact MTF
bridge distance between consecutive endpoint states.  The second can be
replaced by a cutoff-free trace functional in which one word repairs an
entire trace cylinder simultaneously at all depths.

The resulting **portal--trace adaptive theorem** is numerically weaker than
\(\mathrm{AD}_A\) on abstract defect ledgers.  Realizability of the
separating ledger by adaptive-MTF data is not proved.  The theorem also
identifies the exact scope of the improvement:
trace sharing cannot conceal a linear defect in one rank, but it can compress
a cumulative \(\Theta(W)\) defect spread across a Gaussian number of ranks.

Throughout this note

\[
n=2m,\qquad W=\binom{2m}{m},\qquad
H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\), unless explicitly stated otherwise.

---

## 1. Imported adaptive-MTF states

The audited adaptive-MTF theorem associates to an \(H\)-legal oriented
Johnson path

\[
T_0,T_1,\ldots,T_{K-1}\in\binom{[2m]}m
\]

ordered-partition states

\[
\Pi_0,\Pi_1,\ldots,\Pi_{K-1}
\]

with the following properties.

* \(\Pi_i\) exposes one canonical mask in every rank
  \(m-H,\ldots,m+H\), including \(T_i\) in rank \(m\).
* There is one nonempty update mask taking \(\Pi_i\) to \(\Pi_{i+1}\).
* The canonical initial state has exactly
  \[
  s=2H+2
  \tag{1.1}
  \]
  nonempty blocks: one lower core, \(H\) future-departure singletons,
  \(H\) upper-queue singletons, and one residual block.

The usual construction initializes every path independently by writing the
\(s\) blocks of \(\Pi_0\) in reverse order.  For a spanning family of \(C\)
paths, this gives the familiar length

\[
W+(s-1)C=W+(2H+1)C.
\tag{1.2}
\]

We first replace (1.2) by an exact bridge ledger.

---

## 2. Exact portal sharing between MTF pieces

For a nonempty mask \(X\), write \(M_X(\Pi)\) for the move-to-front update
of an ordered partition \(\Pi\).

### Lemma 2.1 — reverse-block reset

Let

\[
\Pi=(B_1,B_2,\ldots,B_s)
\]

be an ordered partition of the ground set into nonempty blocks.  From an
arbitrary preceding state, the word

\[
B_s,B_{s-1},\ldots,B_1
\tag{2.1}
\]

ends in state \(\Pi\).

#### Proof

The blocks are pairwise disjoint and partition the ground set.  After all
updates in (2.1), their last occurrences are in the reverse chronological
order \(B_1,B_2,\ldots,B_s\).  Every older residual block has been deleted,
because its elements lie in one of the \(B_i\).  Hence the final
last-occurrence partition is exactly \(\Pi\).  \(\square\)

The preceding reset need not be used in full.

For an ordered partition \(\Sigma=(C_1,\ldots,C_r)\) and a mask \(X\),
write

\[
D_X(\Sigma)
=(C_1\setminus X,\ldots,C_r\setminus X),
\tag{2.2}
\]

with empty blocks deleted.

### Lemma 2.2 — exact one-update portal criterion

For a target partition

\[
\Pi=(B_1,B_2,\ldots,B_s),
\]

one nonempty update takes \(\Sigma\) to \(\Pi\) if and only if

\[
\boxed{D_{B_1}(\Sigma)=(B_2,\ldots,B_s).}
\tag{2.3}
\]

#### Proof

By definition,

\[
M_X(\Sigma)=(X,D_X(\Sigma)).
\]

Equality with \(\Pi\) forces \(X=B_1\) and then forces precisely (2.3).
The converse is immediate.  \(\square\)

This criterion permits pieces of \(B_1\) to be distributed among old
blocks; literal equality of the visible old blocks with
\(B_2,\ldots,B_s\) is not required.  The following easier sufficient
criterion is useful for accounting.

### Lemma 2.3 — suffix-overlap bridge

Let \(\Sigma\) be the current ordered-partition state and let

\[
\Pi=(B_1,\ldots,B_s)
\]

be the desired state.  Suppose \(\Sigma\) begins with the last \(\kappa\)
blocks of \(\Pi\), in their target order:

\[
\Sigma=
(B_{s-\kappa+1},\ldots,B_s,\ldots).
\tag{2.4}
\]

If \(\kappa<s\), appending

\[
B_{s-\kappa},B_{s-\kappa-1},\ldots,B_1
\tag{2.5}
\]

ends in state \(\Pi\).  If \(\kappa=s\), the one-letter update \(B_1\)
leaves the state equal to \(\Pi\).  Thus a nonempty bridge of length

\[
b\le \max\{1,s-\kappa\}
\tag{2.6}
\]

always exists under (2.4).

#### Proof

The displayed leading blocks in \(\Sigma\) have union

\[
B_{s-\kappa+1}\cup\cdots\cup B_s.
\]

All later blocks of \(\Sigma\) therefore partition the complementary union
\(B_1\cup\cdots\cup B_{s-\kappa}\).  The updates (2.5) remove all those
later residual pieces, leave the displayed leading blocks unchanged, and
place the missing target blocks at the front in the order
\(B_1,\ldots,B_{s-\kappa}\).  This gives \(\Pi\).  When \(\kappa=s\),
\(B_1\) is already the leading block, so updating by \(B_1\) leaves the
partition unchanged.  \(\square\)

Now let

\[
\mathcal P_j=(T_{j,0},\ldots,T_{j,K_j-1}),
\qquad 1\le j\le C,
\]

be vertex-disjoint \(H\)-legal paths which partition the whole middle
layer, so \(\sum_jK_j=W\).  Choose an order of the paths.  Let \(b_j\ge1\)
be the minimum length of a nonempty MTF word taking the terminal state of
\(\mathcal P_j\) exactly to the initial state of \(\mathcal P_{j+1}\).
Denote this minimum by \(d_{\rm MTF}(\Pi_j^{\rm end},
\Pi_{j+1}^{\rm start})\).  It is finite and at most \(s\) by Lemma 2.1.

Define the **portal excess**

\[
\boxed{
\mathfrak P_H
=(s-1)+\sum_{j=1}^{C-1}(b_j-1).
}
\tag{2.7}
\]

### Theorem 2.4 — exact shared-reset ledger

The path states above are realized by a literal nonzero word of length

\[
\boxed{W+\mathfrak P_H.}
\tag{2.8}
\]

It exposes every canonical signed-depth mask belonging to every path state.

#### Proof

Initialize the first path using (2.1), use its \(K_1-1\) one-step updates,
then use the first bridge, and continue.  The total number of entries is

\[
s+\sum_{j=1}^C(K_j-1)+\sum_{j=1}^{C-1}b_j
=W+(s-1)+\sum_{j=1}^{C-1}(b_j-1).
\]

The final endpoint of every bridge has exactly the prescribed initial
state of the next path.  Hence its suffix unions expose the first middle
vertex and all its canonical flags; subsequent one-step states do the same
inside the path.  All entries used in resets, bridges, and path updates are
nonempty.  \(\square\)

Independent resets correspond to \(b_j=s\), in which case
\(\mathfrak P_H=(s-1)C\) and (2.8) is exactly (1.2).  On the other hand, if
all seams are one-update portals, then

\[
\mathfrak P_H=s-1=2H+1,
\tag{2.9}
\]

regardless of \(C\).

If \(\kappa_j\) is a suffix overlap as in Lemma 2.3, then

\[
\boxed{
\mathfrak P_H
\le s-1+
\sum_{j=1}^{C-1}(s-\kappa_j-1)_+.
}
\tag{2.10}
\]

Thus only seams which fail to be almost complete portals need pay an
\(H\)-scale reset cost.  For example, if at most \(B\) seams are reset from
scratch and all others are one-update portals, then

\[
\mathfrak P_H\le 2H+1+(2H+1)B.
\tag{2.11}
\]

The sufficient condition is \(B=o(W/H)\), not \(C=o(W/H)\).

Equivalently, for fixed boundary states put a directed complete graph on the
pieces with weight

\[
w(i,j)=d_{\rm MTF}(\Pi_i^{\rm end},\Pi_j^{\rm start})-1
\in\{0,1,\ldots,s-1\}.
\tag{2.12}
\]

Then the least portal excess over all orders of the pieces is exactly

\[
\boxed{
s-1+min_{\sigma\in S_C}
\sum_{j=1}^{C-1}w(\sigma_j,\sigma_{j+1}).
}
\tag{2.13}
\]

Thus shared initialization is a finite directed Hamilton-path functional on
the actual endpoint states, not an informal appeal to amortization.

---

## 3. One trace word repairs all depths

Let \(\mathcal H\) be any family of nonempty Boolean masks on \([n]\).
Later it will be the family of canonical masks missing from the MTF word.

Fix a proper marked coordinate set

\[
Z\subsetneq[n],\qquad |Z|=t,
\]

and put \(X=[n]\setminus Z\), \(|X|=d=n-t\).  For every trace
\(R\subseteq Z\), define

\[
h_R=\#\{S\in\mathcal H:S\cap Z=R\}
\tag{3.1}
\]

and

\[
\ell_R=\nu(d)+\mathbf1_{\{R\ne\varnothing\}}.
\tag{3.2}
\]

Define the cutoff-free **trace repair functional**

\[
\boxed{
\Phi_Z(\mathcal H)
=\sum_{R\subseteq Z}\min\{h_R,\ell_R\}.
}
\tag{3.3}
\]

### Lemma 3.1 — fixed-trace cylinder word

Every nonempty mask \(S\subseteq[n]\) with \(S\cap Z=R\) is covered by a
literal word of length at most \(\ell_R\).

#### Proof

Take a universal nonzero word

\[
V_1,\ldots,V_{\nu(d)}
\]

on \(X\).  If \(R=\varnothing\), use this word itself.  If
\(R\ne\varnothing\), use

\[
R,\quad R\cup V_1,\ldots,R\cup V_{\nu(d)}.
\tag{3.4}
\]

For \(S=R\cup T\) with nonempty \(T\subseteq X\), lift an interval of the
\(V\)-word whose union is \(T\).  The corresponding interval in (3.4) has
union \(R\cup T\).  If \(T=\varnothing\), then \(R\ne\varnothing\) and
the first entry of (3.4) is the target.  \(\square\)

### Theorem 3.2 — exact trace repair

There is a literal nonzero word of length at most

\[
\boxed{\Phi_Z(\mathcal H)}
\tag{3.5}
\]

covering every member of \(\mathcal H\).

#### Proof

For each trace \(R\), either append its \(h_R\) targets literally or append
the fixed-trace cylinder word from Lemma 3.1, whichever is shorter.  The
trace classes are independent, and concatenation preserves every internal
witness.  Summing the cheaper costs gives (3.5).  \(\square\)

The functional sits exactly between the largest one-rank defect and the raw
sum of all defects.  Suppose

\[
\mathcal H=\bigsqcup_{r\in\mathcal R}\mathcal H_r,
\qquad
\mathcal H_r\subseteq\binom{[n]}r,
\]

and write \(M_r=|\mathcal H_r|\).  Then

\[
\boxed{
\max_{r\in\mathcal R}M_r
\le\Phi_Z(\mathcal H)
\le\sum_{r\in\mathcal R}M_r.
}
\tag{3.6}
\]

Indeed, the upper bound follows from \(\min(h_R,\ell_R)\le h_R\).  For the
lower bound, put

\[
h_{r,R}=\#\{S\in\mathcal H_r:S\cap Z=R\}.
\]

For every \(r,R\),

\[
h_{r,R}
\le\binom d{r-|R|}
\le\binom d{\lfloor d/2\rfloor}
\le\nu(d)
\le\ell_R.
\tag{3.7}
\]

Since also \(h_{r,R}\le h_R\), one has
\(h_{r,R}\le\min(h_R,\ell_R)\).  Sum over \(R\) to get
\(M_r\le\Phi_Z(\mathcal H)\).

Thus trace compression respects the endpoint-throughput obstruction: it
cannot hide \(\Theta(W)\) holes in one depth.  Its only possible gain is
reuse across different ranks.

---

## 4. The portal--trace adaptive theorem

For the spanning state paths of Section 2, let

\[
\mathcal S_q^-\subseteq\binom{[2m]}{m-q},
\qquad
\mathcal S_q^+\subseteq\binom{[2m]}{m+q}
\]

be the supports of their canonical flags.  Define the canonical hole family

\[
\mathcal H_H=
\bigsqcup_{q=1}^H
\left[
\left(\binom{[2m]}{m-q}\setminus\mathcal S_q^-\right)
\sqcup
\left(\binom{[2m]}{m+q}\setminus\mathcal S_q^+\right)
\right].
\tag{4.1}
\]

The middle layer has no holes because the paths span it.

### Theorem 4.1 — exact central-band bound

For every proper marked set \(Z\subsetneq[2m]\), the whole band

\[
m-H,m-H+1,\ldots,m+H
\]

has a literal nonzero contiguous-OR word of length at most

\[
\boxed{
W+\mathfrak P_H+\Phi_Z(\mathcal H_H).
}
\tag{4.2}
\]

#### Proof

Theorem 2.4 gives the physical MTF word of length
\(W+\mathfrak P_H\), covering the middle layer and every canonical flag.
The only masks in the declared band not certified by those supports belong
to \(\mathcal H_H\).  Append the trace-repair word of Theorem 3.2.  \(\square\)

This yields the following new compact sufficient statement.

> **Portal--trace adaptive theorem \(\mathrm{PTAD}_A\) — unproved.**  For
> every fixed \(A>0\), with \(H=\lceil A\sqrt m\rceil\), construct one
> spanning family of \(H\)-legal adaptive-MTF paths, one ordering and bridge
> system, and one marked set \(Z=Z_{m,A}\), such that
> \[
> \boxed{
> \mathfrak P_H+\Phi_Z(\mathcal H_H)=o(W).
> }
> \tag{PTAD_A}
> \]

### Theorem 4.2 — implication to coefficient one

If \(\mathrm{PTAD}_A\) holds for every fixed \(A>0\), then

\[
\boxed{
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
}
\tag{4.3}
\]

#### Proof

For fixed \(A\), Theorem 4.1 gives a central-band word of length
\(W+o_A(W)\).  The independently audited symmetric-chain-product word
covers both tails outside the band with normalized cost

\[
T(A)=O((1+A^2)e^{-A^2}),
\qquad T(A)\longrightarrow0.
\tag{4.4}
\]

Hence

\[
\limsup_{m\to\infty}\frac{\nu(2m)}W\le1+T(A).
\]

First let \(m\to\infty\) for fixed \(A\), then let \(A\to\infty\).
Sperner's lower bound gives the reverse inequality.  Finally use the standard
one-bit lift

\[
\nu(2m+1)\le2\nu(2m)+1
\]

and

\[
\binom{2m+1}{m}
=\frac{2m+1}{m+1}\binom{2m}{m}
\]

to transfer coefficient one to odd dimension.  \(\square\)

---

## 5. Relation to the old adaptive theorem and the first-band forest

The new target is genuinely weaker than \(\mathrm{AD}_A\).

Suppose the audited adaptive construction cuts a two-sided-rainbow forest
into \(C=c+\rho_H\) pieces and resets every piece independently.  Then

\[
\mathfrak P_H=(2H+1)C.
\tag{5.1}
\]

If \(e\) first-band colours are certified separately on the two signs, then
the number of canonical first-band holes is at most \(2(N_1-e)\).  Therefore

\[
\Phi_Z(\mathcal H_H)
\le
2(N_1-e)+
\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+).
\tag{5.2}
\]

The old \(\mathrm{AD}_A\) hypotheses imply \(\mathrm{PTAD}_A\) immediately.

More usefully, the already-proved two-sided-rainbow forest makes the first
term on the right of (5.2) \(o(W)\) when it is refactored using the audited
colour-preserving adaptive-MTF boundary choices.  Thus, starting from that
forest and those boundary choices, it is enough to prove the no-stronger
higher-depth condition

\[
\boxed{
\mathfrak P_H+
\Phi_Z\!\left(
\bigsqcup_{q=2}^H(\mathcal H_q^-\sqcup\mathcal H_q^+)
\right)
=o(W).
}
\tag{5.3}
\]

No separate first-shadow factorability or pin-survival statement remains:
the adaptive MTF word is physical, and its depth-one edge colours are the
old intersection and union colours.

There are two independent relaxations in (5.3).

* Shared portals replace \((2H+1)C\) by the true bridge excess
  \(\mathfrak P_H\).
* Cross-depth trace repair replaces the raw sum of support defects by
  \(\Phi_Z\).

Neither relaxation assumes an exact wreath factor, fractional balancing, or
the now-disproved compact-balanced three-box theorem.

---

## 6. A concrete trace-clustering corollary

The functional has a transparent asymptotic sufficient condition.  Assume

\[
t=|Z|\longrightarrow\infty,
\qquad t=o(m),
\tag{6.1}
\]

and let

\[
J_Z(\mathcal H)
=\#\{R\subseteq Z:h_R>0\}
\tag{6.2}
\]

be the number of active traces.

The unconditional bound \(\nu(d)=O(W(d))\), together with central-binomial
asymptotics, gives uniformly under (6.1)

\[
\nu(2m-t)+1
\le
O\!\left(
2^{-t}\sqrt{\frac{2m}{2m-t}}\,W
+1
\right)
=O(2^{-t}W+1).
\tag{6.3}
\]

Consequently

\[
\boxed{
\Phi_Z(\mathcal H)
\le
O\!\left(J_Z(\mathcal H)2^{-t}W+J_Z(\mathcal H)\right).
}
\tag{6.4}
\]

### Corollary 6.1 — subdense trace support

If

\[
J_Z(\mathcal H)=o(2^t),
\tag{6.5}
\]

then \(\Phi_Z(\mathcal H)=o(W)\).  In particular, for any fixed
\(\delta>0\), the stronger but simpler condition

\[
J_Z(\mathcal H)\le2^{(1-\delta)t}
\tag{6.6}
\]

is sufficient.

#### Proof

The first term in (6.4) is \(o(W)\).  The second is also \(o(W)\), because
\(J_Z=o(2^t)\), \(t=o(m)\), and \(2^t=o(W)\).  \(\square\)

Thus a particularly concrete replacement for the deep-support part of
\(\mathrm{AD}_A\) is:

> Find one slowly growing marked coordinate set for which all higher
> canonical holes, across all \(2H-2\) signed ranks together, occupy only
> \(o(2^t)\) traces.

The total number of holes in those traces need not be \(o(W)\).

---

## 7. The abstract ledger is strictly weaker at Gaussian depth

The strictness can be seen without assuming that the following abstract hole
pattern is realized by a particular forest.

Take the even integer

\[
t=2\left\lfloor\frac14\log_2m\right\rfloor
=\frac12\log_2m+O(1),
\]

choose \(Z\) of size \(t\), and fix one trace \(R\subseteq Z\) of size
\(t/2\).  Put \(d=2m-t\), and for every
\(1\le q\le A\sqrt m\) declare missing all rank-\((m-q)\) masks having
trace \(R\).  The raw aggregate defect is

\[
\begin{aligned}
D_m
&=\sum_{q=1}^{\lceil A\sqrt m\rceil}
\binom d{d/2-q}\\
&=\Theta_A(\sqrt m\,W(d))
=\Theta_A(W),
\end{aligned}
\tag{7.1}
\]

by the central local limit estimate and
\(W(d)/W=(1+o(1))2^{-t}=\Theta(m^{-1/2})\).

But there is only one active trace, so

\[
\Phi_Z\le\nu(d)+1=O(W(d))=O(W/\sqrt m)=o(W).
\tag{7.2}
\]

At each individual depth the defect is only \(O(W/\sqrt m)=o(W)\), in
accordance with the lower bound in (3.6).  The entire saving comes from
using one trace-cylinder word across \(\Theta(\sqrt m)\) ranks.

This example proves that the new **ledger condition** is asymptotically
strictly weaker than raw defect summability at exactly the Gaussian window
relevant to the direct theorem.  It is not asserted that this particular
abstract hole family occurs as the canonical defect of an adaptive forest;
that realizability question is part of the remaining construction problem.

---

## 8. What this says about depth two

The trace functional does **not** permit a macroscopic depth-two defect.
Equation (3.6) gives, for either sign,

\[
M_2^\pm\le\Phi_Z(\mathcal H_H).
\tag{8.1}
\]

Hence \(\mathrm{PTAD}_A\) still forces \(M_2^\pm=o(W)\).  This is not a
weakness of the proof: one right endpoint can represent at most one mask of
a fixed rank, so an \(o(W)\)-length appendage cannot repair
\(\Theta(W)\) missing masks in that rank.

What may be structured and large is the **cumulative** defect over depths.
The correct weakened target is therefore not “allow \(\Theta(W)\) holes at
depth two,” but rather:

\[
M_q^\pm=o(W)\quad\text{for each fixed or moving }q,
\]

while a common low-entropy trace geometry allows

\[
\sum_{q\le H}(M_q^-+M_q^+)
\]

to be as large as \(\Theta(W)\) (or more) without paying that sum in the
word length.

---

## 9. Self-audit and exact remaining problem

The proof uses only four imported facts.

1. The audited adaptive-MTF theorem supplies the physical saturated state
   paths.
2. The current unconditional global upper bound gives
   \(\nu(d)=O(W(d))\) for the smaller trace cube.
3. Sperner gives \(\nu(d)\ge W(d)\), used in the lower sandwich (3.6).
4. The audited SCD-product construction gives the tail cost (4.4).

No probabilistic rounding, product-box equality, exact wreath factor, or
component-noise inequality is used.

The appeal to \(\nu(d)=O(W(d))\) is noncircular: the already-proved
\((\sqrt2+o(1))W(d)\) upper bound is enough.  No coefficient-one estimate in
dimension \(d\) is assumed.

The quantifiers in \(\mathrm{PTAD}_A\) are joint.  The paths, their order,
their terminal dummies and residual queues, the bridge words, and the marked
set \(Z\) must all belong to one common construction.  Separate minimizers
of portal cost and trace entropy do not suffice.

The remaining direct theorem can now be stated briefly.

> **Exact remaining direct-MTF problem.**  For every fixed \(A>0\), orient
> and cut one spanning Johnson chronology, choose all canonical adaptive-MTF
> boundary data, order its pieces, and choose a marked set \(Z\), so that
> \[
> \mathfrak P_H+
> \sum_{R\subseteq Z}
> \min\left\{
> \#\{\text{canonical band holes of trace }R\},
> \nu(2m-|Z|)+\mathbf1_{R\ne\varnothing}
> \right\}
> =o(W).
> \]

This theorem is unproved.  At the level of numerical portal/defect ledgers it
is strictly weaker than the surviving \(\mathrm{AD}_A\) statement in both
nontrivial terms.  Whether the strict abstract separation occurs for
realizable adaptive-MTF defects remains open.  The formulation itself remains
fully literal and integral.
