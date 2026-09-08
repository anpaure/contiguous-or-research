# Global MTF endpoint portals across SCD boxes

Date: 2026-07-25

## 0. Status and exact outcome

Let

\[
2m=3s,\qquad s\ \text{even},\qquad
W=\binom{2m}{m},\qquad H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\).  Split the coordinates into three \(s\)-sets, fix
arbitrary symmetric-chain decompositions in the three blocks, and use their
Cartesian products as the product-box partition.

This note proves four new facts.

1. **A literal fused global portal word exists.**  Cut an exact odd wreath
   factor into its \(W/(m+1)\) complementary geodesics and give every path
   its canonical radius-\(H\) adaptive-MTF lift.  Independent exact resets
   give one literal word of length
   \[
   \boxed{
   W+(2H+1)\frac{W}{m+1}=W+O_A(W/\sqrt m).}
   \tag{0.1}
   \]
   After one common coordinate relabelling, all but \(o(W)\) of its \(W\)
   state endpoints have their \(2H+1\) canonical flag occurrences in
   pairwise distinct product boxes.  Thus stateful arm fusion, with maximum
   Gaussian-band occurrence degree, is possible at \(o(W)\) reset cost.

2. **There is unconditional honest distinct-target sharing at depth one.**
   The same relabelled word has \(\Omega(W)\) right endpoints at which the
   middle target and the upper depth-one target are globally distinct masks
   in distinct boxes.  The upper targets are chosen from the audited
   dominant-box plateau family.  This supplies a literal linear amount of
   distinct-target sharing, although the word is not yet universal in the
   whole Gaussian band.

3. **PTAD upgrades occurrence portals to genuine unbounded-degree ledger
   portals.**  If the same MTF construction satisfies the trace condition
   in \(\mathrm{PTAD}_A\), or if one starts with any \(\mathrm{PTAD}_A\)
   witness, then after relabelling there are
   \[
   \boxed{P=\Theta_A(W/\sqrt m)}
   \tag{0.2}
   \]
   physical right endpoints carrying \(\Omega(W)\) genuine, globally
   distinct selected-target--box incidences.  Their average degree is
   \(\Theta_A(\sqrt m)\).  The relabelled central-band word still has length
   \(W+o(W)\).  This is an implication of PTAD, not a proof of PTAD.

4. **The packet and degree scales are exact.**  A max-plus amalgamation
   theorem below characterizes exactly when prescribed SCD-projected MTF
   states can share one physical reset packet.  The audited endpoint ledger
   forces \(\Omega(W/\sqrt s)\) physical portals even at maximum central-band
   degree, while an incidence-faithful packet has average surface
   \(\Omega(s)\) per product box.  A packet fusing \(B\)
   residual-consuming radius-\(H\) seams and attaining the universal lower
   bound \(2H+1\) must be active in every one of the \(B\) boxes at every
   packet letter.

The unconditional theorem settles portal existence and dynamic arm fusion,
but not deep canonical support.  The remaining gate is exactly the
support/trace term in \(\mathrm{PTAD}_A\).  No wreath synchronization is
inferred from the results below, and no fractional object is treated as a
literal word.

No web search or finite computation is used.

---

## 1. A deterministic maximum-degree portal through any middle owner

Write

\[
[3s]=X_1\sqcup X_2\sqcup X_3,
\qquad |X_i|=s,
\qquad m=3s/2.
\]

Every mask belongs to a unique product box.

### Theorem 1.1 — two-sided box-rainbow portal

Let \(T\in\binom{[3s]}m\), and suppose

\[
1\le H\le s/6.
\tag{1.1}
\]

There are distinct

\[
x_1,\ldots,x_H\in T,
\qquad
y_1,\ldots,y_H\notin T
\]

such that the \(2H+1\) masks

\[
L_q=T\setminus\{x_1,\ldots,x_q\},\quad 0\le q\le H,
\tag{1.2}
\]

and

\[
U_q=T\cup\{y_1,\ldots,y_q\},\quad 1\le q\le H,
\tag{1.3}
\]

lie in \(2H+1\) pairwise distinct product boxes.

Moreover, these masks are all suffix ORs ending at one common physical
position of a literal word of length \(2H+2\), and the terminal
last-occurrence state is a legal fresh canonical radius-\(H\) MTF state.

#### Proof

Choose coordinate blocks \(X_a,X_b\) satisfying

\[
|T\cap X_a|\ge s/2,
\qquad
|X_b\setminus T|\ge s/2.
\tag{1.4}
\]

They exist by averaging; they need not be distinct.

Suppose \(L_0,\ldots,L_{q-1}\) have been chosen in distinct boxes.  The
remaining deletions in \(T\cap X_a\) give

\[
|T\cap X_a|-(q-1)
\]

candidate lower neighbours.  These candidates lie in pairwise distinct
product boxes: their components outside \(X_a\) agree, while two different
equal-rank sets cannot lie in one factor chain in \(X_a\).  Only the \(q\)
boxes already visited are forbidden.  Since \(s/2\ge3H\),

\[
|T\cap X_a|-(q-1)>q
\]

for \(q\le H\).  One may therefore choose \(x_q\) greedily.

After the lower arm is complete, suppose \(U_1,\ldots,U_{q-1}\) have also
been chosen without a repeated box.  The unused additions in
\(X_b\setminus T\) give at least

\[
|X_b\setminus T|-(q-1)
\]

candidate upper neighbours, again in pairwise distinct boxes.  There are
only \(H+q\) previously visited boxes: the \(H+1\) lower masks and the
\(q-1\) earlier upper masks.  Condition (1.1) gives

\[
|X_b\setminus T|-(q-1)>H+q.
\]

Thus \(y_q\) can also be chosen greedily.

Put

\[
R=[3s]\setminus U_H
\]

and define the ordered partition

\[
\Pi=
\bigl(
L_H,\{x_H\},\ldots,\{x_1\},
\{y_1\},\ldots,\{y_H\},R
\bigr).
\tag{1.5}
\]

The first and last blocks both have size \(m-H\), and all other blocks are
singletons.  Its prefix unions are precisely

\[
L_H,L_{H-1},\ldots,L_0=T,U_1,\ldots,U_H.
\tag{1.6}
\]

Writing the blocks of \(\Pi\) in reverse order gives the literal word

\[
R,\{y_H\},\ldots,\{y_1\},
\{x_1\},\ldots,\{x_H\},L_H.
\tag{1.7}
\]

Every mask in (1.6) is the union of a suffix of (1.7) ending at its last
position.  Finally, (1.5) has exactly the canonical fresh form: the
\(x_i\) may be prescribed as the first \(H\) future departures and the
\(y_i\) as the initial upper singleton queue.  \(\square\)

The degree \(2H+1\) is optimal inside a \(2H+1\)-rank band because masks
sharing one oriented endpoint form a strict inclusion chain and therefore
contain at most one mask of each rank.

The theorem is local.  Independently choosing (1.5) at different middle
owners does not make the states one-update compatible.  For fresh canonical
states

\[
(A,\{z_1\},\ldots,\{z_{2H}\},R),
\qquad |A|=|R|=m-H\ge2,
\]

the audited one-update classification says that a genuine transition must
preserve the whole residual \(R\) and perform one delete/insert-front rotor
operation on the ordered singleton queue.  That rigid compatibility is why
the global chronology below is needed.

---

## 2. Literal fusion by the exact odd factor

### 2.1 The physical word

Use the audited exact odd wreath factor and cut it at its distinguished
coordinate.  This gives

\[
B=\frac{W}{m+1}
\tag{2.1}
\]

vertex-disjoint complementary geodesics

\[
T_0,T_1,\ldots,T_m
\tag{2.2}
\]

which partition \(\binom{[2m]}m\).  On every path, removed coordinates
never return and inserted coordinates are never removed.  Hence the path is
\(H\)-legal for every \(H<m/2\), and the audited adaptive-MTF theorem gives
one update per middle edge and a saturated canonical flag

\[
F_{v,-H}\subset F_{v,-H+1}\subset\cdots\subset F_{v,H}
\tag{2.3}
\]

at every middle state endpoint \(v\), where \(|F_{v,q}|=m+q\).

Independently reverse-initialize every path state.  A path with \(m+1\)
middle vertices has length

\[
(m+1)+(2H+1).
\]

Summing over (2.1) gives the exact length (0.1).  Every letter is nonempty,
and all witnesses supplied by (2.3) are literal intervals ending at their
state positions.

### 2.2 Same-box collision under one relabelling

For one state endpoint \(v\), let

\[
C_v(\sigma)
=\#\bigl\{\{q,q'\}:q<q',\ 
\sigma F_{v,q},\sigma F_{v,q'}
\text{ lie in one product box}\bigr\}.
\tag{2.4}
\]

Let \(C(\sigma)=\sum_v C_v(\sigma)\).

### Lemma 2.1 — flag collision estimate

For a uniform coordinate permutation \(\sigma\),

\[
\boxed{
\mathbb E C(\sigma)
\le W\varepsilon_{m,H},}
\tag{2.5}
\]

where

\[
\varepsilon_{m,H}
=\sum_{d=1}^{2H}(2H+1-d)
\frac{\binom{d+2}{2}}{\binom{m-H}{d}}
=O_A(H/m).
\tag{2.6}
\]

For all sufficiently large \(m\), depending on \(A\), one has
\(H\le m/8\) and may take

\[
\varepsilon_{m,H}\le8H/m.
\tag{2.7}
\]

#### Proof

Fix a nested flag pair \(S\subset T\) with rank gap \(d\).  Under a uniform
coordinate permutation it is a uniform nested pair of those two ranks.
Conditional on the upper mask, the lower mask is a uniform \(d\)-deletion.

Inside one three-chain product box, a \(d\)-step predecessor is determined
by the three nonnegative factor-chain drops whose sum is \(d\).  There are
at most \(\binom{d+2}{2}\) such weak compositions.  The upper flag has rank
at least \(m-H\).  Consequently

\[
\Pr(\sigma S,\sigma T\text{ are in one box})
\le
\frac{\binom{d+2}{2}}{\binom{m-H}{d}}.
\tag{2.8}
\]

There are \(2H+1-d\) flag pairs of gap \(d\) at one state.  This proves
(2.5)--(2.6) by linearity of expectation.

For (2.7), the \(d=1\) contribution is \(6H/(m-H)\).  The \(d=2\)
contribution is at most \(12H/\binom{m-H}{2}\), and for
\(3\le d\le2H=O_A(\sqrt m)\) the ratio of consecutive summands is uniformly
bounded away from one once \(m\) is large.  The remaining tail is
\(O_A(H/m^2)\).  Since \(H/m\to0\), (2.7) follows.  \(\square\)

### Theorem 2.2 — fused global occurrence portals

For every fixed \(A>0\), and all sufficiently large \(m\) with
\(2m=3s\), a single relabelling of the literal word in Section 2.1 has the
following properties:

1. its length is exactly (0.1);
2. all but \(o(W)\) of its \(W\) state endpoints have the \(2H+1\)
   canonical flag occurrences in pairwise distinct product boxes;
3. hence a set of \(\Theta(W/H)\) state endpoints already carries
   \(\Theta(W)\) box-rainbow flag occurrences, with degree \(2H+1\) at
   every selected endpoint.

#### Proof

By Lemma 2.1, some relabelling satisfies

\[
C(\sigma)=O_A(HW/m)=o(W).
\]

Every state endpoint whose flag repeats a product box contributes at least
one to \(C(\sigma)\).  Thus only \(o(W)\) state endpoints fail to be fully
box-rainbow.  Select any \(\Theta(W/H)\) of the remaining endpoints.
\(\square\)

The word in Theorem 2.2 is already middle-productive: all but the
\(o(W)\) reset excess positions belong to the chronology covering the
entire middle layer.  This is the fusion missing from isolated
reverse-difference portal blocks.

The word need not have distinct canonical masks at different endpoints.
Thus Theorem 2.2 is an occurrence theorem, not yet a deep-support theorem.

### 2.3 Honest distinct-target sharing at depth one

Use the audited dominant windows

\[
p,q\in[\sqrt s,1.1\sqrt s],
\qquad
r\in[3\sqrt s,3.1\sqrt s]
\tag{2.9}
\]

and select the full plateau of every such box, together with the local
middle layer in every other box.  Put

\[
\kappa_L=e^{-1/2}-e^{-121/200},
\qquad
\kappa_H=e^{-9/2}-e^{-961/200},
\tag{2.10}
\]

and

\[
\alpha=\frac{\sqrt3}{\pi}\kappa_L^2\kappa_H>0.
\tag{2.11}
\]

For all sufficiently large \(s\), at least \(\alpha W\) rank-\((m+1)\)
masks lie in the selected dominant plateaux.  Indeed, there are
\((\kappa_L^2\kappa_H+o(1))W_s^3\) boxes of the displayed orientation,
each plateau layer has at least \(s\) masks, and

\[
\frac{sW_s^3}{W}\longrightarrow\frac{2\sqrt3}{\pi}.
\tag{2.12}
\]

The odd factor has \(mB=N_1\) internal upper edge unions, and these masks
partition rank \(m+1\).  At every noninitial path state, take its middle
mask \(T\) and the incident upper flag \(U\supset T\).  All chosen middle
masks are distinct, all chosen \(U\)'s are distinct, and the two ranks are
different.

### Theorem 2.3 — a linear honest sharing subset

One relabelling in Theorem 2.2 may be chosen so that at least

\[
\boxed{\alpha W/4}
\tag{2.13}
\]

right endpoints simultaneously represent a globally distinct middle mask
and a globally distinct upper depth-one mask, the two masks lie in different
product boxes, and the upper mask belongs to a selected dominant plateau.
The same relabelling has only \(o(W)\) state endpoints with a repeated box
inside the full canonical flag.

#### Proof

Let \(G(\sigma)\) count the noninitial endpoints with the stated
middle/upper property.  A fixed upper mask is uniform in rank \(m+1\), so
its probability of landing in a dominant plateau is at least \(\alpha\).
Conditional on the upper mask, at most three of its \(m+1\) lower neighbours
lie in its product box.  Therefore

\[
\mathbb E G
\ge\left(\alpha-\frac3{m+1}\right)N_1
\ge\frac{\alpha W}{2}
\tag{2.14}
\]

for all sufficiently large \(m\).

By (2.7), \(\mathbb EC\le8HW/m\).  Put

\[
\lambda=\frac{\alpha m}{32H}.
\]

Then

\[
\mathbb E(G-\lambda C)\ge\alpha W/4.
\]

Choose a permutation attaining at least this expectation.  It satisfies
\(G\ge\alpha W/4\), and since \(G\le W\),

\[
C\le\frac{W}{\lambda}
=\frac{32H}{\alpha m}W=o(W).
\]

The global distinctness of the chosen targets was established before the
random relabelling and is preserved by it.  \(\square\)

Thus the fused word already realizes a linear amount of honest
selected-target sharing.  It does not yet cover every selected target, so
this statement is a capacity construction rather than an assertion that the
whole audited endpoint ledger has been completed.

---

## 3. PTAD makes the high degree genuine

Let a \(\mathrm{PTAD}_A\) witness have canonical signed-rank supports

\[
\mathcal S_q^-\subseteq\binom{[2m]}{m-q},
\qquad
\mathcal S_q^+\subseteq\binom{[2m]}{m+q},
\]

and hole counts

\[
M_q^-=N_q-|\mathcal S_q^-|,
\qquad
M_q^+=N_q-|\mathcal S_q^+|,
\qquad
N_q=\binom{2m}{m-q}.
\]

Its trace functional satisfies

\[
\Phi_Z(\mathcal H_H)=o(W).
\tag{3.1}
\]

### Lemma 3.1 — trace cost controls total raw holes

For every such witness,

\[
\boxed{
\sum_{q=1}^H(M_q^-+M_q^+)
\le2H\Phi_Z(\mathcal H_H).}
\tag{3.2}
\]

#### Proof

For one trace \(R\), let \(h_R\) be its total number of holes across the
\(2H\) signed ranks, and let

\[
\ell_R=\nu(2m-|Z|)+\mathbf1_{R\ne\varnothing}.
\]

At each individual rank the trace class contains at most \(\ell_R\) holes,
by the rank sandwich in the audited trace theorem.  Hence

\[
h_R\le2H\ell_R.
\]

Trivially \(h_R\le2Hh_R\).  Therefore

\[
h_R\le2H\min\{h_R,\ell_R\}.
\]

Sum over traces.  \(\square\)

Put

\[
h=\min\left\{H,\left\lfloor\frac{\sqrt s}{4}\right\rfloor\right\}.
\tag{3.3}
\]

For fixed \(A\), one has \(h=\Theta_A(\sqrt m)\) and \(h/H\) is bounded
below by a positive \(A\)-dependent constant.  Equations (3.1)--(3.2) give

\[
\sum_{q=1}^h(M_q^-+M_q^+)=o(hW).
\tag{3.4}
\]

Also, uniformly for \(q\le h\),

\[
N_q\ge c_AW
\tag{3.5}
\]

for a constant \(c_A>0\).

For every distinct supported mask in the shallow signed band, choose one of
its canonical state occurrences.  Include every middle mask at its unique
middle state.  By (3.4)--(3.5), the resulting representative family
\(\mathcal R\) consists of globally distinct masks and has size

\[
|\mathcal R|=\Theta_A(hW).
\tag{3.6}
\]

Every dominant box in (2.9) has plateau excess at least \(0.8\sqrt s\).
Thus all its masks of global rank \(m+q\), \(|q|\le h\), lie in its
plateau.  From here onward, “selected target family” means the audited
family restricted to these shallow ranks; no target outside the PTAD band
is being invoked.  Equation (2.12) implies that, at every such rank, at
least \(\alpha W\) masks belong to this restricted family.  Since the
whole rank layer has size at most \(W\), a uniformly relabelled
representative lands in the selected family with probability at least
\(\alpha\).

For a permutation \(\sigma\), let \(U(\sigma)\) be the number of selected
representatives after relabelling.  Let \(C_{\mathcal R}(\sigma)\) count
pairs of representatives assigned to the same state endpoint which land in
one product box.  Lemma 2.1 applies to every canonical state flag and gives

\[
\mathbb E U\ge\alpha|\mathcal R|=\Theta_A(hW),
\qquad
\mathbb E C_{\mathcal R}=O_A(HW/m)=o(W).
\tag{3.7}
\]

At one endpoint, if \(u_B\) selected representatives land in a box
\(B\), replacing their occurrence count by one endpoint--box incidence
loses

\[
(u_B-1)_+\le\binom{u_B}{2}.
\]

Therefore the number \(D(\sigma)\) of distinct representative
endpoint--box incidences satisfies

\[
D(\sigma)\ge U(\sigma)-C_{\mathcal R}(\sigma).
\tag{3.8}
\]

Taking expectations in (3.8) proves that some permutation has

\[
D(\sigma)\ge c'_AhW
\tag{3.9}
\]

for a constant \(c'_A>0\).

### Theorem 3.2 — PTAD-to-global-portal theorem

Assume \(\mathrm{PTAD}_A\) for one fixed \(A>0\), and restrict to
\(2m=3s\) with \(s\) even.  Relative to any fixed three-block SCD product
partition, one may relabel the PTAD witness so that:

1. its literal central-band word still has length \(W+o(W)\);
2. there is a set of
   \[
   P=\Theta_A(W/h)=\Theta_A(W/\sqrt m)
   \tag{3.10}
   \]
   canonical state right endpoints carrying \(\Omega_A(W)\) genuine
   selected-target--box incidences;
3. after subtracting the one baseline incidence per selected endpoint, the
   same set carries \(\Omega_A(W)\) right-endpoint sharing surplus;
4. its average selected-target box degree is \(\Theta_A(h)=
   \Theta_A(\sqrt m)\), and a positive proportion of the selected endpoints
   have degree \(\Omega_A(\sqrt m)\).

#### Proof

Use the permutation in (3.9), order the \(W\) state endpoints by their
representative box degree, and take the largest

\[
P=\lceil W/h\rceil.
\]

The average of the largest \(P\) degrees is at least the average of all
\(W\) degrees.  Hence their total degree is at least

\[
\frac PW D(\sigma)\ge c'_AW.
\]

For every representative, choose its canonical suffix interval as the
witness.  The representative masks are globally distinct, so these choices
do not compete.  The PTAD central word covers every remaining shallow
selected target; choose an arbitrary witness for each of those targets.
Consequently the degrees just counted are genuine subdegrees of one valid
audited endpoint ledger, not merely occurrence multiplicities.

Since \(P=o(W)\), subtracting one incidence per chosen endpoint leaves
\(\Omega_A(W)\) sharing surplus.  No endpoint can have degree greater than
\(2h+1\), so the total lower bound and this upper bound imply both the
average-degree claim and the positive-proportion claim.

Finally, relabelling preserves every MTF transition and exact bridge
distance.  Relabel \(Z\) simultaneously.  Trace classes are carried
bijectively to trace classes, so

\[
\Phi_{\sigma Z}(\sigma\mathcal H_H)=\Phi_Z(\mathcal H_H),
\]

and the portal excess is unchanged.  Relabelling the trace-repair word
therefore gives the asserted literal \(W+o(W)\) central-band word.  The
chosen canonical witnesses occur inside its principal MTF part and remain
valid after the repair word is appended.  \(\square\)

This theorem shows that cross-box endpoint capacity is automatic once PTAD
is achieved.  It does not prove the PTAD trace bound.  In particular, the
unconditional odd-factor occurrence theorem cannot be upgraded to
Theorem 3.2 without controlling its repeated deep masks.

---

## 4. Exact max-plus amalgamation of SCD-projected MTF packets

The preceding construction uses global Boolean MTF states.  A different
question is whether one physical packet can reset many prescribed local
product-box states simultaneously.  The product-box projection is not
ordinary coordinate restriction, so its exact compatibility law must be
stated separately.

For a factor SCD chain

\[
C_0\subset C_1\subset\cdots\subset C_p,
\qquad
C_t=C_0\cup\{e^C_1,\ldots,e^C_t\},
\tag{4.1}
\]

the audited projection is

\[
\pi_C(A)=\max\bigl(\{t:e^C_t\in A\}\cup\{0\}\bigr).
\tag{4.2}
\]

Identify height \(f\) with the prefix ideal

\[
I_C(f)=\{e^C_1,\ldots,e^C_f\}.
\]

Then \(A\mapsto I_C(\pi_C(A))\) is a union homomorphism.

Let \(X_1,\ldots,X_p\) be a physical packet, and define the last physical
occurrence time

\[
\tau(x)=\max\{j:x\in X_j\},
\]

with value zero if \(x\) does not occur.  Its induced recency profile on
the factor chain is

\[
\boxed{
\eta_C(t)=\max_{u\ge t}\tau(e^C_u).}
\tag{4.3}
\]

This depends only on the owner chain \(C\), not on its two partner chains
in a product box.

### Theorem 4.1 — forced-descent criterion

Prescribe a nonincreasing nonnegative integer profile

\[
\eta_C(1)\ge\eta_C(2)\ge\cdots\ge\eta_C(p_C)\ge0
\]

on every chain in an arbitrary selected family, and set
\(\eta_C(p_C+1)=0\).  There is one physical timestamp map \(\tau\) satisfying
(4.3) for every selected chain if and only if both conditions below hold.

1. Whenever
   \[
   \eta_C(t)>\eta_C(t+1),
   \]
   the coordinate \(e^C_t\) is forced to have timestamp \(\eta_C(t)\), and
   all demands forcing the same physical coordinate agree.
2. If a coordinate \(x\) is forced to value \(a(x)\), then at every
   occurrence \(x=e^D_u\) on every selected chain \(D\),
   \[
   a(x)\le\eta_D(u).
   \tag{4.4}
   \]

When the conditions hold, the canonical solution is

\[
\tau(x)=a(x)\quad\text{on forced coordinates},
\qquad
\tau(x)=0\quad\text{otherwise}.
\tag{4.5}
\]

#### Proof

The recurrence

\[
\eta_C(t)=\max\{\tau(e^C_t),\eta_C(t+1)\}
\tag{4.6}
\]

shows that every strict descent forces
\(\tau(e^C_t)=\eta_C(t)\).  Every occurrence \(x=e^D_u\) lies in the tail
defining \(\eta_D(u)\), giving (4.4).  This proves necessity.

For sufficiency, use (4.5).  Fix \(C,t\).  All forced timestamps in the
tail \(u\ge t\) are at most \(\eta_C(t)\), by (4.4) and monotonicity.  If
\(\eta_C(t)>0\), let \(r\ge t\) be the last index of its constant plateau.
Then \(r\) is a strict descent and

\[
\tau(e^C_r)=\eta_C(r)=\eta_C(t).
\]

Thus the tail maximum is exactly \(\eta_C(t)\).  The zero case is
immediate.  \(\square\)

The terminal local MTF state is obtained by grouping local prefix
coordinates with equal positive \(\eta\)-value in decreasing order and
then appending the source-state residual after deleting every touched local
coordinate.  Therefore Theorem 4.1, together with this deletion-tail
identity, is a necessary and sufficient simultaneous reset theorem.  A
literal packet is obtained by emitting the disjoint masks

\[
X_t=\{x:\tau(x)=t\}.
\tag{4.7}
\]

For prescribed numeric profiles, a common strictly increasing relabelling
of all positive values in both \(\eta\) and \(\tau\) preserves the induced
MTF states.  One may therefore delete unused levels and order-compress the
profiles and timestamps together before emitting (4.7).  For prescribed
target states, rather than prescribed numeric profiles, the shortest packet
length is the least number of distinct positive levels over all representing
profiles satisfying Theorem 4.1 and the deletion-tail identities.

### Corollary 4.2 — common one-letter frontier

Suppose box \(\mathcal B=(C_1,C_2,C_3)\) demands the projected first block
with factor cutoffs

\[
f_{\mathcal B,i}\in\{0,1,\ldots,p(C_i)\}.
\]

For every positive cutoff, the frontier coordinate

\[
e^{C_i}_{f_{\mathcal B,i}}
\]

is forced into a common physical update letter.  Let \(Q\) be the union of
all forced frontier coordinates.  Assume first that at least one cutoff is
positive, so \(Q\ne\varnothing\).  A common one-letter update exists exactly
when:

1. the local deletion-tail identity holds in every box; and
2. every \(x\in Q\), at every occurrence \(x=e^D_u\) in a selected
   box-factor \((\mathcal B',i')\) whose owner chain is \(D\), satisfies
   \[
   u\le f_{\mathcal B',i'},
   \tag{4.8}
   \]
   with a zero cutoff forbidding such an occurrence.

When (4.8) holds, the nonempty forced letter \(Q\) works.  Necessity follows because
an exact maximum \(f>0\) forces the unique increment \(e_f\), while any
forced coordinate above another cutoff would overshoot it.

If every cutoff is zero, then \(Q=\varnothing\).  In this exceptional case
a one-letter physical update exists exactly when the deletion-tail
identities reduce to the zero-allowed conditions
\(\Pi_{\mathcal B}=\Sigma_{\mathcal B}\) in every selected box and there is
a nonempty physical mask whose projection is zero in every selected box.
The empty mask itself is not a legal letter.

For a Cartesian packet

\[
\mathcal C_1\times\mathcal C_2\times\mathcal C_3
\]

whose common first block must have local rank

\[
\frac{p(C_1)+p(C_2)+p(C_3)}2-H,
\]

the cutoffs necessarily have the owner-factorized form

\[
\boxed{
f_i(C)=\frac{p(C)}2+c_i,
\qquad c_1+c_2+c_3=-H.}
\tag{4.9}
\]

Indeed, the projection in factor \(i\) depends only on its owner chain, and
subtracting the rank equations for two choices of one factor makes
\(f_i(C)-p(C)/2\) constant.  Conditions (4.8)--(4.9) are an exact labelled
cut-synchronization requirement.

This conclusion is scoped to the declared common SCD-projected MTF packet.
It is not a necessity for an arbitrary literal OR word, is not equivalent
to MWB, and does not turn unlabelled overload into labelled common-owner
synchronization.

---

## 5. Exact endpoint Pareto frontier

Use all three orientations of the dominant windows (2.9).  Let \(L_s\) be
the number of factor chains with height in the low window and \(K_s\) the
number in the high window.  There are exactly

\[
3L_s^2K_s
\tag{5.1}
\]

window-dominant boxes.  For such a box put

\[
\Delta_{\mathcal B}=r-p-q,
\qquad
w_{\mathcal B}=(p+1)(q+1).
\]

The window inequalities give

\[
0.8\sqrt s\le\Delta_{\mathcal B}\le1.1\sqrt s,
\qquad
\frac{\Delta_{\mathcal B}}r\ge\frac4{15},
\qquad
w_{\mathcal B}\ge s.
\tag{5.2}
\]

Define the exact integer endpoint demand

\[
G_s=
\sum_{\mathcal B\ \mathrm{window\text{-}dominant}}
\left\lceil
\frac{w_{\mathcal B}\Delta_{\mathcal B}}{r_{\mathcal B}}
\right\rceil.
\tag{5.3}
\]

Then

\[
G_s\ge\frac45sL_s^2K_s
=\left(\frac45\kappa_L^2\kappa_H+o(1)\right)sW_s^3.
\tag{5.4}
\]

Select every plateau target in these boxes and only the local middle layer
in every other box.  All selected targets lie in at most

\[
\Delta_*+1,
\qquad
\Delta_*:=\max_{\mathcal B}\Delta_{\mathcal B}\le1.1\sqrt s,
\tag{5.5}
\]

global ranks.

### Theorem 5.1 — exact portal number/degree inequality

Let a word of length \(n=W+E\) cover the selected targets, and choose one
witness interval for each target.  If \(\ell_j,r_j\) are the selected-box
degrees of physical position \(j\) as a left and right endpoint, then

\[
\boxed{
\mathcal C_\partial
:=\sum_j\bigl((\ell_j-1)_++(r_j-1)_+\bigr)
\ge G_s-2E.}
\tag{5.6}
\]

Moreover,

\[
\boxed{\ell_j,r_j\le\Delta_*+1.}
\tag{5.7}
\]

If \(P_s\) physical positions have \(\ell_j\ge2\) or \(r_j\ge2\), then

\[
\boxed{
P_s\ge
\left\lceil\frac{(G_s-2E)_+}{2\Delta_*}\right\rceil.}
\tag{5.8}
\]

#### Proof

For every dominant box, the audited plateau endpoint theorem gives

\[
C_L+C_R\ge2w_{\mathcal B}
+\left\lceil
\frac{w_{\mathcal B}\Delta_{\mathcal B}}{r_{\mathcal B}}
\right\rceil.
\]

Every other box contributes at least \(2w_{\mathcal B}\).  Sum over boxes,
use \(\sum w_{\mathcal B}=W\), and double-count endpoint--box incidences.
Since

\[
\sum_j\ell_j+\sum_jr_j\le2(W+E)+\mathcal C_\partial,
\]

(5.6) follows.

At a fixed oriented endpoint, represented targets form a strict inclusion
chain.  Distinct boxes contain distinct targets, and such a chain contains
at most one target in each selected rank.  This proves (5.7).  A physical
position contributes at most \(2\Delta_*\) excess incidences, proving
(5.8).  \(\square\)

For \(E=o(W)\), (5.4), (5.8), and

\[
\frac{sW_s^3}{W}\longrightarrow\frac{2\sqrt3}{\pi}
\]

give the explicit lower bound

\[
\boxed{
P_s\ge
\left(
\frac{8\sqrt3}{11\pi}\kappa_L^2\kappa_H-o(1)
\right)\frac{W}{\sqrt s}.}
\tag{5.9}
\]

Thus Theorem 3.2 attains the correct order of physical portal count and
degree.

For a designated portal set \(S\), \(|S|=P\), with directional degree at
most \(D\), let \(R_{\mathrm{off}}\) be all endpoint-sharing surplus outside
\(S\).  Then (5.6) gives

\[
\boxed{2P(D-1)+R_{\mathrm{off}}\ge G_s-2E.}
\tag{5.10}
\]

If \(S\) consists only of right-endpoint MTF portals, put

\[
R_{\mathrm{MTF}}
=\sum_j(\ell_j-1)_+
+\sum_{j\notin S}(r_j-1)_+,
\qquad
D_R=\max_{j\in S}r_j.
\]

Thus all left sharing and all off-portal right sharing are charged to
leakage.  The exact one-sided form is

\[
\boxed{P(D_R-1)+R_{\mathrm{MTF}}\ge G_s-2E.}
\tag{5.11}
\]

Hence negligible leakage and \(P=\Theta(W/\sqrt s)\) force
\(D_R=\Theta(\sqrt s)\).

There is a second notion of packet size.  Let \(Q\) be the number of signed
shared endpoint slots \((j,L)\) or \((j,R)\), and let \(I^\pm\) be their
total box incidence.  Exactly

\[
I^\pm=\mathcal C_\partial+Q.
\tag{5.12}
\]

If every product box participates in at most \(u_s\) signed portal slots,
then \(I^\pm\le u_sW_s^3\).  Equations (5.4), (5.6), and (5.12) imply, for
\(E=o(W)\),

\[
\boxed{
u_s\ge
\left(\frac45\kappa_L^2\kappa_H-o(1)\right)s.}
\tag{5.13}
\]

Thus high degree can reduce the number of distinct physical portal
positions to the Gaussian scale, but it cannot reduce the
incidence-faithful average packet surface below \(\Theta(s)\) per box.

---

## 6. Minimum reset-packet length and activity degree

Let one physical packet \(X_1,\ldots,X_p\) be projected into a family of
local boxes.  For box \(b\), let \(a_b\) be the number of nonzero projected
letters after zero projections are deleted.  For physical letter \(j\), let

\[
d_j=\#\{b:X_j\text{ has nonzero projection in }b\}.
\]

Suppose the packet must bridge an already realized local state
\(\Sigma_b\) to a prescribed exact local state \(\Pi_b\), and let

\[
r_b=d^+_{\mathrm{MTF}}(\Sigma_b,\Pi_b)
\]

be the audited nonempty bridge distance.  Boxes declared inactive with
\(\Sigma_b=\Pi_b\) use zero-allowed distance zero instead.

### Theorem 6.1 — packet activity-distance ledger

For every active family,

\[
\boxed{
\sum_{j=1}^p d_j
=\sum_ba_b
\ge\sum_br_b.}
\tag{6.1}
\]

Consequently,

\[
\boxed{
p\ge\max_br_b,
\qquad
\max_jd_j\ge
\left\lceil\frac{\sum_br_b}{p}\right\rceil.}
\tag{6.2}
\]

#### Proof

The equality in (6.1) double-counts nonzero physical-letter--box
projections.  After zero images are deleted, box \(b\) sees a nonempty local
bridge of length \(a_b\), so \(a_b\ge r_b\).  The two inequalities in
(6.2) follow.  \(\square\)

If \(B\) active boxes all have \(r_b\ge r\) and \(p=r+e\), then

\[
\boxed{
\sum_{j=1}^p(B-d_j)\le Be.}
\tag{6.3}
\]

Thus, for every \(0<\varepsilon\le1\),

\[
\boxed{
\#\{j:d_j<(1-\varepsilon)B\}\le e/\varepsilon.}
\tag{6.4}
\]

For every active product box \(b=(C_{b,1},C_{b,2},C_{b,3})\), define its
local Boolean middle parameter by

\[
2m_b=p(C_{b,1})+p(C_{b,2})+p(C_{b,3}).
\]

(The sum is even in the present even-block setting.)  Assume

\[
m_b-H\ge2,
\]

that its terminal canonical radius-\(H\) state is residual-consuming, and
that its target is a fresh canonical radius-\(H\) state.  The audited
depletion theorem then gives

\[
r_b\ge2H+1
\tag{6.5}
\]

for every bridge to a fresh canonical state.  Therefore:

* a packet fusing \(B\) such seams has length at least \(2H+1\);
* if its length is exactly \(2H+1\), every one of its letters has activity
  degree exactly \(B\);
* if its length is \(2H+1+e\), all but at most \(e/\varepsilon\) letters
  have degree at least \((1-\varepsilon)B\).

This is an exact universal lower-bound/equality theorem for packet size and
portal degree.  It does not assert that a compatible packet of length
\(2H+1\) always exists; incompatibility may force a longer shortest packet.
It concerns letter--box activity of exact local resets and is distinct from
the endpoint-box degree in Theorem 5.1.

---

## 7. Audit and remaining theorem

The proof uses the following imported audited facts.

1. The exact odd factor partitions the middle layer into
   \(W/(m+1)\) complementary geodesics of \(m+1\) vertices.
2. Every such path has the canonical one-update radius-\(H\) MTF lift, with
   exact independent-reset cost \(2H+1\) beyond its number of middle
   vertices.
3. Its internal upper depth-one colours partition rank \(m+1\).
4. The translated product-box projection is a join homomorphism, and the
   plateau endpoint inequality survives arbitrary cross-box witnesses.
5. The exact bridge metric and residual-depletion bound give (6.5).

The vulnerable logical points are as follows.

* A coordinate relabelling is common to the entire word.  Independence is
  never assumed; all collision bounds use only linearity of expectation.
* Translation by factor-chain bottoms does not affect the weak-composition
  bound: a triple of factor drops determines at most one predecessor in a
  fixed product box.
* Theorem 2.2 counts canonical occurrences.  It is not silently converted
  into distinct global support.  Theorem 2.3 uses globally unique
  depth-one masks, and Theorem 3.2 explicitly selects one occurrence per
  distinct supported mask before counting.
* The trace implication (3.2) is aggregate.  It does not assert raw
  \(o(W)\) defect summed over Gaussian ranks; it gives the correctly scaled
  \(o(HW)\) bound needed for \(\Theta(HW)\) portal incidence.
* The SCD max-plus theorem uses prefix closure of the range-maximum
  projection, not ordinary coordinate restriction.
* The common-owner conclusion (4.9) is architecture-scoped labelled
  synchronization.  It is strictly stronger than unlabelled overload and
  is not promoted to a necessary condition for arbitrary OR words.
* Endpoint degree, projected-letter activity degree, and repeated
  canonical occurrence degree are different quantities and are never
  added together.

The literal global mechanism is therefore no longer missing.  The exact
remaining positive theorem is the support side:

> Construct one fused global adaptive-MTF chronology with
> \(\mathfrak P_H=o(W)\) and
> \(\Phi_Z(\mathcal H_H)=o(W)\) for every fixed \(A\).

The odd-factor chronology proves the first condition and the global portal
theorems above.  It does not prove the second.  If the second is supplied,
Theorem 3.2 makes the required high-degree SCD endpoint sharing literal,
integral, and scale-sharp inside the same exact word.
