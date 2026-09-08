# Rotor--SCD toll, recursive surgery, and exact lower-bound certificates

Date: 2026-07-25

Source re-audited:
MATH_ATTACK_J_ROTOR_SCD_RESOLUTION_20260724.md.

Standing notation is as follows. Put

\[
n=2m,
\qquad
W=\binom{2m}{m},
\qquad
N_d=\binom{2m}{m-d},
\qquad
c_d=N_d-N_{d+1},
\]

with \(N_{m+1}=0\), and put \(Q_m=(2m-1)(2m)!\). Fix a band
\(H\le m-2\). A full SCD clipped to this band has

\[
\gamma_d=c_d\quad(0\le d<H),
\qquad
\gamma_H=N_H,
\qquad
\sum_{d=q}^H\gamma_d=N_q.
\]

A radius-\(d\) chain state is

\[
\omega=(L;z_1,\ldots,z_{2d};R),
\qquad |L|=|R|=m-d,
\]

and represents the chain
\(L,L+z_1,\ldots,L+z_1+\cdots+z_{2d}\). For \(d\ge1\), its directed
rotor successors are

\[
(L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}),
\qquad x\in L,\ y\in R.
\]

Write \(G_d\) for this rotor graph. If \(\mathcal D_d\) is the
radius-\(d\) state class of a clipped SCD, then
\(p_d^*(\mathcal D)\) is the minimum number of components of a spanning
vertex-disjoint directed path forest in \(G_d[\mathcal D_d]\). At radius
zero the rotor is the ordinary lower/residual coordinate swap; its exact
prefix weight is zero, so its detailed formula will not be needed.

## 1. Verdict

The patched rotor/SCD report is correct at the \(o(W)\) level, but its finite
ledger is not yet fully synchronized.

The exact hard-reset rotor-prefix toll is

\[
\widehat\iota_d=2d\qquad(0\le d<m),
\]

whereas

\[
\iota_d=2d+1\qquad(0\le d<m)
\]

is a conservative canonical-reset toll. Both are useful, but they must not
share one symbol \(R_H\). At the terminal radius \(d=m\), both all-start
ledgers use the exceptional toll \(2m-1\). All fixed-window statements below
retain \(H\le m-2\), so the exception never enters their proofs.

The no-averaging theorem is valid for either ledger, and more generally for
arbitrary nonnegative radius weights. The patched Verdict states the exact
prefix identity with \(\widehat\Phi_H\), while Theorem 2.1 still states and
proves only the conservative identity with \(\Phi_H\). The missing exact
statement is true by the same proof, but it should be stated explicitly.

The separate physical initialization cost is not bounded purely by a
constant times \(\widehat\Phi_H\), because radius zero has exact prefix toll
zero. The correct estimate, for every fixed positive window and all
sufficiently large \(m\), is

\[
I_{\rm phys}
\le 2Q_m\Phi_H
\le 3Q_m\widehat\Phi_H+\frac{2Q_mW}{m+1}.
\tag{1.1}
\]

Thus the exact prefix and conservative reset ledgers have the same
\(o(Q_mW)\) threshold, and small toll in either ledger makes physical
initialization \(o(Q_mW)\) after the additive \(O(Q_mW/m)\) term is
retained. No converse from small initialization cost alone is asserted.
Here (1.1) compares the ledgers attached to the same SCD, forest system, and
orbit construction; it is not a two-sided comparison of independently
optimized initialization and run costs.

The exploration beyond audit gives four unconditional advances.

1. A universal Johnson-label Hall theorem lower-bounds the corrected toll
   \(\widehat\Phi_H\) by exact multilevel deficiencies.
2. Every SCD retaining one stationary coordinate-pair frame has toll
   \(\Theta_A(W\sqrt m)\), and an \(o(W)\)-toll SCD must place at least half
   of its central pair labels outside any fixed frame.
3. The minimum path-component statistic is \(2\)-Lipschitz under chain-state
   replacement. Consequently an \(o(W)\)-toll SCD must differ from every
   permuted BTK SCD on a positive fraction of the chains in every fixed
   typical-radius annulus.
4. Standard two-coordinate product recursion has a two-phase local
   rigidity. In the two radius-\(d\) child lanes of a prescribed parent
   radius-\(d\) box, every parent rotor edge lifts to exactly one lane,
   never both. Relative to any one prescribed faithful forest lift, low
   child toll requires every optimal child-forest witness to use
   \(\Omega(W)\) selected annular arcs outside that lift.

These are no-go theorems for precisely specified sparse recursive-surgery
classes. They do not prove a universal \(\Omega(W)\) lower bound for
arbitrary SCDs and do not refute \(\mathrm{RSCD}_A\). The remaining
constructive target must at least have every optimal forest witness far, in
selected-edge distance, from every prescribed faithful forest lift; the
theorem does not classify those new edges relative to a different parent
forest.

## 2. Re-audit of the patched toll formulas

Throughout this section \(H\le m-2\), as in the clipped-band master. Thus
all displayed radius weights are nonterminal weights.

Put

\[
\widehat\Phi_H(\mathcal D)
=\sum_{d=0}^H2d\,p_d^*(\mathcal D),
\qquad
\Phi_H(\mathcal D)
=\sum_{d=0}^H(2d+1)p_d^*(\mathcal D).
\tag{2.1}
\]

For \(H\ge1\),

\[
\widehat\Phi_H
\le\Phi_H
\le\frac32\widehat\Phi_H+\frac{W}{m+1}.
\tag{2.2}
\]

Indeed,

\[
\Phi_H-\widehat\Phi_H=\sum_{d=0}^Hp_d^*,
\]

\[
p_0^*\le c_0=\frac{W}{m+1},
\]

and

\[
\sum_{d=1}^Hp_d^*
\le\frac12\sum_{d=1}^H2d\,p_d^*
=\frac12\widehat\Phi_H.
\]

The \(H\ge1\) qualification is automatic for
\(H=\lceil A\sqrt m\rceil\), fixed \(A>0\), and large \(m\).

### 2.1 Exact prefix length

For \(0\le d<m\), a radius-\(d\) state

\[
\omega=(L;z_1,\ldots,z_{2d};R)
\]

has chain masks

\[
L,\quad L+z_1,\quad\ldots,\quad L+z_1+\cdots+z_{2d}.
\]

After a hard reset, write

\[
\{z_{2d}\},\ldots,\{z_1\},L.
\tag{2.3}
\]

The final \(j+1\) entries have OR
\(L+\{z_1,\ldots,z_j\}\). A rotor successor costs one further entry.
Therefore a run through \(t\) states has hard-reset prefix length

\[
\boxed{t+2d.}
\tag{2.4}
\]

Within this model the bound is exact: the first endpoint must expose
\(2d+1\) distinct suffix ORs and hence needs at least \(2d+1\) entries, and
the remaining \(t-1\) states require later endpoints.

The residual block \(R\) need not be written. Unseen coordinates may be
treated as one virtual oldest block; alternatively, one global universe
sentinel can be written once. This exactness is only for the stipulated
hard-reset prefix architecture. It is not a lower bound for arbitrary OR
words sharing setup between runs or witnessing one chain at scattered
endpoints.

Writing \(R\) as well gives length \(t+2d+1\), the conservative convention.

### 2.2 The correct weighted chronology theorem

Let \(w_0,\ldots,w_H\ge0\). Define

\[
\Phi_w(\mathcal D)=\sum_{d=0}^Hw_dp_d^*(\mathcal D)
\]

and let \(R_w\) be the total number of hard-started monochromatic runs,
weighted by \(w_d\) at radius \(d\).

### Theorem 2.1 (arbitrary-weight no-averaging)

Let \(H\le m-2\). For the exact \(Q_m\)-color rotor master on that band,

\[
\boxed{
\min R_w
=Q_m\min_{\mathcal D\ {\rm full\ SCD}}\Phi_w(\mathcal D).
}
\tag{2.5}
\]

### Proof

For every fixed colored chronology, the runs of color \(c\) in radius \(d\)
are vertex-disjoint directed paths spanning \((\mathcal D_c)_d\). A physical
cut turns a cyclic monochromatic circuit into one path. Hence

\[
r_{c,d}\ge p_d^*(\mathcal D_c),
\]

and nonnegativity of \(w_d\) gives the lower bound in (2.5).

For the upper bound, choose one SCD \(\mathcal D\) and optimal forests
\(F_d\). The complete labeled coordinate orbit uses each state and each
selected forest arc with the exact stabilizer multiplicities. After the
selected arcs are removed from the master, every state has equally many
residual incoming arcs, residual outgoing arcs, colored path starts, and
colored path ends. Pair incoming residual arcs with starts, contract each
connector-plus-path trail, and Eulerize the balanced macrograph. Every
master-arc copy is used and at most \(Q_mp_d^*\) hard runs remain at radius
\(d\). This proves the matching upper bound. \(\square\)

Taking \(w_d=2d\) yields

\[
\boxed{
\widehat R_H^*
=Q_m\min_{\mathcal D}\widehat\Phi_H(\mathcal D),
}
\tag{2.6}
\]

while \(w_d=2d+1\) yields the patched Theorem 2.1 with \(\Phi_H\).

### 2.3 Remaining finite-ledger corrections

The following distinctions remain necessary in the patched source.

1. Sections 4--5 use \(2d+1\) in pseudo-color switching, capacity, sparse
   repair, and block-permutation bounds. These are correct conservative
   estimates; the exact prefix version uses \(2d\).
2. Proposition 6.1 cites the prefix formula but writes path length
   \(W+\Phi_i\). The literal prefix construction gives
   \[
   W+\widehat\Phi_i\le W+\Phi_i.
   \]
   Its conclusion remains valid.
3. Likewise, the exact direct realization in Section 8 is
   \(W+\widehat\Phi_H\); \(W+\Phi_H\) is a conservative construction.
4. Both all-start identities are correct:
   \[
   \sum_{d=0}^{m-1}2d\,c_d+(2m-1)c_m
   =4^m-W-1
   \tag{2.7}
   \]
   for prefix extraction, while
   \[
   \sum_{d=0}^{m-1}(2d+1)c_d+(2m-1)c_m
   =4^m-2
   \tag{2.8}
   \]
   for the conservative weights. Indeed, summation by parts in
   \(c_d=N_d-N_{d+1}\) turns (2.7) into
   \(2\sum_{q=1}^mN_q-1=4^m-W-1\). The left side of (2.8) exceeds that
   of (2.7) by \(\sum_{d<m}c_d=W-1\).
5. The initialization estimate \(2Q_m\Phi_H\) and the combined conservative
   charge \(3Q_m\Phi_H\) are correct. Equation (1.1), not a pure constant
   factor, is the comparison to the exact prefix ledger.

No state-orbit, arc-orbit, Eulerization, pseudo-color, or RSCD asymptotic
factor error remains.

## 3. Universal Johnson-label Hall lower bound

Let \(\mathcal D\) be one full SCD of \(B_{2m}\), clipped at radius
\(H\le m-2\).
For a radius-\(d\) chain state

\[
\omega=(L;z_1,\ldots,z_{2d};R)
\]

and \(1\le q\le d\), define its rank-\((m-q)\) and rank-\((m+q)\) masks

\[
A_q(\omega)
=L\cup\{z_1,\ldots,z_{d-q}\},
\]

\[
B_q(\omega)
=L\cup\{z_1,\ldots,z_{d+q}\},
\]

and the central difference label

\[
Z_q(\omega)
=B_q(\omega)\setminus A_q(\omega)
=\{z_{d-q+1},\ldots,z_{d+q}\}.
\tag{3.1}
\]

Thus \(Z_q(\omega)\in\binom{[2m]}{2q}\).

### Lemma 3.1 (exact Johnson projection)

If \(\omega\to\omega'\) is a rotor edge and \(q\le d\), then

\[
\boxed{
|Z_q(\omega)\cap Z_q(\omega')|=2q-1.
}
\tag{3.2}
\]

### Proof

For \(q<d\), the successor singleton word is
\((x,z_1,\ldots,z_{2d-1})\), and therefore

\[
Z_q(\omega')
=\{z_{d-q},\ldots,z_{d+q-1}\}.
\]

This replaces \(z_{d+q}\) by \(z_{d-q}\). For \(q=d\),

\[
Z_d(\omega')
=\{x,z_1,\ldots,z_{2d-1}\},
\]

which replaces \(z_{2d}\) by \(x\). \(\square\)

Let

\[
\mathcal V_q=\bigcup_{d=q}^H\mathcal D_d.
\]

The maps \(A_q\) and \(B_q\) are bijections from \(\mathcal V_q\) onto
\(\binom{[2m]}{m-q}\) and \(\binom{[2m]}{m+q}\), respectively. Hence

\[
|\mathcal V_q|=N_q.
\tag{3.3}
\]

Define the multiplicity function

\[
\mu_q(Z)
=|\{\omega\in\mathcal V_q:Z_q(\omega)=Z\}|.
\tag{3.4}
\]

It has total mass \(N_q\) and the exact one-design margins

\[
\boxed{
\sum_{Z\ni i}\mu_q(Z)
=
\binom{2m-1}{m+q-1}
-
\binom{2m-1}{m-q-1}
}
\tag{3.5}
\]

for every coordinate \(i\). This follows by subtracting, over the two rank
layers, the numbers of upper and lower masks containing \(i\).

Let \(J_q=J(2m,2q)\), with two labels adjacent when their intersection has
size \(2q-1\). For a label family \(\mathcal S\), define the full union of
vertex-neighborhoods

\[
\Gamma_q(\mathcal S)
=
\{Z':\exists Z\in\mathcal S,\ |Z\cap Z'|=2q-1\}.
\tag{3.5a}
\]

This set is allowed to intersect \(\mathcal S\) when \(\mathcal S\)
contains adjacent labels. Put

\[
\mu_q(\mathcal S)=\sum_{Z\in\mathcal S}\mu_q(Z).
\]

For chosen radiuswise path forests define

\[
P_q=\sum_{d=q}^Hp_d.
\tag{3.6}
\]

### Theorem 3.2 (weighted label-Hall deficiency)

Every choice of spanning rotor path forests satisfies

\[
\boxed{
P_q\ge
\max_{\mathcal S\subseteq\binom{[2m]}{2q}}
\bigl(\mu_q(\mathcal S)-\mu_q(\Gamma_q(\mathcal S))\bigr)_+.
}
\tag{3.7}
\]

Consequently,

\[
\boxed{
\widehat\Phi_H(\mathcal D)
\ge
2\sum_{q=1}^H
\max_{\mathcal S}
\bigl(\mu_q(\mathcal S)-\mu_q(\Gamma_q(\mathcal S))\bigr)_+.
}
\tag{3.8}
\]

### Proof

The union of the forests over \(d\ge q\) has \(P_q\) path ends. Among the
\(\mu_q(\mathcal S)\) vertices labelled in \(\mathcal S\), all but at most
\(P_q\) have a selected successor. Distinct sources have distinct
successors because forest indegree is at most one. Lemma 3.1 places every
successor label in \(\Gamma_q(\mathcal S)\). Therefore

\[
\mu_q(\mathcal S)-P_q
\le\mu_q(\Gamma_q(\mathcal S)),
\]

which proves (3.7). For the consequence (3.8), now choose the optimal
forest at every radius, so \(p_d=p_d^*(\mathcal D)\). Then

\[
\widehat\Phi_H
=\sum_{d=1}^H2d\,p_d
=2\sum_{q=1}^HP_q,
\tag{3.9}
\]

and summing (3.7) proves (3.8). \(\square\)

### Corollary 3.3 (independent-label certificate)

If \(\mathcal I\) is independent in \(J_q\), and

\[
M_q=\mu_q(\mathcal I),
\]

then

\[
\boxed{
P_q\ge(2M_q-N_q)_+.
}
\tag{3.10}
\]

Indeed, \(\Gamma_q(\mathcal I)\cap\mathcal I=\varnothing\), so
\(\mu_q(\Gamma_q(\mathcal I))\le N_q-M_q\).

The theorem is universal, but it need not give a positive numerical
deficiency for a diffuse label distribution. The uniform fractional label
measure has perfect one-design margins and no Hall obstruction. Thus
the one-design equations together with their fractional single-level Hall
relaxation cannot settle \(\mathrm{RSCD}_A\). This does not exclude an
argument using one-level integrality or SCD realizability; an additional
source of structure is the integral nested compatibility of all \(Z_q\)
levels.

## 4. Stationary coordinate-pair recursion is impossible

Fix a perfect matching \(\mathcal P\) of the \(2m\) coordinates and define

\[
\mathcal U_q(\mathcal P)
=
\left\{
\bigcup_{e\in Q}e:
Q\subseteq\mathcal P,\ |Q|=q
\right\}.
\tag{4.1}
\]

Two distinct members of \(\mathcal U_q(\mathcal P)\) intersect in at most
\(2q-2\) coordinates. Hence this family is independent in
\(J(2m,2q)\).

### Theorem 4.1 (paired-label lower bound)

Let \(E_q\) be the number of states in \(\mathcal V_q\) whose label
\(Z_q\) does not belong to \(\mathcal U_q(\mathcal P)\). Then

\[
\boxed{
P_q\ge(N_q-2E_q)_+,
}
\tag{4.2}
\]

and

\[
\boxed{
\widehat\Phi_H
\ge2\sum_{q=1}^H(N_q-2E_q)_+.
}
\tag{4.3}
\]

### Proof

Apply Corollary 3.3 with
\(M_q=N_q-E_q\), and then use (3.9). \(\square\)

Call an SCD centrally \(\mathcal P\)-paired if every positive-radius state
has \(Z_1(\omega)\in\mathcal P\).

### Corollary 4.2 (exact stationary-pair obstruction)

For a centrally \(\mathcal P\)-paired SCD, every positive-radius induced
rotor graph is empty. Therefore

\[
p_d^*(\mathcal D)=\gamma_d\qquad(1\le d\le H)
\]

and

\[
\boxed{
\widehat\Phi_H(\mathcal D)
=\sum_{d=1}^H2d\,\gamma_d
=2\sum_{q=1}^HN_q.
}
\tag{4.4}
\]

### Proof

Along a rotor edge, the two \(Z_1\)-labels share exactly one coordinate.
Two edges of the fixed perfect matching are either equal or disjoint.
Hence no rotor edge joins two centrally paired states. The telescoping
identity in (4.4) follows from
\(\sum_{d=q}^H\gamma_d=N_q\). \(\square\)

In particular, the coordinate-orbit construction generated by this SCD has
exact minimum hard-reset prefix run-start overhead

\[
Q_m\widehat\Phi_H
=2Q_m\sum_{q=1}^HN_q,
\tag{4.4a}
\]

by the fixed-SCD lower and upper halves of Theorem 2.1. Thus (4.4) is an
exact unavoidable radius-weighted run-start toll for that complete
coordinate orbit, not merely an estimate for one chronology.

For \(H=\lceil A\sqrt m\rceil\),

\[
\boxed{
\frac{\widehat\Phi_H(\mathcal D)}{W\sqrt m}
\longrightarrow
2\int_0^Ae^{-x^2}\,dx
=\sqrt\pi\,\operatorname{erf}(A).
}
\tag{4.5}
\]

For completeness, the Gaussian estimate used here and below follows from
the exact product

\[
\frac{N_q}{W}
=\prod_{j=0}^{q-1}\frac{m-j}{m+j+1}.
\tag{4.5a}
\]

Uniformly for \(0\le q\le A\sqrt m\), Taylor expansion with a uniform
remainder gives

\[
\log\frac{N_q}{W}
=-\frac1m\sum_{j=0}^{q-1}(2j+1)
+\frac1{2m^2}\sum_{j=0}^{q-1}(2j+1)
+O_A\!\left(\frac1{m^3}\sum_{j=0}^{q-1}(j+1)^3\right)
=-\frac{q^2}{m}+O_A(m^{-1}).
\tag{4.5b}
\]

Consequently \(N_q/W=e^{-q^2/m}(1+O_A(m^{-1}))\), uniformly on the
window. Substitution into

\[
\frac{2}{W\sqrt m}\sum_{q=1}^{\lceil A\sqrt m\rceil}N_q
\]

and the Riemann-sum theorem prove (4.5), including the harmless rounded
endpoint.

Moreover, the \(q=1\) part of (4.2) gives the stability statement

\[
\widehat\Phi_H\ge2(N_1-2E_1)_+.
\tag{4.6}
\]

Thus \(\widehat\Phi_H=o(W)\) forces

\[
\boxed{
E_1\ge\frac12N_1-o(W)
=\left(\frac12-o(1)\right)W.
}
\tag{4.7}
\]

Equivalently, every low-toll target has at least
\(N_1/2-o(W)\) states whose \(Z_1\)-label lies outside the prescribed frame.
In particular, a construction keeping all but \(o(W)\) of these labels
inside one stationary frame cannot reach low toll. This is an off-frame
count, not a general edit-distance theorem.

## 5. Exact stability under chain-state surgery

The following metric lemma applies to every pair of SCDs and does not use a
special recursion.

### Theorem 5.1 (two-Lipschitz path-component statistic)

Let \(\mathcal D,\mathcal E\) be full SCDs clipped to the same band. At
radius \(d\), put

\[
M_d
=|\mathcal D_d\setminus\mathcal E_d|
=|\mathcal E_d\setminus\mathcal D_d|.
\tag{5.1}
\]

Then

\[
\boxed{
\left|p_d^*(\mathcal D)-p_d^*(\mathcal E)\right|
\le2M_d.
}
\tag{5.2}
\]

Consequently,

\[
\boxed{
\left|
\widehat\Phi_H(\mathcal D)-\widehat\Phi_H(\mathcal E)
\right|
\le4\sum_{d=1}^HdM_d.
}
\tag{5.3}
\]

### Proof

Let \(F\) be an optimal spanning path forest on \(\mathcal D_d\). It has
\(\gamma_d-p_d^*(\mathcal D)\) edges. Delete the \(M_d\) vertices in
\(\mathcal D_d\setminus\mathcal E_d\) and their incident edges. Because
\(F\) is a path forest, at most \(2M_d\) edges are deleted. The remaining
edges lie on the common state set. Add the \(M_d\) missing vertices of
\(\mathcal E_d\) as singletons. This is a spanning path forest on
\(\mathcal E_d\), so

\[
\gamma_d-p_d^*(\mathcal E)
\ge
\gamma_d-p_d^*(\mathcal D)-2M_d.
\]

Thus

\[
p_d^*(\mathcal E)
\le p_d^*(\mathcal D)+2M_d.
\]

Interchanging the two SCDs proves (5.2), and weighted summation proves
(5.3). \(\square\)

For radii \(d=\Theta(\sqrt m)\), (5.3) says that \(o(W)\) state
replacements change the weighted toll by only \(o(W\sqrt m)\). It therefore
cannot bridge a \(\Theta(W\sqrt m)\)-to-\(o(W)\) gap, as in the BTK
application below; no broader assertion about an unspecified “high” toll is
intended.

### 5.1 BTK is linearly far from every low-toll SCD

For the Greene--Kleitman/BTK SCD, and for every coordinate relabeling of it,
the induced positive-radius rotor graph is empty at every un-clipped radius.
A short stack proof is as follows. Encode a BTK lower endpoint by its ballot
word, with an up-step pushing and a down-step popping the most recent
unmatched up-step. Let \(L\) be the matched down positions, \(R\) the
matched up positions, and \(z_1<\cdots<z_{2d}\) the final persistent stack,
from bottom to top.
A rotor successor using \(x\in L\), \(y\in R\) would have to make

\[
x,z_1,\ldots,z_{2d-1}
\]

the new persistent unmatched sequence, so \(x<z_1\). If \(x<y\), the old
stack immediately before \(x\) is nonempty, because the down-step
at \(x\) was matched. If the new up-step at \(x\) survived forever, every
older stack item below it would survive too, producing a persistent item
before \(x\), a contradiction. If \(y<x\), the changes at \(y\) and \(x\)
restore the old height by time \(x\), and the two words have identical
letters thereafter. If the old stack is empty immediately after \(x\), the
modified height, which was two below the old height between \(y\) and
\(x\), has already underflowed; the modified word is not a BTK lower
endpoint. Otherwise the new \(x\) occupies the stack depth of an old
pre-\(x\) up-step. Since \(z_1>x\), that old item was eventually popped;
the identical future descent also pops the new \(x\). Again persistence
fails. Thus no positive-radius rotor edge remains inside the un-clipped BTK
SCD.
The rotor definition is equivariant under coordinate permutations, so the
same conclusion holds for every permuted BTK SCD.

Fix

\[
0<a<b<A,\qquad H=\lceil A\sqrt m\rceil,
\]

and let \(\mathcal B\) be any permuted BTK SCD. For another SCD
\(\mathcal D\), define \(M_d\) by (5.1). Since

\[
p_d^*(\mathcal B)=c_d
\qquad
(a\sqrt m\le d\le b\sqrt m)
\]

for large \(m\), Theorem 5.1 gives

\[
\widehat\Phi_H(\mathcal D)
\ge
\sum_{a\sqrt m\le d\le b\sqrt m}
2d(c_d-2M_d).
\tag{5.4}
\]

Uniformly for \(d=x\sqrt m\), \(x\in[a,b]\),

\[
\frac{N_d}{W}=e^{-x^2}+o(1),
\qquad
\frac{c_d}{W}
=\frac{2x}{\sqrt m}e^{-x^2}+O_{a,b}(m^{-1}).
\tag{5.5}
\]

Indeed, the first estimate is (4.5b), while

\[
c_d=N_d-N_{d+1}
=N_d\frac{2d+1}{m+d+1}.
\tag{5.5a}
\]

Since \(a\le x\le b\), inserting (4.5b) in (5.5a) gives the second
estimate in (5.5), uniformly with error \(O_{a,b}(m^{-1})\). Therefore

\[
\frac{2d\,c_d}{W\sqrt m}
=\frac1{\sqrt m}
\left(4x^2e^{-x^2}+O_{a,b}(m^{-1/2})\right),
\]

and summing proves the Riemann limit (5.6).

Hence

\[
\frac1{W\sqrt m}
\sum_{a\sqrt m\le d\le b\sqrt m}2dc_d
\longrightarrow
4\int_a^b x^2e^{-x^2}\,dx.
\tag{5.6}
\]

### Corollary 5.2 (no sparse BTK surgery)

If

\[
\widehat\Phi_H(\mathcal D)=o(W),
\]

then

\[
\boxed{
\sum_{a\sqrt m\le d\le b\sqrt m}dM_d
\ge
\left(
\int_a^b x^2e^{-x^2}\,dx-o(1)
\right)W\sqrt m
}
\tag{5.7}
\]

and therefore

\[
\boxed{
\sum_{a\sqrt m\le d\le b\sqrt m}M_d
\ge
\left(
\frac1b\int_a^b x^2e^{-x^2}\,dx-o(1)
\right)W.
}
\tag{5.8}
\]

Thus, for every fixed \(0<a<b<A\), a successful SCD must replace a positive
fraction of the chains in that annulus of every permuted BTK SCD. In
particular, no \(o(W)\)-chain whole-chain surgery around BTK can prove
\(\mathrm{RSCD}_A\).

## 6. Exact whole-chain multicolor trades

The two-color ownership overlay has a clean multicolor extension.

Let

\[
\mathcal D^{(1)},\ldots,\mathcal D^{(k)}
\]

be full SCDs. Form the \(k\)-partite ownership hypergraph whose part \(i\)
consists of the chain occurrences of \(\mathcal D^{(i)}\), and whose
hyperedge for a mask \(M\) is

\[
e_M=
\{
\operatorname{own}_{\mathcal D^{(i)}}(M):1\le i\le k
\}.
\tag{6.1}
\]

The occurrences remain side-labelled even when two source chains are
identical as set systems.

### Theorem 6.1 (rainbow characterization)

A whole-chain \(k\)-color trade is exactly a map

\[
\varphi:
\{\text{all source chain occurrences}\}\longrightarrow[k]
\]

whose restriction to every ownership hyperedge \(e_M\) is a bijection onto
\([k]\).

### Proof

The multiplicity of \(M\) in target color \(c\) is

\[
|\{i:
\varphi(\operatorname{own}_{\mathcal D^{(i)}}(M))=c\}|.
\]

Every target color owns \(M\) exactly once if and only if the \(k\) values
on \(e_M\) are all distinct. \(\square\)

This is an integral rainbow-coloring problem, not a Birkhoff average.

There is a useful rigidity certificate. In part \(i\), join two chain
occurrences \(C,C'\) in the equality graph if there are masks \(M,M'\) for
which the owners agree in every part \(j\ne i\), while the \(i\)-owners are
\(C,C'\).

### Corollary 6.2 (equality-component rigidity)

Every rainbow trade colors \(C\) and \(C'\) equally on each equality edge,
and hence is constant on every equality component. If the equality graph in
every part is connected, the only trades are global permutations of the
\(k\) source colors.

### Proof

The common \(k-1\) owners on \(e_M\) and \(e_{M'}\) use \(k-1\) distinct
colors. Both \(C\) and \(C'\) must receive the unique missing color. If every
part is connected, each part is monochromatic; one ownership hyperedge then
forces the \(k\) part-colors to be distinct. \(\square\)

For \(k=2\), this recovers the connected-overlay rigidity case of the
component-by-component ownership-overlay characterization.

## 7. Two-coordinate product phases: rigidity and a prescribed-lift obstruction

Let

\[
C=(C_0<C_1<\cdots<C_{2d}),\qquad d\ge1,
\]

be a parent symmetric chain, and add two new coordinates \(a,b\). The
standard phase-\(a\) decomposition of the box \(C\times B_{\{a,b\}}\)
consists of

\[
\mathsf A_a:
C_0,\ldots,C_{2d},C_{2d}+a,C_{2d}+a+b,
\]

\[
\mathsf B_a:
C_0+a,\ldots,C_{2d-1}+a,C_{2d-1}+a+b,
\]

\[
\mathsf D_b:
C_0+b,\ldots,C_{2d}+b,
\]

and

\[
\mathsf C:
C_0+a+b,\ldots,C_{2d-2}+a+b.
\tag{7.1}
\]

Phase \(b\) interchanges \(a,b\). The \(\mathsf C\)-chain is structurally
the same in both phases.

### Theorem 7.1 (local product-phase rigidity)

The ownership overlay of the two phases has exactly two connected
components:

1. the two side-labelled copies of \(\mathsf C\); and
2. one component containing all \(\mathsf A,\mathsf B,\mathsf D\) chains.

Consequently, every exact whole-chain two-color recombination chooses one
complete phase package in the parent box.

The same conclusion holds with arbitrarily many labelled copies of the two
phases over the same parent-chain box system: every target color receives
one complete phase-\(a\) or phase-\(b\) package structurally, and no third
local SCD type is created. Labels may still mix among copies inside the
chosen structural package.

### Proof

The cells \(C_j\) join \(\mathsf A_a\) to \(\mathsf A_b\). The lower
\(a\)-cells join \(\mathsf B_a\) to \(\mathsf D_a\), and the top \(a\)-cell
joins \(\mathsf A_a\) to \(\mathsf D_a\). The analogous \(b\)-cells join
\(\mathsf B_b,\mathsf D_b,\mathsf A_b\). The cell
\(C_{2d-1}+a+b\) joins \(\mathsf B_a\) to \(\mathsf B_b\), and
\(C_{2d}+a+b\) again joins \(\mathsf A_a\) to \(\mathsf A_b\). The cells
\(C_j+a+b\), \(0\le j\le2d-2\), join the two copies of
\(\mathsf C\), producing the separate component.

For the multicolor assertion, let

\[
A_a,A_b,B_a,B_b,D_a,D_b
\]

denote the numbers of structural chain types assigned to one target color.
Exact cell coverage gives

\[
A_a+A_b=1,\quad
B_a+D_a=1,\quad
A_a+D_a=1,
\]

\[
D_b+B_b=1,\quad
D_b+A_b=1,\quad
B_a+B_b=1.
\tag{7.2}
\]

Therefore

\[
B_a=D_b=A_a,\qquad
B_b=D_a=A_b,
\]

and \(A_a+A_b=1\) forces one complete phase package. The common
\(\mathsf C\)-type is selected once independently. \(\square\)

### 7.1 Exactly one natural lift per parent rotor edge

Write the parent chain state as

\[
C=(L;z_1,\ldots,z_{2d};R).
\]

If a box uses phase \(p\in\{a,b\}\), and \(q\) is the other new coordinate,
its two radius-\(d\) child states are

\[
\mathsf H_p(C)
=
(L+p;z_1,\ldots,z_{2d-1},q;R+z_{2d}),
\tag{7.3}
\]

\[
\mathsf S_q(C)
=
(L+q;z_1,\ldots,z_{2d};R+p).
\tag{7.4}
\]

Let \(C\to C'\) be a parent rotor edge using \(x\in L\), \(y\in R\).

### Lemma 7.2 (one-lane lifting)

If the source and target boxes have the same phase \(p\), then

\[
\mathsf S_q(C)\longrightarrow\mathsf S_q(C').
\tag{7.5}
\]

If the source box has phase \(p\) and the target box has phase \(q\), then

\[
\mathsf H_p(C)\longrightarrow\mathsf S_p(C').
\tag{7.6}
\]

Among the two radius-\(d\) states (7.3)--(7.4) in each of the two prescribed
parent radius-\(d\) boxes, these are the only child rotor arcs projecting to
the prescribed parent edge and using the same old coordinates \(x,y\).
Thus every boxwise phase field supplies exactly one such child lane, never
two. This statement does not classify radius-\(d\) states arising from
parent radii \(d-1\) or \(d+1\), nor arcs projecting to other parent edges.

### Proof

Substitute the parent successor

\[
C'=(L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d})
\]

into (7.3)--(7.4). Using the old \(x,y\) in the child rotor rule gives
(7.5) in the equal-phase case and (7.6) in the unequal-phase case. Any
child successor projecting to the specified old-coordinate successor must
exchange these same old \(x,y\); using \(a\) or \(b\) changes the projected
lower block. The displayed successor is therefore unique. \(\square\)

### Theorem 7.3 (prescribed-lift deficiency inequality)

Let a parent radius-\(d\) path forest have

\[
v=c_d^{(m)}
\]

vertices and \(p\) components. Fix any phase field on its parent boxes and
let \(\mathscr N_d\) be the \(v-p\) natural child arcs supplied by
Lemma 7.2.

Let \(F'_d\) be any spanning radius-\(d\) path forest in any child SCD of
\(B_{2m+2}\), including one obtained by chain splicing. Let \(s_d\) be the
number of selected arcs of \(F'_d\) not belonging to \(\mathscr N_d\).
Then

\[
\boxed{
p'_d\ge v+p-s_d\ge v-s_d.
}
\tag{7.7}
\]

### Proof

The child radius-\(d\) class has fixed size

\[
c_d^{(m+1)}
=c_{d-1}^{(m)}+2c_d^{(m)}+c_{d+1}^{(m)}
\ge2v,
\tag{7.8}
\]

as follows by decomposing every parent-chain product box. At most
\(v-p\) selected arcs of \(F'_d\) lie in \(\mathscr N_d\), and all other
selected arcs are counted by \(s_d\). Since a path forest with \(V\)
vertices and \(E\) edges has \(V-E\) components,

\[
p'_d
\ge2v-\bigl((v-p)+s_d\bigr)
=v+p-s_d.
\]

\(\square\)

Fix \(0<a<b<A\). If a sequence of child SCDs has

\[
\widehat\Phi_{\lceil A\sqrt{m+1}\rceil}=o(W_{m+1}),
\]

choose \(F'_d\) optimally at every radius, so that
\(p'_d=p_d^*\), and define \(s_d\) for these optimal forests. Then

\[
\sum_{a\sqrt m\le d\le b\sqrt m}p'_d
=o(W_m/\sqrt m).
\tag{7.9}
\]

Indeed, throughout the annulus \(2d\ge2a\sqrt m\), so the left side is at
most \(\widehat\Phi/(2a\sqrt m)\). The hypothesis and
\(W_{m+1}/W_m=4-2/(m+1)\) give (7.9).

Summing (7.7), using

\[
\sum_{a\sqrt m\le d\le b\sqrt m}c_d^{(m)}
=
\bigl(e^{-a^2}-e^{-b^2}+o(1)\bigr)W_m,
\]

where the estimate is immediate by telescoping: for
\(\ell=\lceil a\sqrt m\rceil\) and
\(u=\lfloor b\sqrt m\rfloor\), the sum is
\(N_\ell-N_{u+1}\), and (4.5b) applies. This gives the exact asymptotic
obstruction

\[
\boxed{
\sum_{a\sqrt m\le d\le b\sqrt m}s_d
\ge
\bigl(e^{-a^2}-e^{-b^2}-o(1)\bigr)W_m.
}
\tag{7.10}
\]

Thus arbitrary boxwise phase choices, two-color exchanges, or multicolor
copies cannot produce an optimal low-toll child forest that is an
\(o(W)\)-selected-edge perturbation of one prescribed faithful forest lift.
Equation (7.10) forces every optimal forest witness for the low child toll
to have linear selected-edge distance from that prescribed lift.

This does not exclude a globally reoptimized phase-field product. An arc
counted by \(s_d\) may be an entirely natural lift of another parent edge or
of another parent forest. Therefore (7.10) does not prove that
\(\Omega(W)\) arcs are intrinsically cross-lane, cross-origin, or
nonliftable; it proves only the stated distance from \(\mathscr N_d\).

## 8. Direct binary splicing also misses rotor neighbors

Let

\[
C_0<\cdots<C_{2d},
\qquad
C'_0<\cdots<C'_{2d}
\]

be equal-radius chains with \(d\ge1\). For \(0\le k<2d\), swapping their
tails after level \(k\) gives two chains if and only if

\[
C_k\subset C'_{k+1},
\qquad
C'_k\subset C_{k+1}.
\tag{8.1}
\]

### Proposition 8.1 (one-cut splice obstruction)

If \(C\to C'\) is a rotor edge, condition (8.1) fails at every cut.

### Proof

Write

\[
C_j=L\cup\{z_1,\ldots,z_j\}.
\]

For the rotor successor,

\[
C'_0=L-x+y,
\]

and, for \(j\ge1\),

\[
C'_j=L\cup\{y,z_1,\ldots,z_{j-1}\}.
\tag{8.2}
\]

One has

\[
C_j\subset C'_{j+1},
\]

but \(y\in C'_j\setminus C_{j+1}\). Thus the reciprocal inclusion always
fails. \(\square\)

A direct one-cut two-tail swap cannot make its two operated outputs be the
desired rotor-neighbor pair: tail swapping is an involution, so if its two
outputs formed such a pair, applying the same swap backward would contradict
Proposition 8.1. This does not rule out a binary splice whose changed output
becomes rotor-adjacent to a third, unchanged chain. Thus a construction
realizing the edge must involve that third chain, use multiple cuts, or
perform a global recombination.

## 9. What a successful recursion must prove

The preceding theorems rule out:

- a stationary coordinate-pair frame;
- \(o(W)\)-chain perturbations of BTK;
- local multicolor whole-chain mixing beyond the two product phases;
- an optimal low-toll child forest that is an \(o(W)\)-selected-edge
  perturbation of one prescribed faithful product forest lift; and
- a one-cut two-chain splice performed directly on a rotor-neighbor pair.

They do not rule out dense cross-box absorption.

Put \(H_m(A)=\lceil A\sqrt m\rceil\). A clean recursive sufficient lemma
is:

> **Fixed-window strict contraction lemma -- UNPROVED.** There are
> \(0<\eta<4\), \(\varepsilon_m\ge0\) with \(\varepsilon_m\to0\), and an
> exact recursive SCD operator
> \(T_m\) such that, for every fixed \(A>0\) and all
> \(m\ge m_0(A)\), the recursively related SCDs
> \(\mathcal D_{m+1}=T_m\mathcal D_m\) satisfy
> \[
> \widehat\Phi_{m+1,H_{m+1}(A)}(\mathcal D_{m+1})
> \le
> (4-\eta)
> \widehat\Phi_{m,H_m(A)}(\mathcal D_m)
> +\varepsilon_mW_m.
> \tag{9.1}
> \]

This lemma would prove \(\mathrm{RSCD}_A\). Indeed,

\[
\frac{W_{m+1}}{W_m}
=4-\frac{2}{m+1}.
\tag{9.2}
\]

Set

\[
x_m(A)
=\frac{\widehat\Phi_{m,H_m(A)}(\mathcal D_m)}{W_m}.
\]

After division by \(W_{m+1}\), (9.1) gives

\[
x_{m+1}(A)
\le
\frac{4-\eta}{4-2/(m+1)}x_m(A)
+\frac{\varepsilon_m}{4-2/(m+1)}.
\tag{9.3}
\]

For all large \(m\), the first coefficient is bounded by a constant
\(\rho<1\), while the second term tends to zero. The elementary
inhomogeneous contraction recurrence therefore forces

\[
x_m(A)\longrightarrow0,
\]

which is \(\mathrm{RSCD}_A\). A shifted-window version would also suffice
if the shifts were absolutely summable and the estimate uniform for \(A\)
in the resulting compact interval; a bare \(A+o(1)\) does not justify
iteration.

Theorem 7.3 proves that no optimal forest witness for an implementation of
(9.1) can remain an \(o(W)\)-selected-edge perturbation of any one prescribed
faithful parent forest lift. It does not rule out a globally reoptimized
standard-phase construction, because arcs outside that prescribed lift may
be natural for a different parent forest.

On the lower-bound side, Theorem 3.2 reduces a universal obstruction to the
nested Johnson-label problem

\[
\sum_{q\le A\sqrt m}
\max_{\mathcal S}
\bigl(
\mu_q(\mathcal S)-\mu_q(\Gamma_q(\mathcal S))
\bigr)_+.
\tag{9.4}
\]

Proving (9.4) is \(\Omega(W)\) for every SCD would refute
\(\mathrm{RSCD}_A\). No such universal bound is known. The one-design
identities (3.5) alone cannot prove it; the missing input would have to use
the nested relation among the labels \(Z_1\subset Z_2\subset\cdots\) inside
each chain state and the simultaneous two-sided SCD ownership.

## 10. Final theorem ledger

### Proved

1. The patched \(2d\) prefix toll is correct, and the arbitrary-weight
   no-averaging theorem supplies the missing exact identity.
2. The finite initialization comparison requires the additive
   \(O(Q_mW/m)\) term in (1.1).
3. The multilevel Johnson-label Hall bound (3.8) is universal.
4. Stationary paired recursions have exact toll \(2\sum_{q\le H}N_q\), and
   every \(o(W)\)-toll SCD places at least half of its central labels outside
   any prescribed pair frame.
5. The component statistic is two-Lipschitz under chain-state surgery, and
   every low-toll SCD is a positive linear distance from every permuted BTK
   SCD on each fixed typical-radius annulus.
6. Whole-chain multicolor trades are exactly rainbow ownership-hypergraph
   colorings.
7. In the two prescribed radius-\(d\) child lanes of a standard product
   box, each prescribed parent rotor edge has exactly one lift. Relative to
   any prescribed faithful parent forest lift, every optimal witness for low
   child toll uses \(\Omega(W)\) selected annular arcs outside that lift.
8. A direct one-cut binary splice cannot use the rotor-neighbor pair itself
   as its two operated chains.

### Still unproved

- A dense cross-lane absorption or strict-contraction construction.
- A universal positive lower bound for the nested Hall deficiency (9.4).
- \(\mathrm{RSCD}_A\) itself.

Accordingly, the exploration does not prove or refute the contiguous-OR
conjecture. It narrows the recursive lane sharply: low toll is impossible
within an \(o(W)\)-chain neighborhood of BTK, and no optimal low-toll forest
witness lies within an \(o(W)\)-selected-edge neighborhood of a prescribed
faithful product forest lift. A successful construction must reorganize a
linear fraction of the relevant Gaussian-window chain states or selected
transitions.

## 11. Adversarial audit

1. **Terminal radius.** Neither Theorem 2.1 nor the fixed-window deductions
   pass through \(d=m\). The only terminal statements are the static
   all-start identities (2.7)--(2.8), with exceptional toll \(2m-1\).
2. **Meaning of exact toll.** The lower bound \(t+2d\) is exact only for the
   stated hard-reset prefix architecture. It is not claimed for an arbitrary
   OR word that shares setup across runs or realizes chain masks at
   nonconsecutive endpoints.
3. **Initialization.** Equation (1.1) is one-way and applies to the same
   SCD/forest/orbit construction. Small physical initialization alone need
   not imply small \(\widehat\Phi_H\), and no pure multiplicative comparison
   with \(\widehat\Phi_H\) is asserted.
4. **Hall certificate.** Theorem 3.2 is a genuine universal lower bound, but
   its right side can vanish for diffuse one-level label measures. No
   positive universal nested deficiency is proved.
5. **Structural lower bounds.** The exact stationary-pair obstruction is
   conditional on one fixed pair frame. The BTK argument uses only radii
   \(d\le b\sqrt m<H\), so no assertion about the clipped boundary class is
   needed. Neither result is a lower bound for every SCD.
6. **Surgery distance.** The two-Lipschitz estimate yields a necessary
   linear distance from BTK; it does not say that every SCD at that distance
   has low toll or that arbitrary dense surgery is possible.
7. **Product rigidity.** Theorem 7.1 concerns labelled copies of the two
   standard phases over the same parent-chain box system. Its multicolor
   conclusion is structural; occurrences can still mix among equal
   structural phase types.
8. **Prescribed-lift metric.** The quantity \(s_d\) is relative to one
   prescribed parent forest and phase field; (7.9)--(7.10) then choose an
   optimal child forest. An arc counted by \(s_d\) may be a natural lift for
   another forest. Hence (7.10) is not a universal cross-lane or
   nonliftability theorem.
9. **Splice scope.** Proposition 8.1 excludes one cut when the two operated
   chains themselves are the desired rotor-neighbor pair. It does not
   exclude an operated output becoming adjacent to a third chain.
10. **Remaining lemma.** The contraction statement (9.1) is explicitly
    unproved. Its fixed-window parameter is essential: an unspecified
    \(A+o(1)\) cannot be iterated without summability and compact-uniform
    control.

After these attacks on scope and constants, the unconditional claims that
remain are exactly those listed in Section 10; none implies
\(\mathrm{RSCD}_A\) by itself.
