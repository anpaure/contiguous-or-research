# Exact decoration hypergraphs for rank-two queues and the deep-row codegree gate

**Date:** 2026-08-07  
**Method:** expose the relevant gauge bits of every suffix cell and count
configuration degrees exactly  
**Status:** exact reduction and quantitative boundary. The binary
\(2^{3p}\) gauge gives the desired decoration lists, but its deepest
proper row has mixed codegree ratio \(1/2\), so list size alone does not
yield an LLL or small-codegree matching theorem. Allowing the private
core injection to vary and switching every bank coordinate reduces that
ratio to \(1/c=o(1)\), but a growing-rank and pointwise-degree gate
remains.

## 1. Starting from an owner-disjoint ring bank

Let \(\mathscr R\) be any collection of pairwise owner-disjoint canonical
rank-two queue rings. Every ring \(R\in\mathscr R\) has:

\[
 |R|=3p,\qquad |K_R|=c,\qquad |B_R|=3p,
\tag{1.1}
\]

where \(K_R\) is its permanent core and \(B_R\) is the union of its
\(p\) phase triples. Assume \(c\ge3p\).

For every cyclic source interval \(Q\) in \(R\) of proper length

\[
 1\le j=|Q|<p,
\tag{1.2}
\]

define

\[
 X_R(Q)=\{x\in B_R:Q\subseteq I_x\}.
\tag{1.3}
\]

Here \(I_x\) is the \(p-1\)-position open carrier interior from the
core--bank gauge theorem.

### Lemma 1.1 (exact relevant-bit set)

For every \(Q\) of length \(j<p\),

\[
 \boxed{|X_R(Q)|=p-j.}
\tag{1.4}
\]

Moreover, the reachable target families belonging to two different
intervals \(Q,Q'\) of the same depth are disjoint.

#### Proof

The interval \(Q\) contains positions from \(j\) consecutive active
phases. It crosses one source position in each active phase, so it is not
contained in any carrier interior from those phases. In each of the other
\(p-j\) phases, it lies strictly between two consecutive updates. That
gap is \(I_x\) for the unique coordinate common to the two endpoint
blocks. This proves (1.4).

Every reachable target still has two bank coordinates in precisely its
active phases and at most one in every inactive phase. Hence its active
phase interval is recoverable from the target. The active two-blocks also
distinguish the three rounds with the same phase interval. Thus distinct
source intervals have disjoint reachable target families. \(\square\)

The complete marked packet of a decoration is the set of all targets in
all \(3p\) cyclic cells at each depth \(1,\ldots,p-1\). Its size is

\[
 h=3p(p-1).
\tag{1.5}
\]

Targets within a packet are distinct: they are simple at fixed depth and
different depths have different ranks.

## 2. The binary-decoration configuration hypergraph

Fix for every ring an injection

\[
 \kappa_R:B_R\longrightarrow K_R.
\tag{2.1}
\]

For \(E\subseteq B_R\), let \(\Phi_R(E)\) be the \(h\)-target packet of
the gauge decoration which switches \(\kappa_R(x)\) with \(x\) on
\(I_x\) for \(x\in E\).

If \(U_R(Q)\) is the canonical value at \(Q\), then

\[
 U_R^E(Q)=
 \left(U_R(Q)\setminus
       \kappa_R(E\cap X_R(Q))\right)
 \cup(E\cap X_R(Q)).
\tag{2.2}
\]

Define \(\mathcal H_{\rm bin}(\mathscr R)\) on the disjoint union of:

1. one private vertex for every ring \(R\);
2. every named target in the ranks \(c+2,c+4,\ldots,c+2p-2\).

For each \(E\subseteq B_R\), insert the \((h+1)\)-edge

\[
 \{R\}\cup\Phi_R(E).
\tag{2.3}
\]

### Proposition 2.1 (exact binary matching reduction)

A matching of size \(H\) in \(\mathcal H_{\rm bin}(\mathscr R)\) is
equivalent to choosing \(H\) already owner-disjoint rings and one gauge
decoration of each, with all marked proper-depth targets pairwise
distinct.

#### Proof

The private ring vertices enforce at most one decoration per ring. The
target vertices enforce all-depth target disjointness. Owner disjointness
was imposed in the definition of \(\mathscr R\). \(\square\)

### Proposition 2.2 (exact binary degrees)

Put

\[
 L_{\rm bin}=2^{3p}.
\tag{2.4}
\]

Then

\[
 d(R)=L_{\rm bin}.
\tag{2.5}
\]

Fix a depth-\(j\) target \(S\). For a ring \(R\), either \(S\) is
unreachable, or it belongs to the reachable family of a unique interval
\(Q\), in which case

\[
 \boxed{
 d(R,S)=2^{3p-(p-j)}=2^{2p+j}.
 }
\tag{2.6}
\]

Equivalently,

\[
 \boxed{
 \frac{d(R,S)}{d(R)}=2^{-(p-j)}.
 }
\tag{2.7}
\]

Each ring has exactly

\[
 3p\,2^{p-j}
\tag{2.8}
\]

reachable depth-\(j\) targets.

If \(S,S'\) correspond in one ring to intervals \(Q,Q'\), their two
constraints specify the gauge bits on \(X_R(Q)\) and \(X_R(Q')\).
When those specifications agree on the overlap, the number of common
decorations is

\[
 2^{3p-|X_R(Q)\cup X_R(Q')|};
\tag{2.9}
\]

otherwise it is zero.

#### Proof

Formula (2.2) shows that a target at \(Q\) specifies exactly the
\(p-j\) bits in \(E\cap X_R(Q)\). All other \(2p+j\) bits are free,
proving (2.6). Lemma 1.1 makes the reachable families for different
intervals disjoint. It also gives (2.8). Two simultaneous target
constraints fix the union of their relevant bit sets exactly when they
agree on the intersection, proving (2.9). \(\square\)

For

\[
 N_j={n\choose c+2j},\qquad M=|\mathscr R|,
\tag{2.10}
\]

the average depth-\(j\) target degree is

\[
 \frac1{N_j}\sum_{|S|=c+2j}d(S)
 =\frac{M\,3p}{N_j}L_{\rm bin}.
\tag{2.11}
\]

Thus the average target degree is a constant multiple of the ring degree
when \(M=\Theta(W/p)\). The difficulty is not average scalar capacity.

### Corollary 2.3 (the exact deep-row obstruction)

At the deepest proper row \(j=p-1\),

\[
 \boxed{d(R,S)=\frac12d(R)}
\tag{2.12}
\]

for every reachable ring--target pair.

Hence the \(2^{3p}\) list size does not give exponentially small local
events at that row. A specified reachable deepest target occurs under a
uniform random binary decoration with probability \(1/2\), and two rings
with the same two-option local target family can collide with constant
probability.

In particular, \(\mathcal H_{\rm bin}\) does not satisfy a
small-pair-codegree hypothesis: its mixed ring--target codegree is already
one half of the ring degree. A black-box nibble, Pippenger--Spencer
theorem, or symmetric LLL cannot be inferred from the decoration-list
cardinality.

## 3. Removing the atom by varying the core injection

There is a stronger decoration family. For every injection

\[
 \kappa:B_R\hookrightarrow K_R,
\tag{3.1}
\]

switch **all** \(3p\) bank coordinates on their carrier interiors. Let
\(\Psi_R(\kappa)\) be its complete marked packet. The number of choices is

\[
 L_{\rm inj}=(c)_{3p}.
\tag{3.2}
\]

For an interval \(Q\) of depth \(j\), put \(r=p-j\). Its target is

\[
 U_R^\kappa(Q)=
 \left(U_R(Q)\setminus\kappa(X_R(Q))\right)
 \cup X_R(Q).
\tag{3.3}
\]

It records the \(r\)-set \(\kappa(X_R(Q))\subseteq K_R\), but not the
bijection from \(X_R(Q)\) to that set. Consequently:

### Proposition 3.1 (exact injection degrees)

For a fixed interval \(Q\) at depth \(j\):

1. there are exactly
   \[
   {c\choose r}
   \tag{3.4}
   \]
   reachable target values;
2. every one occurs in exactly
   \[
   r!\,(c-r)_{3p-r}
   \tag{3.5}
   \]
   injection decorations;
3. for every reachable ring--target pair,
   \[
   \boxed{
   \frac{d(R,S)}{d(R)}
   =\frac1{{c\choose p-j}}.
   }
   \tag{3.6}
   \]

If targets at intervals \(Q,Q'\) prescribe image sets
\(A,A'\subseteq K_R\), put

\[
 r=|X_R(Q)|,\quad r'=|X_R(Q')|,\quad
 a=|X_R(Q)\cap X_R(Q')|.
\tag{3.7}
\]

Their constraints are compatible only if

\[
 |A\cap A'|=a.
\tag{3.8}
\]

When compatible, the exact number of common injections is

\[
 a!\,(r-a)!\,(r'-a)!\,
 (c-r-r'+a)_{\,3p-r-r'+a}.
\tag{3.9}
\]

#### Proof

The target determines exactly the image set of the \(r\)-element domain
\(X_R(Q)\). For a prescribed image set, there are \(r!\) bijections on
that domain and \((c-r)_{3p-r}\) injections on the remaining bank
coordinates. Dividing by \((c)_{3p}\) gives

\[
 \frac{r!(c-r)_{3p-r}}{(c)_{3p}}
 =\frac1{{c\choose r}}.
\]

For two constraints, injectivity gives

\[
 \kappa(X_R(Q))\cap\kappa(X_R(Q'))
 =\kappa(X_R(Q)\cap X_R(Q')),
\]

so (3.8) is necessary. If it holds, independently biject the common
domain to \(A\cap A'\), the two domain differences to the two image
differences, and inject the remaining coordinates into the unused core.
This gives (3.9). \(\square\)

Define \(\mathcal H_{\rm inj}(\mathscr R)\) analogously to (2.3), using
the packets \(\Psi_R(\kappa)\). It has the same exact matching
interpretation. At depth \(j\), one ring has

\[
 3p{c\choose p-j}
\tag{3.10}
\]

reachable targets, while its average target degree is again

\[
 \frac{M\,3p}{N_j}L_{\rm inj}.
\tag{3.11}
\]

At the deepest proper row,

\[
 \boxed{
 \max_{S:d(R,S)>0}\frac{d(R,S)}{d(R)}=\frac1c=o(1).
 }
\tag{3.12}
\]

Thus varying the private core injection removes the binary construction's
probability-\(1/2\) atom.

## 4. What is and is not closed

The injection decoration is a genuine quantitative improvement, but it
does not by itself prove the required packet matching.

First, the edge rank is

\[
 h+1=3p(p-1)+1=\Theta(m).
\tag{4.1}
\]

Although the largest local mixed-codegree ratio is now \(1/c=o(1)\), the
natural rank-weighted quantity is

\[
 \frac{h}{c}
 =\frac{3p(p-1)}c
 \longrightarrow\frac{3\pi}{4},
\tag{4.2}
\]

not zero at triangular depth. Fixed-rank small-codegree theorems do not
apply diagonally to this growing-rank family.

Second, (2.11) and (3.11) are average identities. They give no pointwise
bound on the number of owner rings capable of realizing one named target.
A target concentrated in many ring lists can still have degree much
larger than the ring degree.

Therefore the gauge construction yields the exact remaining statement:

> **All-depth injection-decoration matching lemma.** From the
> owner-disjoint queue bank, select
> \[
> H=(\theta+o(1))\frac{W}{3p}
> \]
> rings and one injection decoration per selected ring so that their
> \(hH\) marked targets are pairwise distinct.

This lemma would close owner--lower-target recoupling without changing a
single owner. It is not presently proved.

The binary gauge alone is quantitatively insufficient for a generic
LLL/matching argument because of (2.12). The all-switch injection family
is the proof-relevant refinement: it converts the exact obstruction from
a constant local atom into a growing-rank, pointwise-spread problem.
