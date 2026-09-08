# EP via a tag-\(H\) rotor backbone and promotion fibres

Date: 2026-07-25

Pure mathematics only. No search, solver, computation, or generic
probabilistic rounding theorem is used.

## 0. Outcome

Let

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\). The decorated-SCD extension gate
\(\mathrm{EP}_A\) asks for one clipped Boolean SCD, one radius-\(H\)
collar extension of every chain state, and a bridge-one path cover of the
\(W\) useful states with

\[
p=o_A(W/H).
\]

This note does not prove \(\mathrm{EP}_A\). It derives its exact induced
middle-owner dynamics, proves an integral matching theorem for the
promotion fibres, and isolates one fully explicit sufficient construction
as two concrete lemmas.

The principal conclusions are:

1. Every nontrivial bridge-one arc induces the Johnson transition
   \[
   \boxed{Y=X-z_H+a,}
   \]
   where \(a\) is either a residual-tail coordinate (rotor shift) or one of
   the upper collar singletons (promotion).
2. Promotion preserves the full collar top
   \[
   U=L\cup\{z_1,\ldots,z_{2H}\}.
   \]
   Hence it is a fibrewise operation over \(U\).
3. For every clipped SCD, all chains of tag \(d<H\) can be assigned
   integrally to collar tops \(U\in\binom{[2m]}{m+H}\) containing their
   actual upper endpoints, with at most
   \[
   \sum_{d<H}\left\lceil\frac{N_d}{N_H}\right\rceil
   =O_A(H)
   \]
   shorter chains assigned to any one \(U\). This is a direct capacitated
   Hall matching, not a fractional assignment.
4. Every \(U\) is the actual top of exactly one tag-\(H\) chain. Those
   tag-\(H\) chains have no collar-extension freedom.
5. Two distinct tag-\(H\) chains in one SCD cannot be joined by promotion,
   because promotion preserves \(U\) and two SCD chains cannot own the same
   rank-\((m+H)\) mask.
6. If an EP path cover has \(p\) components, the number of tag-\(H\) to
   tag-\(H\) arcs is at least
   \[
   \boxed{(2N_H-W-p)_+.}
   \]
   Every such arc is necessarily a genuine rotor shift. In particular, if
   \(A<\sqrt{\log2}\), then EP needs
   \[
   \bigl(2e^{-A^2}-1-o(1)\bigr)W
   \]
   rotor arcs between no-extension states. Promotion alone cannot prove
   EP, even though it greatly enlarges the bridge graph.
7. The apparent \(H\) inverse-promotion slots at one Johnson predecessor
   owner induce only \(d+1\) distinct tag-\(d\) chain templates. The last
   template has \(H-d\) collar-order realizations; each of the other \(d\)
   templates has one.
8. A mask-disjoint packing by recursive \(2\ell\)-cycles which misses only
   \(o_A(W/H)\) tag-\(H\) states would prove the required top-tag backbone.
   Such a packing must mix coordinate matchings: one fixed pairing has a
   positive Gaussian pair-type deficit at \(H=A\sqrt m\).
9. In the bounded-fibre programme, once only \(o_A(W)\) shorter chains are
   sent to boundary paths, the remaining threading needs
   \(\Omega_A(W/H)\) detoured backbone edges. Thus the promotion problem
   occurs at the critical interface density, not on a negligible family.

A concrete sufficient programme is therefore:

* build one SCD whose tag-\(H\) states have a long rotor-shift path cover;
* jointly assign every shorter chain to a collar-top fibre and split each
  fibre into an incoming and an outgoing ordered list; and
* replace selected backbone edges \(U\to V\) by two-sided detours: promote
  through the outgoing list in \(U\), make one rotor move, then promote
  through the incoming list in \(V\).

The detour is local to an oriented top edge, but the fibre assignment and
incoming/outgoing splits are global correlated choices. A one-sided detour
is impossible by Proposition 6.1. The precise formulations appear in
Section 7 and together imply \(\mathrm{EP}_A\).

## 1. Exact coordinates of a collar extension

Write a tagged radius-\(d\) SCD state as

\[
\omega_d=(A;c_1,\ldots,c_{2d};B),
\qquad |A|=|B|=m-d.
\tag{1.1}
\]

Its saturated chain is

\[
A\subset A+c_1\subset\cdots\subset A+c_1+\cdots+c_{2d},
\tag{1.2}
\]

and its middle owner is

\[
X=A\cup\{c_1,\ldots,c_d\}.
\tag{1.3}
\]

A radius-\(H\) extension chooses ordered distinct elements

\[
a_1,\ldots,a_{H-d}\in A,
\qquad
b_1,\ldots,b_{H-d}\in B.
\tag{1.4}
\]

The full useful state is

\[
\omega=(L;z_1,\ldots,z_{2H};R),
\tag{1.5}
\]

where

\[
L=A\setminus\{a_1,\ldots,a_{H-d}\},
\qquad
R=B\setminus\{b_1,\ldots,b_{H-d}\},
\tag{1.6}
\]

and

\[
(z_1,\ldots,z_{2H})
=
(a_1,\ldots,a_{H-d},
 c_1,\ldots,c_{2d},
 b_1,\ldots,b_{H-d}).
\tag{1.7}
\]

Thus

\[
X=L\cup\{z_1,\ldots,z_H\}.
\tag{1.8}
\]

The full collar bottom and top are

\[
D=L\in\binom{[2m]}{m-H},
\qquad
U=L\cup\{z_1,\ldots,z_{2H}\}
  =[2m]\setminus R\in\binom{[2m]}{m+H}.
\tag{1.9}
\]

The actual tag-\(d\) lower and upper endpoints are recovered by

\[
A=L\cup\{z_1,\ldots,z_{H-d}\},
\tag{1.10}
\]

\[
[2m]\setminus B
=L\cup\{z_1,\ldots,z_{H+d}\}.
\tag{1.11}
\]

For \(d=H\), the lists in (1.4) are empty. Hence a tag-\(H\) chain has
exactly one radius-\(H\) useful state: its SCD chain word itself.

## 2. The induced middle-owner transition

Let

\[
\omega=(L;z_1,\ldots,z_{2H};R)
\]

and let \(\omega'\) be a bridge-one successor. The complete classification
in ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md has the following
middle-owner consequence.

### Proposition 2.1 (owner projection of every bridge-one arc)

Let \(X=L\cup\{z_1,\ldots,z_H\}\).

1. In a rotor shift, for \(x\in L\) and \(y\in R\),
   \[
   L'=L-x+y,\qquad
   (z'_1,\ldots,z'_{2H})=(x,z_1,\ldots,z_{2H-1}),
   \tag{2.1}
   \]
   and
   \[
   \boxed{Y=X-z_H+y.}
   \tag{2.2}
   \]
2. In a promotion, for \(x\in L\) and \(1\le j\le2H\),
   \[
   L'=L-x+z_j,
   \tag{2.3}
   \]
   \[
   (z'_1,\ldots,z'_{2H})
   =(x,z_1,\ldots,z_{j-1},z_{j+1},\ldots,z_{2H}).
   \tag{2.4}
   \]
   If \(j\le H\), then \(Y=X\). If \(j>H\), then
   \[
   \boxed{Y=X-z_H+z_j.}
   \tag{2.5}
   \]

Thus every bridge-one arc between distinct owners is a Johnson edge and
deletes the single coordinate \(z_H\).

#### Proof

For the rotor case, the first \(H\) target singletons are
\(x,z_1,\ldots,z_{H-1}\). Therefore

\[
Y=(L-x+y)\cup\{x,z_1,\ldots,z_{H-1}\}
  =X-z_H+y.
\]

For promotion, the first \(H\) target singletons are \(x\) followed by the
first \(H-1\) entries of the old list with \(z_j\) deleted. If \(j\le H\),
the promoted element \(z_j\) in \(L'\) exactly replaces its deletion from
the first half, so the middle owner remains \(X\). If \(j>H\), the first
half loses \(z_H\), while \(L'\) gains \(z_j\), proving (2.5).
\(\square\)

### Proposition 2.2 (collar-top dynamics)

Let \(U=L\cup\{z_1,\ldots,z_{2H}\}\).

1. Promotion preserves the collar top:
   \[
   \boxed{U'=U.}
   \tag{2.6}
   \]
2. A rotor shift changes it by the Johnson move
   \[
   \boxed{U'=U-z_{2H}+y.}
   \tag{2.7}
   \]

#### Proof

In promotion, \(z_j\) moves from the singleton list into \(L\), while \(x\)
moves from \(L\) into the singleton list. Their union is unchanged. In a
rotor shift, \(x\) is likewise transferred internally, \(y\) enters from
\(R\), and the dropped last singleton \(z_{2H}\) enters the new residual.
This proves (2.6)--(2.7). \(\square\)

The distinction is exact: promotion moves between chain states inside one
top fibre \(U\), while rotor shifts move between adjacent top fibres.

## 3. First-band compatibility forced by an SCD

Suppose the source chain has positive tag. In (1.7), position \(H\) is
\(c_d\), so its actual lower rank-\((m-1)\) member is

\[
L_1(X)=X-z_H.
\tag{3.1}
\]

If the target chain has positive tag, its actual upper rank-\((m+1)\)
member is

\[
U_1(Y)=Y+z'_{H+1}.
\tag{3.2}
\]

For every distinct-owner bridge-one arc, (2.1)--(2.5) give

\[
z'_{H+1}=z_H.
\tag{3.3}
\]

Hence

\[
\boxed{
L_1(X)=X\cap Y,\qquad U_1(Y)=X\cup Y
}
\tag{3.4}
\]

whenever the relevant tag is positive. Radius-zero chains have no forced
first lower or upper flag and must be audited separately; their number is

\[
\gamma_0=W-N_1=\frac{W}{m+1}=o(W/H).
\tag{3.5}
\]

They may therefore be isolated without affecting EP's component scale.

## 4. Exact capacitated assignment to promotion fibres

For a chain \(C\) of tag \(d\), let

\[
T(C)\in\binom{[2m]}{m+d}
\]

be its actual upper endpoint. A collar extension with top \(U\) exists
exactly when

\[
T(C)\subseteq U,\qquad |U|=m+H.
\tag{4.1}
\]

Indeed, the \(H-d\) elements of \(U\setminus T(C)\) are precisely the
chosen upper extension coordinates \(b_1,\ldots,b_{H-d}\).

Let \(\mathcal C_d\) be the tag-\(d\) chains of a clipped SCD. Their number
is

\[
|\mathcal C_d|=\gamma_d
\quad(d<H),\qquad
|\mathcal C_H|=N_H.
\tag{4.2}
\]

### Theorem 4.1 (integral top-fibre assignment)

For every \(d<H\), the chains in \(\mathcal C_d\) can be assigned to tops
\(U\in\binom{[2m]}{m+H}\) satisfying \(T(C)\subseteq U\), so that no top
receives more than

\[
\boxed{k_d=\left\lceil\frac{N_d}{N_H}\right\rceil}
\tag{4.3}
\]

tag-\(d\) chains.

Performing these assignments independently for all \(d<H\), every top
receives at most

\[
\boxed{
K_A(m):=\sum_{d=0}^{H-1}k_d=O_A(H)
}
\tag{4.4}
\]

shorter chains.

#### Proof

Consider the regular inclusion graph between all rank-\((m+d)\) sets and
all rank-\((m+H)\) sets. Its left and right degrees are

\[
\alpha_d=\binom{m-d}{H-d},
\qquad
\beta_d=\binom{m+H}{H-d}.
\tag{4.5}
\]

Double counting its edges gives

\[
N_d\alpha_d=N_H\beta_d.
\tag{4.6}
\]

Restrict the left side to the actual top endpoints
\(\{T(C):C\in\mathcal C_d\}\). For any subfamily \(\mathcal S\), all
\(\alpha_d|\mathcal S|\) incident edges land in its neighbourhood, where
each right vertex receives at most \(\beta_d\) of them. Hence

\[
|N(\mathcal S)|
\ge\frac{\alpha_d}{\beta_d}|\mathcal S|
=\frac{N_H}{N_d}|\mathcal S|.
\tag{4.7}
\]

Replace every right vertex by \(k_d\) identical capacity copies. Since
\(k_dN_H/N_d\ge1\), equation (4.7) is Hall's condition for a matching
saturating all chains in \(\mathcal C_d\). This proves (4.3).

Uniformly for \(d\le H\),

\[
\frac{N_d}{N_H}
\le\frac{W}{N_H}
=e^{A^2+o_A(1)}.
\tag{4.8}
\]

Thus every \(k_d=O_A(1)\), and summing \(H\) values proves (4.4).
\(\square\)

The theorem assigns the upper extension **sets** exactly. Their orders and
the lower extension coordinates remain free for the promotion-threading
step.

Every rank-\((m+H)\) mask \(U\) is the upper member of exactly one tag-\(H\)
chain, because the \(N_H\) tag-\(H\) chains partition that rank. Denote this
forced no-extension state by \(\omega_U\). It is the natural anchor of the
promotion fibre over \(U\).

## 5. Tag-\(H\) chains: the no-extension audit

For a tag-\(H\) chain,

\[
\omega_U=(L;c_1,\ldots,c_{2H};R),
\qquad U=L\cup\{c_1,\ldots,c_{2H}\},
\tag{5.1}
\]

and there is no collar choice.

### Proposition 5.1 (promotion cannot join two tag-\(H\) chains)

If two tag-\(H\) states in one SCD are joined by a bridge-one arc and have
distinct middle owners, then the arc is a rotor shift.

#### Proof

Identity and promotions with \(j\le H\) preserve the middle owner. A
promotion with \(j>H\) changes the owner but preserves the collar top \(U\)
by (2.6). For a tag-\(H\) state, \(U\) is its actual rank-\((m+H)\) SCD
member. Two distinct SCD chains cannot both contain that mask. Therefore no
promotion joins two distinct tag-\(H\) states. The bridge classification
leaves only a rotor shift. \(\square\)

### Proposition 5.2 (forced density of tag-\(H\) rotor arcs)

Let a directed path cover of all \(W\) decorated states have \(p\)
components. Let \(a_{HH}\) be the number of its arcs whose source and target
both have tag \(H\). Then

\[
\boxed{
a_{HH}\ge(2N_H-W-p)_+.
}
\tag{5.2}
\]

Every one of these arcs is a rotor shift.

#### Proof

A path cover has \(W-p\) arcs. There are \(W-N_H\) lower-tag vertices.
Since every vertex has indegree and outdegree at most one, at most
\(2(W-N_H)\) cover arcs are incident with a lower-tag vertex. Therefore

\[
a_{HH}\ge W-p-2(W-N_H)=2N_H-W-p.
\]

Take the positive part and apply Proposition 5.1. \(\square\)

Since

\[
\frac{N_H}{W}=e^{-A^2+o_A(1)},
\tag{5.3}
\]

EP with \(p=o(W/H)\) implies, whenever \(A<\sqrt{\log2}\),

\[
\boxed{
a_{HH}\ge
\bigl(2e^{-A^2}-1-o_A(1)\bigr)W.
}
\tag{5.4}
\]

Thus the extension freedom of shorter chains cannot hide the hard
full-depth core. A proof of EP for all fixed \(A\) must in particular solve
the tag-\(H\) rotor problem for every sufficiently small positive \(A\).

### Proposition 5.3 (exact promotion-predecessor star of an anchor)

Fix the tag-\(H\) anchor

\[
\omega_U=(L;w_1,\ldots,w_{2H};R).
\tag{5.5}
\]

Every promotion predecessor which has a distinct middle owner is uniquely
specified by a pair

\[
s\in L,\qquad H<j\le2H,
\tag{5.6}
\]

and has full state

\[
\widetilde\omega_{s,j}
=
\left(
L-s+w_1;\
w_2,\ldots,w_j,s,w_{j+1},\ldots,w_{2H};\
R
\right).
\tag{5.7}
\]

All \(H\) slot choices for a fixed \(s\) have the same middle owner

\[
\boxed{
X(\widetilde\omega_{s,j})=X(\omega_U)-s+w_{H+1}.
}
\tag{5.8}
\]

Conversely, every distinct-owner promotion predecessor of \(\omega_U\) is
one of the states (5.7).

#### Proof

In the promotion formula, the first target singleton is the element
\(x\) removed from the source lower block. Hence \(x=w_1\). The promoted
source singleton \(z_j\) must be the element \(s\) inserted into the target
lower block, so \(s\in L\), and the source lower block is
\(L-s+w_1\).

Deleting source position \(j\) and prepending \(w_1\) must recover the
target list \(w_1,\ldots,w_{2H}\). This forces the source list in (5.7).
The owner changes exactly when \(j>H\). In that case the first \(H\) source
singletons are \(w_2,\ldots,w_{H+1}\), independently of \(j\). Therefore

\[
\begin{aligned}
X(\widetilde\omega_{s,j})
&=(L-s+w_1)\cup\{w_2,\ldots,w_{H+1}\}\\
&=X(\omega_U)-s+w_{H+1},
\end{aligned}
\]

which proves (5.8) and exhausts all inverse promotion choices.
\(\square\)

The formula exposes two distinct layers of the local matching problem.
Top containment \(T(C)\subseteq U\) is necessary to extend a shorter chain
into the fibre \(U\), and Theorem 4.1 solves that capacity problem. To place
the chain immediately before the anchor, its middle owner must additionally
lie in the directed Johnson star (5.8), and an insertion slot in (5.7) must
induce its forced tag-\(d\) chain state. Neither condition follows from top
containment alone. The exact number of distinct induced tag states is
smaller than the apparent \(H\) slot count.

### Proposition 5.4 (the exact tag-\(d\) port list)

Fix \(s\in L\), let \(0\le d<H\), and truncate the \(H\) states
\(\widetilde\omega_{s,j}\), \(H<j\le2H\), to tag \(d\). They induce
exactly \(d+1\) distinct tagged chain states, all with owner

\[
X_s=X(\omega_U)-s+w_{H+1}.
\tag{5.9}
\]

For the \(d\) slots \(H<j\le H+d\), the central word is

\[
(w_{H-d+2},\ldots,w_j,s,w_{j+1},\ldots,w_{H+d}),
\tag{5.10}
\]

one different word for each \(j\). All \(H-d\) slots \(j>H+d\) induce
the same tagged chain state, whose central word is

\[
(w_{H-d+2},\ldots,w_{H+d+1}).
\tag{5.11}
\]

Consequently, if the unique SCD chain owned by \(X_s\) has tag \(d<H\), it
has a radius-\(H\) extension that promotes directly into \(\omega_U\) if
and only if its tagged state is one of the \(d+1\) templates
(5.10)--(5.11). If it is the last template, there are exactly \(H-d\)
valid incoming collar orders; otherwise there is exactly one.

#### Proof

Let \(q^{(j)}\) be the singleton list in (5.7). Since \(j>H\), its first
\(H-d\) entries are always

\[
w_2,\ldots,w_{H-d+1}.
\tag{5.12}
\]

Thus every truncation has the same lower endpoint

\[
(L-s+w_1)\cup\{w_2,\ldots,w_{H-d+1}\}.
\tag{5.13}
\]

If \(j\le H+d\), the inserted letter \(s\) lies in the central
\(2d\)-letter interval of \(q^{(j)}\), giving (5.10); its upper residual
set is

\[
R\cup\{w_{H+d+1},\ldots,w_{2H}\}.
\tag{5.14}
\]

These \(d\) ordered central words are distinct. If \(j>H+d\), the whole
central interval occurs before the insertion and equals (5.11). The upper
residual set is then

\[
R\cup\{s,w_{H+d+2},\ldots,w_{2H}\},
\tag{5.15}
\]

independently of the position of \(s\) inside that residual block. Hence
all \(H-d\) such slots truncate to one and the same tagged state. The
owner identity is (5.8). An SCD has exactly one tagged chain at each
middle owner, so the final criterion and multiplicities follow. \(\square\)

Call a pair \((U,s)\) an **incoming promotion port** when the SCD chain at
the owner (5.9) is one of the templates in Proposition 5.4. The direct
last step into a tag-\(H\) anchor is therefore not a generic inclusion
matching: it is the exact deterministic test of at most \(d+1\) chain
states at each of its \(m-H\) directed Johnson ports.

Define the **port graph** \(\mathcal P(\mathcal D)\) with the shorter SCD
chains on the left and the tag-\(H\) anchors on the right, joining \(C\) to
\(U\) exactly when \(C\) occupies an incoming promotion port of
\(\omega_U\).

### Corollary 5.5 (exact terminal-port Hall gate)

For a specified anchor family \(\mathcal A\), there are pairwise distinct
shorter chains \(C_U\), \(U\in\mathcal A\), and radius-\(H\) extensions

\[
\widetilde\omega(C_U)\longrightarrow\omega_U
\tag{5.16}
\]

by promotion if and only if

\[
|N_{\mathcal P}(\mathcal S)|\ge|\mathcal S|
\qquad\text{for every }\mathcal S\subseteq\mathcal A.
\tag{5.17}
\]

#### Proof

Proposition 5.4 says that the edges of \(\mathcal P(\mathcal D)\) are
exactly the shorter-chain/anchor pairs admitting (5.16), including the
complete collar-order list. Pairwise distinct choices are therefore
exactly a matching saturating \(\mathcal A\), and Hall's theorem gives
(5.17). \(\square\)

This is strictly weaker than Lemma 7.2: it chooses only the terminal chain
at each requested anchor and does not thread the remaining fibre chains or
make one collar support both an incoming and an outgoing arc. It is the
smallest exact matching obstruction exposed by promotion.

There is an asymmetric outgoing version which will be needed for a valid
rotor-edge detour.

### Proposition 5.6 (exact promotion-successor ports)

Fix \(0\le d<H\) and the anchor (5.5). For a promotion with \(x\in L\)
and \(H<j\le2H\), its successor is

\[
\left(
L-x+w_j;\
x,w_1,\ldots,w_{j-1},w_{j+1},\ldots,w_{2H};\
R
\right).
\tag{5.18}
\]

For fixed \(j\), all \(m-H\) choices of \(x\) truncate to the same
tag-\(d\) chain state, with owner

\[
Y_j=X(\omega_U)-w_H+w_j.
\tag{5.19}
\]

Its lower endpoint is

\[
L\cup\{w_1,\ldots,w_{H-d-1},w_j\}.
\tag{5.20}
\]

If \(j\le H+d\), its central word and upper residual are

\[
(w_{H-d},\ldots,w_{j-1},w_{j+1},\ldots,w_{H+d}),
\tag{5.21}
\]

\[
R\cup\{w_{H+d+1},\ldots,w_{2H}\}.
\tag{5.22}
\]

If \(j>H+d\), they are

\[
(w_{H-d},\ldots,w_{H+d-1}),
\tag{5.23}
\]

\[
R\cup
\bigl(\{w_{H+d},\ldots,w_{2H}\}\setminus\{w_j\}\bigr).
\tag{5.24}
\]

Thus the SCD chain at owner \(Y_j\), if it has tag \(d<H\), admits a
promotion directly from \(\omega_U\) exactly when it equals the displayed
template; in that event it has exactly \(m-H\) valid outgoing collar
orders.

#### Proof

Formula (5.18) is Proposition 2.1. Because \(j>H\), the first \(H-d\)
successor singletons are

\[
x,w_1,\ldots,w_{H-d-1}.
\]

Together with the successor lower block they give (5.20), independently of
\(x\). Reading the next \(2d\) positions and the final \(H-d\) positions
gives (5.21)--(5.24), according as the deleted letter \(w_j\) occurs inside
or after the central interval. Equation (5.19) is (2.5). Distinct \(x\)'s
give distinct full states, and Proposition 2.1 exhausts all promotion
successors, proving the multiplicity. \(\square\)

Call a matching chain in Proposition 5.6 an **outgoing promotion port** of
\(U\). Incoming ports have only the \(1\) or \(H-d\) collar multiplicities
of Proposition 5.4, whereas every outgoing port has multiplicity \(m-H\).

## 6. The exact tag-\(H\) shift graph

Let two tag-\(H\) states be

\[
\omega=(L;c_1,\ldots,c_{2H};R),
\qquad
\omega'=(L';c'_1,\ldots,c'_{2H};R').
\]

By Proposition 5.1 they are adjacent only if, for some \(x\in L\) and
\(y\in R\),

\[
\boxed{
L'=L-x+y,
}
\tag{6.1}
\]

\[
\boxed{
(c'_1,\ldots,c'_{2H})
=(x,c_1,\ldots,c_{2H-1}),
}
\tag{6.2}
\]

\[
\boxed{
R'=R-y+c_{2H}.
}
\tag{6.3}
\]

The induced middle and top transitions are

\[
X'=X-c_H+y,
\qquad
U'=U-c_{2H}+y.
\tag{6.4}
\]

Call the resulting directed graph on the tag-\(H\) chains of an SCD its
**full-depth shift graph** \(\mathcal G_H(\mathcal D)\).

The overlap in (6.2) is rigid: the target's entire \(2H\)-letter chain word
is obtained by shifting the source word one place and prepending one element
of its lower endpoint. Unlike lower tags, neither endpoint can alter this
word by choosing a collar extension.

### Proposition 6.1 (no one-sided substitution of a top-tag rotor edge)

Let \(\omega_U\to\omega_V\) be a tag-\(H\) rotor arc. Consider a simple
bridge-one path from \(\omega_U\) to \(\omega_V\) whose collar-top sequence
stays at \(U\), changes once by a rotor step to \(V\), and then stays at
\(V\); all other steps are promotions. If the path has an internal vertex,
then it has at least one internal vertex of top \(U\) before the rotor and
at least one internal vertex of top \(V\) after the rotor.

#### Proof

Suppose first that the rotor leaves \(\omega_U\) itself. Its entering
coordinate, hence the target top \(V\), fixes the rotor-successor owner by
(2.2). Because \(\omega_U\to\omega_V\) is a rotor arc, that owner is
\(X(\omega_V)\). A selected decorated state with this owner must lie over
the unique SCD chain owned by \(X(\omega_V)\), namely the tag-\(H\) chain
of \(\omega_V\). This chain has no extension freedom, so the rotor target
is \(\omega_V\) itself. A simple path cannot then leave and later end at
\(\omega_V\). Thus every nontrivial detour has an internal top-\(U\)
vertex before the rotor.

Dually, suppose the rotor lands directly at \(\omega_V\). For a fixed
target state and a fixed source top \(U\), the inverse rotor formulas
uniquely recover the source: the dropped last singleton is the unique
element of \(U\setminus V\), the entering residual element is the unique
element of \(V\setminus U\), and the remaining word is obtained by deleting
the first target singleton and appending the dropped element. Since
\(\omega_U\) is one such predecessor, it is the unique one. A simple path
cannot visit \(\omega_U\), leave by promotions, and return to it as the
rotor source. Hence a nontrivial detour also has an internal top-\(V\)
vertex after the rotor. \(\square\)

This is the exact interface toll missed by a target-fibre-only threading
argument. A transparent one-rotor replacement of a tag-\(H\) edge consumes
at least two shorter chains, one assigned to each endpoint fibre. It does
not prove a universal two-chain toll for arbitrary bridge paths, which may
make several rotor top changes.

### Necessary tag-\(H\) backbone

Every EP path cover induces in \(\mathcal G_H(\mathcal D)\) a directed
linear forest with at least

\[
(2N_H-W-p)_+
\tag{6.5}
\]

edges. For \(A<\sqrt{\log2}\), this is a positive linear fraction of \(W\).
The already known first-band Johnson forest supplies only the projection
\(X\to X-c_H+y\); it does not supply the word overlap (6.2) or the residual
update (6.3).

## 7. A recursive/matching construction reduced to two lemmas

Theorem 4.1 gives an exact assignment

\[
\phi:\bigcup_{d<H}\mathcal C_d
\longrightarrow\binom{[2m]}{m+H},
\qquad
T(C)\subseteq\phi(C),
\tag{7.1}
\]

with fibre size at most \(K_A(m)=O_A(H)\). Write

\[
\mathcal F_U=\{C:\phi(C)=U\}.
\tag{7.2}
\]

Every \(C\in\mathcal F_U\) has upper collar extensions with top \(U\), and
\(\omega_U\) is the unique tag-\(H\) anchor in that fibre.

The following two statements are sufficient for EP.

### Lemma target 7.1 (tag-\(H\) rotor backbone)

There is a clipped SCD \(\mathcal D\) for which
\(\mathcal G_H(\mathcal D)\) has a directed path cover
\(\mathcal P_H\) with

\[
p_H=o_A(W/H).
\tag{7.3}
\]

This is a shift-word refinement of the first-band two-sided-rainbow forest,
not merely a Johnson-edge factor.

There is a concrete recursive sufficient condition for this lemma. Let
\(\ell\le m\) be a power of two with \(H\le\ell/2\). Proposition 1.1 of
ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md supplies a genuine
\(2\ell\)-cycle of pairwise mask-disjoint radius-\(H\) chains from every
recursive orientation-cube cycle.

### Proposition 7.1a (divisibility-safe recursive packet reduction)

Suppose one clipped SCD contains pairwise mask-disjoint recursive
radius-\(H\) packets, each of length \(2\ell\), covering all but \(r\) of
its tag-\(H\) chains. Then its full-depth shift graph has a path cover with

\[
p_H\le \frac{N_H-r}{2\ell}+r.
\tag{7.3a}
\]

In particular, for the largest power of two \(\ell\le m\), if

\[
r=o_A(W/H),
\tag{7.3b}
\]

then Lemma 7.1 holds.

#### Proof

Cut one edge in every packet cycle and make each of the \(r\) uncovered
tag-\(H\) states a singleton path. The packet count is exactly
\((N_H-r)/(2\ell)\), an integer because it counts the selected packets;
no divisibility of \(N_H\) is assumed. Since \(2\ell>m\),

\[
\frac{N_H-r}{2\ell}=O_A(W/m)=o_A(W/H),
\]

and (7.3b) proves the assertion. \(\square\)

The selection in Proposition 7.1a cannot stay inside one fixed coordinate
pairing. For a rank-\((m-H)\) lower target with \(f\) full pairs, the fixed
frame has target demand and source capacity

\[
T_{f,H}=
\frac{m!}{f!(f+H)!(m-2f-H)!}\,2^{m-2f-H},
\qquad
V_f=
\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.
\tag{7.3c}
\]

The fixed-pair capacity audit gives

\[
\sum_f(T_{f,H}-V_f)_+
=\bigl(e^{-A^2}\Delta(A)+o_A(1)\bigr)W,
\qquad \Delta(A)>0.
\tag{7.3d}
\]

An exceptional set of size \(r=o_A(W/H)=o_A(W)\) can supply only \(r\)
additional lower boundary masks, far below (7.3d). Hence every recursive
packet packing satisfying (7.3b) must change pair frames on a positive
Gaussian scale. Gluing strata within one fixed frame cannot prove Lemma
7.1.

The exact recursive selection problem is the common-base matching gate from
MATH_ATTACK_EP_TAGH_COMMON_BASE_RECURSIVE_AUDIT_20260725.md: at every layer
one must choose the lower and upper Boolean perfect matchings on the same
active set, and a rotor edge survives only when both matchings take their
two edge-forced values. The recursive cycles prove that this agreement is
locally possible; an integral, multi-frame selection with total loss
\(o_A(W/H)\) is still open.

### Lemma target 7.2 (two-sided fibre detours)

For an SCD and tag-\(H\) rotor backbone as in Lemma 7.1, one can jointly
choose:

1. an assignment \(\phi\) satisfying (7.1) and the \(O_A(H)\) load bound;
2. for every anchor \(U\), a disjoint ordered split
   \[
   \mathcal F_U=\mathcal F_U^-\sqcup\mathcal F_U^+;
   \tag{7.4}
   \]
3. one radius-\(H\) extension of every shorter chain;

so that every backbone edge \(\omega_U\to\omega_V\) is either retained
unchanged, with

\[
\mathcal F_U^+=\mathcal F_V^-=\varnothing,
\tag{7.5}
\]

or is replaced by a two-sided detour

\[
\boxed{
\omega_U
\longrightarrow A_1\longrightarrow\cdots\longrightarrow A_r
\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_s
\longrightarrow\omega_V,
}
\tag{7.6}
\]

where

\[
(A_1,\ldots,A_r)=\mathcal F_U^+,qquad
(B_1,\ldots,B_s)=\mathcal F_V^-,qquad r,s\ge1.
\tag{7.7}
\]

All arrows before \(A_r\to B_1\) are promotions in top fibre \(U\), the
middle arrow \(A_r\to B_1\) is one rotor shift from top \(U\) to top
\(V\), and all later arrows are promotions in fibre \(V\). At path
boundaries, the unused incoming or outgoing lists can be covered by a total
of \(o_A(W/H)\) additional paths. Every shorter chain occurs in exactly one
list.

The first chain \(A_1\) must be an outgoing port from Proposition 5.6, and
the last chain \(B_s\) must be an incoming port from Proposition 5.4. The
interior promotion steps and the central rotor step are the remaining exact
correlations. Proposition 6.1 proves that the condition \(r,s\ge1\) is
necessary for every nontrivial detour of this one-rotor form; a one-sided
version of Lemma 7.2 is false.

For recursive packet cycles it is better not to cut the tag-\(H\) cycle
first. Construct the detours cyclically, then cut one resulting edge per
packet. This removes artificial initial/terminal fibre losses; only the
exceptional tag-\(H\) states and genuinely unthreaded shorter chains enter
the boundary ledger.

### Proposition 7.2a (critical density of paired interfaces)

Assume the load bound \(|\mathcal F_U|\le K_A(m)\), and suppose \(b\)
shorter chains are handled in boundary paths rather than in detours (7.6).
If \(D\) backbone edges are detoured, then

\[
\boxed{
D\ge\frac{W-N_H-b}{2K_A(m)}.
}
\tag{7.8}
\]

In particular, if \(b=o_A(W)\), then

\[
D=\Omega_A(W/H).
\tag{7.9}
\]

Also \(D\le(W-N_H-b)/2\), because Proposition 6.1 requires at least one
distinct shorter chain on each side of every detoured edge.

#### Proof

One detour on \(U\to V\) contains at most

\[
|\mathcal F_U^+|+|\mathcal F_V^-|\le2K_A(m)
\]

shorter chains. The detours contain exactly \(W-N_H-b\) shorter chains,
which proves (7.8). Since \(W-N_H=\Theta_A(W)\) for fixed \(A>0\) and
\(K_A(m)=O_A(H)\), equation (7.9) follows. The upper bound follows from
the two nonempty sides in Proposition 6.1. \(\square\)

Thus even the bounded-load matching theorem leaves a critical-density
\(\Theta(W/H)\)-scale family of paired interfaces to solve. The point of a
successful detour is that it pays one bridge entry, not an initialization
reset; the proposition is a compatibility toll, not by itself a lower
bound on final OR-word excess.

### Theorem 7.3 (backbone plus two-sided detours implies EP)

If Lemma targets 7.1 and 7.2 hold with total boundary paths
\(o_A(W/H)\), then \(\mathrm{EP}_A\) holds.

#### Proof

Replace every selected backbone edge by its path (7.6), retaining the
edges satisfying (7.5). The lists in (7.4) partition all shorter chains,
so the resulting threads are vertex-disjoint and use every SCD chain once.
Every transition is bridge one by Lemma 7.2. A cyclic packet thread is cut
once; a backbone path retains its original component count. Adding the
declared boundary paths gives \(o_A(W/H)\) components. The chosen extension
of each chain therefore forms the path cover required by
\(\mathrm{EP}_A\). \(\square\)

Theorem 4.1 proves only that a bounded-load assignment (7.1) exists. It
cannot be selected independently and then frozen: the split (7.4), the two
port tests, the internal promotion order, and the central rotor arc must all
be chosen jointly. The remaining sufficient statements are:

* Lemma 7.1 is a stronger-than-necessary recursive route through the
  tag-\(H\) no-extension mass. For small \(A\), Proposition 5.2 forces a
  positive linear subforest there, though not a path cover of the whole
  tag-\(H\) class.
* Lemma 7.2 is the exact two-sided interface problem in which promotion and
  the \(H-d\) collar coordinates of shorter chains must be used.

## 8. Audit of tempting shortcuts

1. **Promotions alone.** False for small \(A\) by (5.4). A positive linear
   number of tag-\(H\) rotor arcs is necessary.
2. **First-band Johnson matching.** Insufficient. It verifies (6.4) only at
   the middle-owner level and does not enforce the full word shift
   (6.2)--(6.3).
3. **Independent collar choices.** They give the correct local extension
   multiplicities but not a common incoming/outgoing state for a path
   vertex.
4. **Assign every shorter chain to an arbitrary top.** The inclusion
   capacity must be checked. Theorem 4.1 supplies the exact capacitated Hall
   proof and the \(O_A(H)\) load.
5. **Ignore tag \(H\).** Impossible. It contains \(N_H=\Theta_A(W)\)
   no-extension states and forces the rotor density (5.2).
6. **Reset between top fibres.** At the required density, this returns to
   the linear interface toll. Backbone transitions must be bridge-one rotor
   arcs.
7. **One fixed pair frame.** Impossible for the recursive packet route.
   The positive Gaussian deficit (7.3d) is linear in \(W\), whereas the
   allowed exceptional set is \(o(W/H)\). Pair frames must change.
8. **Target-fibre-only substitution.** False by Proposition 6.1. A
   nontrivial one-rotor detour needs shorter chains on both the source and
   target sides of the rotor.
9. **Near-Ucycle normalization.** Not used. EP is a sufficient decorated-SCD
   construction and is not asserted to characterize arbitrary near-optimal
   OR words.

## 9. Theorem ledger

### Proved

1. The exact full-collar representation of every tagged SCD chain.
2. The induced Johnson owner transition for rotor and promotion arcs.
3. Promotion preserves the collar top; rotor shifts move it by one Johnson
   edge.
4. Exact first-band lower/upper compatibility for positive tags.
5. An integral capacitated matching assigning all shorter chains to
   tag-\(H\) promotion fibres with load \(O_A(H)\).
6. The exact promotion-predecessor star and its \(d+1\) tag-\(d\) port
   templates, including the multiplicity \(H-d\) of the residual template.
7. The exact terminal-port Hall criterion (5.17).
8. The exact outgoing promotion-port templates and their \(m-H\) collar
   multiplicity.
9. Promotion cannot join distinct tag-\(H\) chains.
10. Every EP path cover must contain at least \((2N_H-W-p)_+\) tag-\(H\)
   rotor arcs.
11. The exact tag-\(H\) shift graph, its forced word-overlap rule, and the
    no-one-sided-substitution interface toll.
12. The critical paired-interface density bound (7.8).
13. The divisibility-safe recursive-packet reduction to Lemma 7.1, together
    with the fixed-frame Gaussian no-go.
14. Lemmas 7.1--7.2 together imply \(\mathrm{EP}_A\).

### Still open

1. A multi-frame clipped SCD with the tag-\(H\) rotor backbone in Lemma
   7.1, for example via the exceptional-packet bound (7.3b).
2. The joint two-sided fibre-detour lemma 7.2.
3. Therefore \(\mathrm{EP}_A\), \(\mathrm{MFUP}_A\), and coefficient one.

The gain from the EP reformulation is now exact. All shorter chains admit a
bounded-load integral placement into promotion fibres. For small \(A\), an
unavoidable global module is a positive-density no-extension tag-\(H\)
rotor subforest. The sufficient programme strengthens it to a spanning
tag-\(H\) backbone. Even after that is built, promotion requires a globally
correlated assignment whose exact local atom is a two-sided detour across
an oriented backbone edge.
