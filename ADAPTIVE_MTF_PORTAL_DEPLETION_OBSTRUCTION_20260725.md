# Exact MTF portal distance and the residual-depletion obstruction

Date: 2026-07-25

## Status and main conclusion

This note does **not** prove the portal--trace adaptive theorem
\(\mathrm{PTAD}_A\), and therefore does not prove the constant-one upper
bound.  It proves a sharp obstruction to one of the two advertised escapes
in that theorem.

The portal distance between two ordered-partition states has an exact closed
form.  Applied to the canonical radius-\(H\) adaptive-MTF states, it gives the
following dichotomy.

* If a path consumes even one coordinate of its initial upper residual block,
  then every bridge from its terminal state to a fresh canonical initial
  state has length at least
  \[
  2H+1.
  \]
* A complete reverse-block reset has length \(2H+2\).

Thus a residual-consuming component can save at most one letter by portal
sharing.  Every cyclic strip with \(\ell>H\), and every complementary
geodesic obtained by cutting an odd wreath, is residual-consuming.  Hence:

1. for \(p\) selected strip components, the portal excess is at least
   \(2Hp+1\);
2. if their middle leave is \(o(W)\), then
   \[
   \mathfrak P_H=o(W)\quad\Longrightarrow\quad \ell/H\longrightarrow\infty;
   \]
3. the portal relaxation does not improve the leading reset order in the
   full-strip or odd-cut architectures;
4. combining this necessary ratio with the standard growing-uniformity
   economical-cover hypothesis gives the architecture ceiling
   \[
   H=o(\sqrt{\log m}).
   \]

The last conclusion is architecture-scoped: it rules out reaching a
Gaussian window by retuning full strips, the same matching black box, and
shared exact-state portals.  It is not an obstruction to a different
adaptive-MTF construction whose components preserve their residual blocks,
nor to trace repair.

Throughout,
\[
n=2m,
\qquad
W=\binom{2m}{m},
\qquad
1\le H<m,
\qquad
s=2H+2.
\]
The depletion and portal-support theorems additionally assume
\(m-H\ge2\).  The exceptional case \(m-H=1\) admits cheap portals and is
excluded; all asymptotic applications in this note satisfy the assumption.

---

## 1. The exact bridge metric on ordered partitions

Let
\[
\Sigma=(C_1,\ldots,C_r)
\]
be an ordered partition of \([n]\).  For a nonempty mask \(X\), the
move-to-front update is
\[
M_X(\Sigma)
=
(X,C_1\setminus X,\ldots,C_r\setminus X),
\tag{1.1}
\]
with empty blocks deleted.  For a mask \(U\), write
\[
D_U(\Sigma)
=
(C_1\setminus U,\ldots,C_r\setminus U),
\tag{1.2}
\]
again deleting empty blocks.

Fix a target state
\[
\Pi=(B_1,\ldots,B_s)
\]
and put
\[
U_t=B_1\cup\cdots\cup B_t
\qquad(0\le t\le s),
\tag{1.3}
\]
where \(U_0=\varnothing\).  Define
\[
t_*(\Sigma,\Pi)
=
\min\left\{
t\in\{0,1,\ldots,s\}:
D_{U_t}(\Sigma)=(B_{t+1},\ldots,B_s)
\right\}.
\tag{1.4}
\]
The set in (1.4) is nonempty because \(U_s=[n]\).  Let
\(d^+_{\rm MTF}(\Sigma,\Pi)\) be the minimum length of a **nonempty** MTF
word carrying \(\Sigma\) exactly to \(\Pi\).

### Theorem 1.1 — exact deletion-suffix formula

One has
\[
\boxed{
d^+_{\rm MTF}(\Sigma,\Pi)
=\max\{1,t_*(\Sigma,\Pi)\}.
}
\tag{1.5}
\]

Equivalently, if
\[
\kappa_*(\Sigma,\Pi)=s-t_*(\Sigma,\Pi),
\tag{1.6}
\]
then
\[
\boxed{
d^+_{\rm MTF}(\Sigma,\Pi)
=\max\{1,s-\kappa_*(\Sigma,\Pi)\}.
}
\tag{1.7}
\]

Here \(\kappa_*\) is a deletion-suffix overlap: the target prefix is first
deleted from the source state, and only then must the target suffix appear.
It is strictly more general than requiring the source state itself to begin
with that suffix.

#### Proof

Consider a word of \(k\) updates
\[
X_1,X_2,\ldots,X_k.
\]
The final last-occurrence partition consists first of the nonempty
differences
\[
X_k,
\quad
X_{k-1}\setminus X_k,
\quad\ldots,\quad
X_1\setminus\bigcup_{j=2}^kX_j,
\tag{1.8}
\]
in that order, and then of
\[
D_{X_1\cup\cdots\cup X_k}(\Sigma).
\tag{1.9}
\]
This follows either by induction from (1.1), or directly by grouping
coordinates according to their last positive update time.

If the final state is \(\Pi\), the nonempty blocks in (1.8) form a prefix
\(B_1,\ldots,B_t\) of \(\Pi\), with \(t\le k\).  Their union is \(U_t\),
and (1.9) is the remaining suffix.  Hence
\[
D_{U_t}(\Sigma)=(B_{t+1},\ldots,B_s),
\]
so \(t_*\le t\le k\).  Every nonempty bridge therefore has length at
least \(\max\{1,t_*\}\).

Conversely, suppose \(t=t_*>0\).  Apply the cumulative target prefixes in
the chronological order
\[
U_t,U_{t-1},\ldots,U_1.
\tag{1.10}
\]
After the first update the leading block is \(U_t\) and the residual state
is the target suffix.  Each subsequent update peels the last target block
off that leading union.  After all \(t\) updates the state is exactly
\[
(B_1,B_2,\ldots,B_t,B_{t+1},\ldots,B_s)=\Pi.
\]
If \(t_*=0\), then \(\Sigma=\Pi\), and the one-letter update \(B_1\) is
idempotent.  This proves (1.5). \(\square\)

### Corollary 1.2 — exact portal ledger

For ordered path pieces with terminal states \(\Sigma_j\) and initial states
\(\Pi_{j+1}\), put
\[
t_j=t_*(\Sigma_j,\Pi_{j+1}).
\]
Then the portal excess of the exact shared-reset ledger is
\[
\boxed{
\mathfrak P_H
=(s-1)+\sum_j(t_j-1)_+.
}
\tag{1.11}
\]
In deletion-overlap notation this is
\[
\boxed{
\mathfrak P_H
=(s-1)+\sum_j(s-\kappa_{*,j}-1)_+.
}
\tag{1.12}
\]

Thus the suffix-overlap expression previously available only as an upper
bound becomes an equality after replacing literal leading overlap by the
correct deletion-suffix overlap.

---

## 2. Canonical adaptive states and their residual block

For an \(H\)-legal oriented Johnson path
\[
T_0,T_1,\ldots,T_{K-1},
\qquad
T_{i+1}=T_i-\{p_i\}+\{q_i\},
\]
the canonical radius-\(H\) state is
\[
\Pi_i=
\bigl(
L_i,
\{p_{i+H-1}\},\ldots,\{p_i\},
\Theta_i
\bigr),
\tag{2.1}
\]
where
\[
|L_i|=m-H,
\qquad
\Theta_{i+1}=(\{p_i\},\Theta_i\setminus\{q_i\}).
\tag{2.2}
\]
At the beginning of a fresh component one chooses
\[
\Theta_0=
(\{z_1\},\ldots,\{z_H\},R_0),
\qquad
|R_0|=m-H.
\tag{2.3}
\]
Hence every fresh initial state has exactly \(s=2H+2\) blocks:
\[
\Pi^{\rm in}
=
\bigl(
B_1,
\{x_1\},\ldots,\{x_{2H}\},
B_s
\bigr),
\tag{2.4}
\]
with
\[
|B_1|=|B_s|=m-H.
\tag{2.5}
\]

The recurrence (2.2) has a simple invariant.  Every block of \(\Theta_i\)
other than its last residual block is a singleton.  Its last block is
\[
R_i=R_0\setminus\{q_j:q_j\in R_0,\ 0\le j<i\}.
\tag{2.6}
\]
It may become empty, in which case it is omitted.  In particular,
\[
|R_i|\le m-H,
\tag{2.7}
\]
and strict inequality holds as soon as one arrival is extracted from the
initial residual.

We call a path component **residual-consuming** when
\[
|R_{K-1}|<m-H.
\tag{2.8}
\]

---

## 3. The residual-depletion portal obstruction

The next result is the central new obstruction.

### Theorem 3.1 — a depleted component needs a near-full reset

Assume \(m-H\ge2\).
Let \(\Sigma\) be the terminal canonical state of a residual-consuming
radius-\(H\) path, and let \(\Pi\) be **any** fresh canonical initial state
of the form (2.4).  Then
\[
\boxed{
d^+_{\rm MTF}(\Sigma,\Pi)\ge s-1=2H+1.
}
\tag{3.1}
\]

Thus the bridge saves at most one letter relative to the universal
reverse-block reset of length \(s=2H+2\).

#### Proof

The terminal source state has the form
\[
\Sigma=(A,\text{singleton blocks},R),
\tag{3.2}
\]
where
\[
|A|=m-H,
\qquad
|R|<m-H,
\tag{3.3}
\]
and \(R\) may be empty.  The block \(A\) is first, \(R\) is last, and all
intermediate blocks are singletons.

Suppose for contradiction that
\[
t_*(\Sigma,\Pi)\le s-2.
\]
Then the target suffix in (1.4) contains at least two blocks.  Its last
block is the target residual \(B_s\), of size \(m-H\).

After deleting any mask from \(\Sigma\), a block of size \(m-H\) can only
come from \(A\): the intermediate blocks are singletons and \(|R|<m-H\).
For \(A\setminus U\) still to have size \(m-H\), the deleted mask must be
disjoint from \(A\).  Consequently \(A\) is the **first** surviving block
of \(D_U(\Sigma)\).  It cannot simultaneously be the last block of a
suffix containing at least two blocks.  This contradicts (1.4).

Therefore \(t_*\ge s-1\), and Theorem 1.1 proves (3.1). \(\square\)

The proof also gives the exact cheap-portal prerequisite.

### Corollary 3.2 — necessary invariant for a substantial portal

Assume \(m-H\ge2\).
If a terminal canonical state \(\Sigma\) admits a bridge of length at most
\(s-2\) to a fresh canonical state, then its upper residual is untouched:
\[
|R_{K-1}|=m-H.
\tag{3.4}
\]
Moreover the target residual block is exactly that same source residual
block.  Thus any bridge saving at least two letters from a full reset must
preserve and align an \((m-H)\)-set across the seam.

#### Proof

In a target suffix of length at least two, its final \((m-H)\)-block cannot
come from the first source block, by the order argument in Theorem 3.1.  It
must therefore come from the last source residual.  This forces the latter
to have size \(m-H\), to be disjoint from the deleted target prefix, and to
equal the target residual. \(\square\)

The lower bound is sharp as a statement about canonical source and target
layouts.  Let
\[
\Sigma=(A,\{x_1\},\ldots,\{x_{m+H}\}),
\qquad |A|=m-H.
\]
Partition \(\{x_1,\ldots,x_{m+H}\}\) into a target first block of size
\(m-H\) followed by \(2H\) singleton target blocks, and take target
residual \(A\).  Deleting the target prefix leaves exactly \((A)\), so
Theorem 1.1 gives distance \(s-1\).

### Theorem 3.3 — complete classification of one-update fresh portals

Assume \(m-H\ge2\).  Let both source and target be fresh canonical states,
written as
\[
\Sigma=(A,\{x_1\},\ldots,\{x_{2H}\},B),
\]
\[
\Pi=(A',\{y_1\},\ldots,\{y_{2H}\},B'),
\tag{3.5}
\]
where \(|A|=|A'|=|B|=|B'|=m-H\).  A one-update portal from \(\Sigma\) to
\(\Pi\) exists if and only if either \(\Pi=\Sigma\), or there are
\[
a\in A,
\qquad
j\in\{1,\ldots,2H\}
\]
such that
\[
\boxed{
\begin{aligned}
B'&=B,\\
A'&=A-\{a\}+\{x_j\},\\
(y_1,\ldots,y_{2H})
&=(a,x_1,\ldots,x_{j-1},x_{j+1},\ldots,x_{2H}).
\end{aligned}}
\tag{3.6}
\]

In particular, every one-update run of fresh canonical states preserves the
same residual \((m-H)\)-set.

#### Proof

The one-update criterion is
\[
D_{A'}(\Sigma)
=(\{y_1\},\ldots,\{y_{2H}\},B').
\tag{3.7}
\]
Put
\[
k=|A'\cap\{x_1,\ldots,x_{2H}\}|,
\quad
a_0=|A\setminus A'|,
\quad
b_0=|B\setminus A'|.
\]
Because \(|A'|=m-H\),
\[
a_0+b_0=m-H+k.
\tag{3.8}
\]
The last target block has size \(m-H\ge2\).  It cannot come from a source
singleton.  It also cannot come from \(A\setminus A'\), because that block
precedes every surviving source singleton while the target large block is
last.  Hence it must be \(B\setminus A'\), forcing
\[
b_0=m-H,
\qquad
A'\cap B=\varnothing,
\qquad
B'=B.
\tag{3.9}
\]
Equation (3.8) now gives \(a_0=k\).

If \(k=0\), then \(a_0=0\), so \(A'=A\), and (3.7) forces
\(\Pi=\Sigma\).  If \(k>0\), the block \(A\setminus A'\) occurs as one
additional block before the surviving source singletons.  The target has
exactly \(2H\) singleton blocks.  Hence
\[
1+(2H-k)=2H,
\]
so \(k=a_0=1\).  Writing
\[
A\setminus A'=\{a\},
\qquad
A'\cap\{x_1,\ldots,x_{2H}\}=\{x_j\}
\]
gives exactly (3.6).  Conversely, direct deletion of \(A'\) from \(\Sigma\)
gives the target suffix in (3.6), so the displayed conditions are
sufficient. \(\square\)

There is a useful middle-layer interpretation.  In the canonical layout the
middle mask is
\[
T=A\cup\{x_1,\ldots,x_H\}.
\tag{3.10}
\]
Under (3.6), if \(j\le H\) then the target state exposes the same middle
mask.  If \(j>H\), it exposes the Johnson neighbour
\[
T'=T-\{x_H\}+\{x_j\}.
\tag{3.11}
\]
Thus the surviving zero-excess portal mechanism is precisely a fixed-residual
queue walk: a core element is ejected to the front of the singleton queue,
and either the middle mask is refreshed or its last future-departure marker
is exchanged with an upper marker.  This identifies, rather than rules out,
the only local portal architecture not hit by Theorem 3.1.

It does, however, rule out using only fresh one-state pieces.

### Corollary 3.4 — singleton-piece portal chains have one deepest upper flag

Assume \(m-H\ge2\).
Consider a path system in which every piece consists of one fresh canonical
state.  One-update portals can join pieces only inside a common residual
class.  Every state with residual block \(B\) has the same canonical
rank-\((m+H)\) mask
\[
\boxed{[2m]\setminus B.}
\tag{3.12}
\]

If \(J\) distinct residual blocks occur and the pieces support \(M\)
distinct canonical rank-\((m+H)\) masks, then \(J\ge M\), and every
exact-state bridge system satisfies
\[
\boxed{
\mathfrak P_H
\ge
2H+1+2H(J-1)
\ge
2H+1+2H(M-1).
}
\tag{3.13}

In particular, if the canonical deepest-upper defect is \(o(W)\), then
\[
M=N_H-o(W).
\]
For \(H=A\sqrt m+o(\sqrt m)\),
\[
N_H=(e^{-A^2}+o(1))W,
\]
and (3.13) is \(\Omega_A(HW)\), not \(o(W)\).  Hence
\(\mathrm{PTAD}_A\) cannot be realized by singleton pieces joined through
fresh one-update portals.

#### Proof

Theorem 3.3 preserves \(B\) along a one-update portal.  In a fresh state the
rank-\((m+H)\) prefix is the union of the core and all \(2H\) singleton
blocks, hence is exactly \([2m]\setminus B\).  This proves (3.12) and
\(J\ge M\).

Corollary 3.2 says that changing the residual between fresh states requires
a bridge of length at least \(s-1\), contributing at least \(s-2=2H\)
portal excess.  Any linear ordering which visits \(J\) distinct residual
values has at least \(J-1\) residual-changing seams, in addition to the first
initialization.  This proves (3.13).

Finally, the trace-repair sandwich gives
\[
M_H^+\le\Phi_Z(\mathcal H_H).
\]
Thus \(\mathrm{PTAD}_A\) forces deepest-upper defect \(o(W)\).  The standard
central-binomial ratio gives
\(N_H/W=e^{-A^2+o(1)}\), completing the Gaussian statement. \(\square\)

This corollary is about the canonical support ledger.  Incidental masks at
bridge endpoints are not counted in \(\mathcal H_H\) as currently defined.
Allowing those masks as additional designated support would require a
separate augmented ledger.

---

## 4. Exact lower bound for a whole path system

Consider \(C\) canonical path components, in an arbitrary order, and let
\(D\) of them be residual-consuming.  At most one residual-consuming
component can be placed last and thereby avoid an outgoing seam.

### Theorem 4.1 — depleted-component portal ledger

Assume \(m-H\ge2\).
For every ordering and every exact bridge system,
\[
\boxed{
\mathfrak P_H
\ge
2H+1+2H(D-1)_+.
}
\tag{4.1}
\]

In particular,
\[
\boxed{
\mathfrak P_H=o(W)
\quad\Longrightarrow\quad
D=o(W/H).
}
\tag{4.2}
\]

#### Proof

Every depleted component which is not last has outgoing bridge length at
least \(s-1\) by Theorem 3.1, and hence contributes at least
\[
(s-1)-1=s-2=2H
\]
to the sum in the portal excess.  The unavoidable first initialization
contributes \(s-1=2H+1\).  This proves (4.1), and (4.2) follows. \(\square\)

This is independent of the canonical hole family and of the marked set used
for trace repair.  Since \(\mathrm{PTAD}_A\) adds
\(\mathfrak P_H\) and \(\Phi_Z\), no trace compression can cancel the lower
bound (4.1).

There is a complementary support obstruction.  If a component does **not**
consume its residual \(B\), then \(\Theta_i\) always consists of exactly
\(H\) singleton blocks followed by that same \((m-H)\)-block \(B\).
Consequently its deepest upper flag is constant:
\[
P^+_{i,H}=[2m]\setminus B
\qquad\text{at every state }i.
\tag{4.3}
\]

### Theorem 4.2 — portal--support dichotomy

Assume \(m-H\ge2\).
For a canonical path system, let

* \(D\) be the number of residual-consuming components;
* \(K_D\) be their total number of middle states;
* \(J\) be the number of distinct residual blocks among the
  non-residual-consuming components;
* \(\mathcal S_H^+\) be the canonical rank-\((m+H)\) support.

Then
\[
\boxed{
|\mathcal S_H^+|\le K_D+J,
}
\tag{4.4}
\]
and every ordering and exact bridge system satisfies
\[
\boxed{
D-1\le\frac{\mathfrak P_H-(2H+1)}{2H},
\qquad
J-1\le\frac{\mathfrak P_H-(2H+1)}{2H}.
}
\tag{4.5}

Hence, if \(H\to\infty\),
\[
\mathfrak P_H=o(W),
\qquad
M_H^+=o(W),
\tag{4.6}
\]
imply
\[
\boxed{
D=o(W/H),
\qquad
J=o(W/H),
\qquad
K_D\ge N_H-o(W).
}
\tag{4.7}

At Gaussian depth \(H=A\sqrt m+o(\sqrt m)\), this becomes
\[
\boxed{
K_D\ge(e^{-A^2}+o(1))W,
\qquad
\frac{K_D}{D}=\omega(H).
}
\tag{4.8}

Thus a successful exact-state \(\mathrm{PTAD}_A\) construction must place a
positive fraction of all middle owners into only \(o(W/H)\)
residual-consuming components, whose average length is superlinear in
\(H\).  Residual-preserving components may be joined cheaply, but they
cannot carry the deepest upper support.

#### Proof

Equation (4.3) shows that every non-consuming residual value contributes at
most one deepest-upper mask.  The consuming components contribute at most
one such mask per middle state.  This proves (4.4).

The first inequality in (4.5) is Theorem 4.1.  For the second, order the
components and mark the first occurrence of each of the \(J\) distinct full
residual values.  Apart from a possible value at the first component, each
new value has an incoming seam.  If the preceding component is consuming,
Theorem 3.1 makes that seam length at least \(s-1\).  If it is non-consuming
with a different full residual, Corollary 3.2 gives the same conclusion.
Thus each of the \(J-1\) new values charges at least \(s-2=2H\) portal
excess, proving (4.5).

Under (4.6), (4.5) gives \(D,J=o(W/H)\).  The support inequality and
\(N_H-|\mathcal S_H^+|=M_H^+=o(W)\) then give
\(K_D\ge N_H-o(W)\).  Finally
\[
N_H/W=e^{-A^2+o(1)}
\]
at Gaussian depth, and division by \(D=o(W/H)\) proves (4.8). \(\square\)

Because the trace-repair sandwich has \(M_H^+\le\Phi_Z(\mathcal H_H)\),
every \(\mathrm{PTAD}_A\) witness satisfies the hypotheses (4.6).

---

## 5. Cyclic strips necessarily deplete the residual

Take a cyclic strip
\[
T_i=C\cup I_\gamma(i,\ell),
\qquad i\in\mathbb Z_{2\ell},
\tag{5.1}
\]
where \(C,D\) are disjoint cores of size \(m-\ell\), and cut one edge to
obtain a linear path through all \(2\ell\) middle states.  Assume
\[
H<\ell<m.
\tag{5.2}
\]

Write the moving cyclic coordinates as
\(z_0,\ldots,z_{2\ell-1}\), with
\[
T_0=C\cup\{z_0,\ldots,z_{\ell-1}\}.
\]
The initial complement is
\[
T_0^c=D\cup\{z_\ell,\ldots,z_{2\ell-1}\}.
\tag{5.3}
\]
The cyclic-boundary initialization places \(H\) of the moving complement
coordinates in singleton upper blocks.  Therefore its residual is
\[
R_0
=D\cup\{\ell-H\text{ moving coordinates}\},
\qquad |R_0|=m-H.
\tag{5.4}
\]
During the cut path, every one of those \(\ell-H\) moving coordinates is an
arrival.  Each is extracted from \(R_0\), while no coordinate of the fixed
core \(D\) ever arrives.  Hence the terminal residual is exactly
\[
R_{\rm end}=D,
\qquad
|R_{\rm end}|=m-\ell<m-H.
\tag{5.5}
\]

Thus every selected cyclic strip is residual-consuming.

### Corollary 5.1 — shared portals do not amortize strip resets

If \(p\ge1\) cyclic strips occur among the path components, then
\[
\boxed{
\mathfrak P_H\ge2Hp+1.
}
\tag{5.6}
\]

If their middle rows are disjoint and leave \(u_0=o(W)\) middle masks, then
\[
p=\frac{W-u_0}{2\ell}
\]
and consequently
\[
\boxed{
\frac{\mathfrak P_H}{W}
\ge
(1-o(1))\frac{H}{\ell}.
}
\tag{5.7}
\]
Therefore
\[
\boxed{
\mathfrak P_H=o(W)
\quad\Longrightarrow\quad
\ell/H\longrightarrow\infty.
}
\tag{5.8}
\]

The usual independent reset ledger is
\((2H+1)p\).  The exact lower bound (5.6) is \(2Hp+1\).  Thus exact-state
portal sharing can save at most one letter per selected strip and cannot
change the leading component toll.

---

## 6. Odd-cut complementary geodesics also deplete the residual

Assume \(m-H\ge2\).  This restriction is automatic in the Gaussian
applications below.

In the odd-cut architecture, each complementary geodesic has
\[
T_0=A,
\quad
T_i=A-\{a_0,\ldots,a_{i-1}\}
       +\{b_0,\ldots,b_{i-1}\},
\quad
0\le i\le m.
\tag{6.1}
\]
Every coordinate of the initial complement
\(\{b_0,\ldots,b_{m-1}\}\) arrives once.  Only \(H\) of those coordinates
can occupy the initial singleton queue, so all \(m-H\) coordinates of the
initial residual are extracted.  The terminal residual is empty.

The exact odd factor supplies
\[
B=\frac{W}{m+1}
\tag{6.2}
\]
such paths.  Theorem 4.1 gives
\[
\boxed{
\mathfrak P_H\ge2HB+1
=\frac{2HW}{m+1}+1.
}
\tag{6.3}
\]
Independent resets cost \((2H+1)B\).  Their difference from the lower bound
is only \(B-1\).  At Gaussian depth \(H=A\sqrt m\), both are
\(\Theta_A(W/\sqrt m)=o(W)\), so portals are not the obstruction there; but
they also provide no new leading-order saving.

---

## 7. Consequence for the full-strip economical-cover architecture

The preceding obstruction combines with the standard growing-uniformity
matching hypothesis to give a sharp architecture ceiling.

Let \(\mathcal G(m,H,\ell)\) be the full-strip hypergraph on the signed band.
Assume the standard strip regime
\[
H<\ell=o(m).
\]
Its edge size is
\[
R_{\rm hyp}=2\ell(2H+1).
\tag{7.1}
\]
The degree of a middle vertex is
\[
D_0=\frac{m!^2}{2(m-\ell)!^2},
\tag{7.2}
\]
and the maximum band degree is
\[
D_{\max}
=\frac{(m+H)!(m-H)!}{2(m-\ell)!^2}.
\tag{7.3}
\]

### Lemma 7.1 — an unavoidable relative codegree

Let \(\Gamma\) be the maximum codegree of two real band vertices.  Then
\[
\boxed{
\Gamma\ge\frac{2D_0}{m}.
}
\tag{7.4}
\]
If \(H\le A\sqrt m\) for fixed \(A\), then
\[
\boxed{
\frac{\Gamma}{D_{\max}}
\ge
\frac{2e^{-A^2+o(1)}}{m}.
}
\tag{7.5}

For arbitrary \(H<m\), the following weaker but uniform form will be used:
\[
\boxed{
\frac{\Gamma}{D_{\max}}
\ge
\frac2m\exp\left(-\frac{H^2}{m-H}\right).
}
\tag{7.6}

#### Proof

Fix a middle mask \(T\).  Every strip through \(T\) contains exactly two
rank-\((m-1)\) strip masks which are facets of \(T\): the two cyclic
\((\ell-1)\)-intervals obtained by deleting one endpoint of the moving
\(\ell\)-interval.  Therefore
\[
\sum_{\substack{S\subset T\\|S|=m-1}}
\deg(T,S)=2D_0.
\]
There are \(m\) facets, proving (7.4).

Moreover
\[
\frac{D_0}{D_{\max}}
=
\frac{m!^2}{(m+H)!(m-H)!}
=
\prod_{i=1}^H\frac{m-H+i}{m+i}
=
\exp\left(-\frac{H^2}{m}+o(1)\right)
\]
uniformly for \(H\le A\sqrt m\).  This proves (7.5). \(\square\)

For the uniform form, write
\[
\frac{D_{\max}}{D_0}
=\prod_{i=1}^H
\left(1+\frac{H}{m-H+i}\right).
\]
Using \(\log(1+x)\le x\) gives
\[
\log\frac{D_{\max}}{D_0}
\le
H\sum_{i=1}^H\frac1{m-H+i}
\le\frac{H^2}{m-H}.
\]
Together with (7.4), this proves (7.6).

Now suppose the full-strip hypergraph is rounded using the standard
economical-cover/near-perfect-matching hypothesis
\[
e^{2R_{\rm hyp}}\Gamma
=o\left(\frac{D_{\max}}{\log D_{\max}}\right),
\tag{7.7}
\]
possibly after symmetric dummy regularization to degree \(D_{\max}\).
Dummy regularization does not remove the real codegrees in Lemma 7.1.

Equations (7.6) and (7.7) imply
\[
2R_{\rm hyp}
\le
\log m+\frac{H^2}{m-H}
-\log\log D_{\max}-\omega(1).
\tag{7.8}
\]
Since
\[
R_{\rm hyp}=2\ell(2H+1)\ge4\ell H,
\]
and the strip regime has \(H<\ell=o(m)\), inequality (7.8) first implies
\(H^2=O(\log m)\): its left side is at least \(8H^2\), whereas
\(H^2/(m-H)=o(H^2)\).  Substitution back into (7.8) then gives
\[
\boxed{
\ell H\le\left(\frac18+o(1)\right)\log m.
}
\tag{7.9}
\]

If the selected strips have middle leave \(o(W)\) and their exact-state
portal excess is \(o(W)\), Corollary 5.1 also forces
\[
\frac{H}{\ell}\longrightarrow0.
\tag{7.10}
\]
Multiplying (7.9) and (7.10) gives
\[
\boxed{
H^2=o(\log m),
\qquad
H=o(\sqrt{\log m}).
}
\tag{7.11}

### Theorem 7.2 — portal-stable full-strip ceiling

Within the architecture consisting of

1. full signed-depth strip edges;
2. parameters \(H<\ell=o(m)\);
3. a matching with \(o(W)\) middle leave;
4. the standard growing-uniformity hypothesis (7.7); and
5. exact-state portal concatenation of the selected canonical strip paths,

total length \(W+o(W)\) forces
\[
\boxed{H=o(\sqrt{\log m}).}
\tag{7.12}
\]

Thus portal sharing cannot promote the proved
\(o(\sqrt{\log m/\log\log m})\) strip theorem to a polynomial or Gaussian
window.  The remaining \(\sqrt{\log\log m}\) gap inside this architecture is
about the quantitative matching leave, not initialization sharing.

---

## 8. Exact scope of the advance

### Proved here

1. The exact MTF bridge-distance formula (1.5).
2. The exact deletion-overlap portal ledger (1.11)--(1.12).
3. The residual-depletion lower bound (3.1).
4. The necessary common-residual invariant for every bridge of length at
   most \(2H\).
5. The system-level lower bound (4.1).
6. Exact residual depletion for cyclic strips and odd-cut complementary
   geodesics.
7. The necessity \(\ell/H\to\infty\) for a near-spanning strip system with
   \(o(W)\) portal excess.
8. The portal-stable economical-cover ceiling
   \(H=o(\sqrt{\log m})\).

### Not proved here

1. \(\mathrm{PTAD}_A\) or the constant-one upper bound.
2. Any lower bound on the trace-repair term \(\Phi_Z\) beyond the known
   one-rank throughput bound.
3. An obstruction to a mixed construction in which the required positive
   fraction of middle owners already lies in a few super-\(H\)-long depleted
   components.
4. An obstruction to a genuinely global path construction not assembled
   from full strips or odd-cut geodesics.

The precise surviving positive escape is therefore narrower than before:
one must build \(o(W/H)\) super-\(H\)-long residual-consuming components
which together contain \((e^{-A^2}+o(1))W\) middle states and carry almost
all deepest-upper support.  Residual-preserving components can be portalized
cheaply but contribute only one deepest-upper mask per residual value.
Alternatively one must abandon exact canonical-state portals or augment the
canonical support ledger with incidental bridge witnesses.  Cyclic strips
and complementary geodesics satisfy the depletion side of the dichotomy,
but exact portals cannot reduce their leading reset toll.
