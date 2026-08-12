# Sixth-wave AB: a positive-density exact schedule of distinct MSW packet bridges

Date: 2026-07-25

Status: theorem-level mathematical report. Every assertion labelled **Theorem**,
**Lemma**, **Proposition**, or **Corollary** is proved below from the frozen logic
and the explicitly identified, previously audited MSW component and four-arm
formulas. Every intermediate factor in the positive construction is an integral
exact middle wreath factor. There is no finite search, computational experiment,
signed-factor surrogate, or web input.

---

## 0. Verdict

The one-fresh-cell theorem from
MATH_ATTACK_AB5_AFR_OVERLAY_FRAGMENTATION_20260725.md extends to a
positive-density schedule of genuinely distinct fresh coordinate bridges.

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
B=\operatorname{Cat}_m=\frac Wn,\qquad
H=H_A=\lceil A\sqrt m\rceil .
\]

For every fixed \(A>0\), and all sufficiently large \(m\), there is an exact
factor \(F^\sharp\) in a canonical MSW heterogeneous packet cube and a sequence

\[
\tau_s=(2s+2\ \ 2s+3),
\qquad 2\le s\le m-H-2,
\tag{0.1}
\]

with the following properties.

1. The sequence contains \(L=m-H-3\) pairwise distinct, vertex-disjoint
   coordinate edges. Starting from the edgeless coordinate forest, every
   \(\tau_s\) is a genuinely fresh forest bridge, and

   \[
   \frac{L}{n-1}\longrightarrow\frac12.
   \tag{0.2}
   \]

2. Bridge \(\tau_s\) carries

   \[
   k_s=\operatorname{Cat}_{m-s-2}
   \tag{0.3}
   \]

   pairwise disjoint genuine size-two MSW components. Packet owners and their
   middle-root supports never recur at another bridge. The reserved carrier
   contains more than \(B/128\) distinct owner rows, hence more than \(W/128\)
   distinct middle roots.

3. Process the bridges in increasing \(s\). At each bridge replace its coherent
   packet side by a balanced-half signing. With a backward choice of the initial
   coherent pile orientations, every stage has unconditional expected gain

   \[
   \boxed{
   \mathbb E[
   \mathcal Q_H(F_{s-1})-\mathcal Q_H(F_s)]
   >7H\operatorname{Cat}_{m-s-2}.
   }
   \tag{0.4}
   \]

   Consequently

   \[
   \boxed{
   \mathbb E[
   \mathcal Q_H(F^\sharp)-\mathcal Q_H(F_{\rm final})]
   >\frac7{256}HB.
   }
   \tag{0.5}
   \]

   Some deterministic exact path attains the total bound.

4. Every macro-stage is realized by
   \(\lfloor k_s/2\rfloor\) or \(\lceil k_s/2\rceil\) sequential component
   switches, freshly recomputed after every microstep. Individual microsteps,
   and even individual realized macro-stages, are not claimed to be downhill;
   (0.4) is an unconditional stage expectation.

5. For every realized current state, stage gain is bounded above by best fresh
   cell gain and elementary pair-orbit release. Hence

   \[
   \mathbb E\Gamma_{\tau_s}^*,\quad
   \mathbb E\mathcal R_{\tau_s}
   >7H\operatorname{Cat}_{m-s-2}.
   \tag{0.6}
   \]

6. An annealed variant, sampling the initial coherent pile orientations fairly,
   exposes genuine later subgroup-profile release on every odd bridge:

   \[
   \boxed{
   \mathbb E\Delta_s^Q
   >\frac92H\operatorname{Cat}_{m-s-2}
   \qquad(s\ {\rm odd}).
   }
   \tag{0.7}
   \]

   Summed over the odd stages,

   \[
   \boxed{
   \sum_{s\ {\rm odd}}\mathbb E\Delta_s^Q
   >\frac9{2048}HB.
   }
   \tag{0.8}
   \]

This proves a positive-density no-recycling schedule, not merely a second isolated
cell.

It still does not prove \(AFR_A\). The later gain and subgroup-release estimates
are two lower bounds; there is no upper bound on \(\Delta_s^Q\), hence no fixed
capture ratio. Moreover, all native packet bridges form a coordinate matching.
Even the complete native matching supplies only \(m-1\) of the \(2m\) edges of a
coordinate spanning tree.

---

## 1. Exact affine normalization

At depth \(q\), put

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q},\qquad c_q=\lfloor\lambda_q\rfloor.
\]

For an exact factor \(F\), let \(\mu_q^F\) be its rank-\(r_q\) cyclic-interval
load vector. The fixed-window energy is

\[
\mathcal Q_H(F)=
\sum_{q=1}^H\frac1{c_q}
\sum_S(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
\tag{1.1}
\]

Use

\[
\|x\|_H^2=\sum_{q=1}^H\frac{\|x_q\|_2^2}{c_q}.
\tag{1.2}
\]

Every exact factor has total load \(W\) at every depth, so

\[
\mathcal Q_H(F)=\|\mu^F\|_H^2+C_{m,H}
\tag{1.3}
\]

for a factor-independent constant \(C_{m,H}\).

Suppose an exact factor contains pairwise owner-disjoint component packets

\[
\{(\tau_t,K_{t,i}):1\le t\le T,\ 1\le i\le k_t\}.
\]

Let \(a_{t,i}\) and \(\tau_ta_{t,i}\) be the two packet contributions and set

\[
d_{t,i}=a_{t,i}-\tau_ta_{t,i},
\quad
D_t=\sum_i d_{t,i},
\quad
V_t=\sum_i\|d_{t,i}\|_H^2,
\quad
\Lambda_t=\|D_t\|_H^2-V_t.
\tag{1.4}
\]

If sign \(+1\) chooses \(a_{t,i}\), every heterogeneous cube vertex has

\[
\mu(F_\varepsilon)
=\bar\mu+\frac12\sum_{t,i}\varepsilon_{t,i}d_{t,i}.
\tag{1.5}
\]

Putting \(E=2\bar\mu\), (1.3)--(1.5) give

\[
\boxed{
\mathcal Q_H(F_\varepsilon)
=C_{m,H}
+\frac14\left\|
E+\sum_{t,i}\varepsilon_{t,i}d_{t,i}
\right\|_H^2.
}
\tag{1.6}
\]

The factors \(1/2\) and \(1/4\) are essential. Pairwise owner-disjoint packets
have disjoint middle-root supports; either side partitions its invariant support.
Thus every vertex of (1.5) is an integral exact factor.

---

## 2. The row-disjoint native schedule

Let \(F_m^{\rm MSW}\) be the canonical MSW factor. For \(s\ge2\), define

\[
P_s=1^s0^s\in\mathcal D_s,\qquad
M_s=m-s-2,\qquad
\tau_s=(2s+2\ \ 2s+3),
\tag{2.1}
\]

\[
J_s=
\{\{P_s1100R,\ P_s1010R\}:R\in\mathcal D_{M_s}\}.
\tag{2.2}
\]

Every member of \(J_s\) is an audited genuine size-two component of the
\(\tau_s\)-overlay.

### Theorem 2.1 (positive-density zero-recycling packet matching)

Assume \(H\le m-4\), and put

\[
\mathcal S=\{2,3,\ldots,m-H-2\}.
\tag{2.3}
\]

Then:

1. all owner rows in \(J_s\), \(s\in\mathcal S\), are pairwise distinct;
2. their middle-root packets are pairwise disjoint;
3. every choice of packet sides is an integral exact factor;
4. at every heterogeneous cube vertex, each packet, including one currently on
   its translated side, is exactly a component of its freshly recomputed
   \(\tau_s\)-overlay;
5. the \(\tau_s\) are pairwise vertex-disjoint and genuinely fresh in
   increasing-\(s\) order;
6. the bridge and packet counts are

   \[
   L=m-H-3,
   \qquad
   K=\sum_{s\in\mathcal S}|J_s|
   =\sum_{r=H}^{m-4}C_r,
   \quad C_r:=\operatorname{Cat}_r.
   \tag{2.4}
   \]

The owner carrier has size \(2K\), with

\[
\boxed{
2K>2C_{m-4}>\frac B{128}.
}
\tag{2.5}
\]

Its middle-root carrier has size \(2nK>W/128\).

#### Proof

Every endpoint word in \(J_s\) has initial run of ones exactly \(s\), since
\(P_s\) begins with \(s\) ones and its next letter is zero. Distinct \(s\) give
distinct rows. At fixed \(s\), the four-letter block distinguishes the two
endpoints and \(R\) recovers the packet.

Distinct exact-factor rows own disjoint root blocks. Each packet support \(U\) is
\(\tau_s\)-invariant and is partitioned by either \(K\) or \(\tau_sK\).
This proves exactness of all side choices.

At any cube vertex, restrict the current factor and its \(\tau_s\)-translate to
\(U\). The two sides are still \(K,\tau_sK\), possibly exchanged, and the
internal graph is the original connected component. Since \(\tau_sU=U\), no
overlay edge enters or leaves \(U\). Other switches act on disjoint supports.
Thus the present side is exactly one freshly recomputed component.

The edge \(\tau_s\) uses \(\{2s+2,2s+3\}\), while \(\tau_{s+1}\) uses
\(\{2s+4,2s+5\}\). Hence each new edge joins two still-isolated coordinate
vertices.

Equation (2.4) is immediate. Successive Catalan ratios are below four, so

\[
B=C_m<4^4C_{m-4},
\]

which proves (2.5). Multiplication by \(n\) proves the root claim. \(\square\)

For fixed \(A\),

\[
\frac{L}{n-1}=\frac{m-H-3}{2m}\longrightarrow\frac12.
\tag{2.6}
\]

If \(H\le m/2\) and \(m\ge12\), then

\[
L\ge\frac m4=\frac{n-1}{8}.
\tag{2.7}
\]

---

## 3. The shifted Catalan pile

For a Dyck word \(W\), split its flip permutation into lists

\[
\rho(W)=(a_0,b_0,\ldots),\qquad
\mathsf A(W)=(a_i),\quad\mathsf B(W)=(b_i).
\tag{3.1}
\]

For packet \((s,P_s,R)\), the exact four-arm lists are

\[
\mathsf E_{s,R}
=(2s+4+\mathsf A(R),\ n,\ \mathsf B(P_s)),
\tag{3.2}
\]

\[
\mathsf O_{s,R}
=(2s+4+\mathsf B(R),\ \mathsf A(P_s)).
\tag{3.3}
\]

Orient packet effects consistently and put

\[
D_s=\sum_{R\in\mathcal D_{M_s}}d_{s,R}.
\tag{3.4}
\]

### Lemma 3.1 (shifted pile lower bound)

For \(1\le q\le M_s\),

\[
\boxed{
\|D_{s,q}\|_2^2\ge2C_{M_s-q}C_q^2.
}
\tag{3.5}
\]

#### Proof

Restrict to

\[
R=UV,\qquad U\in\mathcal D_q,\quad
V\in\mathcal D_{M_s-q}.
\]

Concatenation gives

\[
\mathsf A(R)=
\mathsf A(U)\mathbin\Vert(2q+\mathsf A(V)).
\tag{3.6}
\]

At depth \(q\), the positive \(\mathsf E\)-suffix arm deletes the first \(q\)
entries of \(\mathsf E_{s,R}\), leaving the core

\[
\mathcal C_{s,V}
=(2s+4+2q+\mathsf A(V))
\cup\{n\}\cup\mathsf B(P_s),
\tag{3.7}
\]

independent of \(U\). All \(C_q\) choices of \(U\) contribute with one
orientation.

If \(q\le s\), mark a coordinate among the last \(q\) entries of
\(\mathsf B(P_s)\). The positive core contains it; the negative
\(\mathsf E\)-prefix deletes it; and both \(\mathsf O\)-arms use
\(\mathsf A(P_s)\), disjoint from \(\mathsf B(P_s)\).

If \(q>s\), mark \(n\). The last \(q\) entries of \(\mathsf E_{s,R}\)
contain all \(s\) entries of \(\mathsf B(P_s)\) and then \(n\), so the
negative \(\mathsf E\)-prefix omits \(n\). The \(\mathsf O\)-arms never
contain \(n\).

Thus no negative arm cancels the private dipole. Distinct \(V\)'s have distinct
sets \(\mathsf A(V)\), hence give distinct target pairs. There are
\(C_{M_s-q}\) pairs, each with coefficient magnitude at least \(C_q\) and
squared dipole norm two. \(\square\)

The \(+2q\) shift in (3.7) is essential. Marking only \(n\) fails when
\(s\ge q\).

### 3.1 Coherence constants

Fix \(A>0\), define

\[
L_A=\exp(2(A+1)(A+2)),
\tag{3.8}
\]

and choose \(m_A^{(6)}\) so that for every \(m\ge m_A^{(6)}\),

\[
H\ge5,\qquad H\le\frac m2,\qquad m\ge12,\qquad
4^H\ge288L_AH^5.
\tag{3.9}
\]

As in AB5,

\[
\lambda_H
=\prod_{j=0}^{H-1}\left(1+\frac{2+2j}{m-j}\right)
\le L_A,
\quad c_H\le L_A,
\tag{3.10}
\]

\[
C_H\ge\frac{4^H}{(H+1)(2H+1)}
\ge\frac{4^H}{4H^2}.
\tag{3.11}
\]

Every packet has depth-one squared norm four and squared norm eight at depths
\(2,\ldots,H\). Therefore, with \(k_s=C_{M_s}\),

\[
\boxed{
V_s=
k_s\left(\frac4{c_1}+8\sum_{q=2}^H\frac1{c_q}\right)
\le(8H-4)k_s.
}
\tag{3.12}
\]

### Theorem 3.2 (uniform positive internal coherence)

For every \(s\in\mathcal S\),

\[
\boxed{
\Lambda_s:=\|D_s\|_H^2-V_s
>(28H+4)k_s>28Hk_s.
}
\tag{3.13}
\]

#### Proof

Since \(M_s\ge H\),

\[
C_{M_s-H}>\frac{C_{M_s}}{4^H}=\frac{k_s}{4^H}.
\tag{3.14}
\]

Lemma 3.1 at \(q=H\) and (3.10)--(3.11) give

\[
\|D_s\|_H^2
\ge\frac{2C_{M_s-H}C_H^2}{c_H}
>\frac{k_s4^H}{8L_AH^4}
\ge36Hk_s.
\tag{3.15}
\]

Subtract (3.12). \(\square\)

---

## 4. Exact multiblock resampling

For \(k_t\ge2\), define

\[
\kappa_t=
\begin{cases}
k_t-1,&k_t\text{ even},\\
k_t,&k_t\text{ odd}.
\end{cases}
\tag{4.1}
\]

The balanced law has equally many signs of each kind if \(k_t\) is even. If
\(k_t\) is odd, append one zero dummy vector and balance the \(k_t+1\) signs.

### Theorem 4.1 (backward coherent endpoints, forward balanced resampling)

Consider a heterogeneous exact packet cube grouped into ordered blocks
\(J_1,\ldots,J_T\), with \(\Lambda_t\ge0\). There is a choice of one initial
common sign \(\sigma_t\) for every block such that, when the balanced block
resamplings are mutually independent, forward resampling satisfies

\[
\boxed{
\mathbb EG_t
=\frac14\left(1+\frac1{\kappa_t}\right)\Lambda_t
+\frac12\left|
\left\langle D_t,E+\sum_{u>t}\sigma_uD_u\right\rangle_H
\right|
}
\tag{4.2}
\]

at every stage. Hence

\[
\boxed{
\mathbb EG_t\ge
\frac14\left(1+\frac1{\kappa_t}\right)\Lambda_t
\ge\frac{\Lambda_t}{4}.
}
\tag{4.3}
\]

Every stage toggles \(\lfloor k_t/2\rfloor\) or
\(\lceil k_t/2\rceil\) freshly recomputed components. A deterministic choice of
balanced outcomes has total gain at least

\[
\boxed{
\frac14\sum_t\left(1+\frac1{\kappa_t}\right)\Lambda_t.
}
\tag{4.4}
\]

#### Proof

Choose coherent signs backward. Once \(\sigma_u\), \(u>t\), are fixed, put

\[
B_t=E+\sum_{u>t}\sigma_uD_u
\]

and choose \(\sigma_t\) so that

\[
\sigma_t\langle D_t,B_t\rangle_H
=|\langle D_t,B_t\rangle_H|.
\tag{4.5}
\]

For the balanced block variable

\[
X_t=\sum_i\varepsilon_{t,i}d_{t,i},
\]

one has

\[
\mathbb EX_t=0,\qquad
\mathbb E(\varepsilon_{t,i}\varepsilon_{t,j})
=-\frac1{\kappa_t},
\]

and therefore

\[
\boxed{
\mathbb E\|X_t\|_H^2=V_t-\frac{\Lambda_t}{\kappa_t}.
}
\tag{4.6}
\]

Before and after stage \(t\), the affine residuals in (1.6) are

\[
Y_{t-1}=B_t+\sum_{u<t}X_u+\sigma_tD_t,
\qquad
Y_t=B_t+\sum_{u<t}X_u+X_t.
\]

Earlier block variables are independent and centered, so their variance terms
cancel. Equations (1.6) and (4.6) give

\[
\mathbb EG_t
=\frac14\left(
\|D_t\|_H^2-V_t+\frac{\Lambda_t}{\kappa_t}
+2\sigma_t\langle D_t,B_t\rangle_H
\right),
\]

which is (4.2).

The product law has finite support. Reveal block outcomes successively and choose
at each reveal an outcome whose conditional expected final total is at least the
current average. The last reveal gives (4.4). Exactness follows from Theorem 2.1.
\(\square\)

Theorem 4.1 is an exact packet-cube statement, not a coordinate-forest statement:
distinct transposition labels alone need not be forest-fresh. In its application
below, freshness follows separately from the vertex-disjoint native edges proved
in Theorem 2.1.

For every realized history, the stage child is in the freshly recomputed
\(\tau_t\)-cell. Pointwise,

\[
G_t\le\Gamma_{\tau_t}^*(F_{t-1})
\le\mathcal R_{\tau_t}(F_{t-1}).
\tag{4.7}
\]

Thus (4.2) also lower-bounds the expected best cell gain and expected elementary
release.

The estimate is unconditional, not predictable. Conditional on a realized past,

\[
\mathbb E(G_t\mid\mathcal F_{t-1})
=\frac14\left[
\left(1+\frac1{\kappa_t}\right)\Lambda_t
+2\sigma_t\left\langle
D_t,B_t+\sum_{u<t}X_u
\right\rangle_H
\right],
\tag{4.8}
\]

whose last term may be negative. For example, in one dimension take two
three-vector blocks with \(d_{1,i}=2\), \(d_{2,i}=1\), and \(E=0\).
Then \(\Lambda_1=24,\Lambda_2=6\), but on the balanced history
\(X_1=-2\), the second conditional expected gain is \(-1\), although its
unconditional expectation is \(2\).

---

## 5. The fixed-endpoint distinct-bridge theorem

Order \(\mathcal S\) increasingly and apply Theorem 4.1.
Set \(F_1=F^\sharp\), and for \(s\in\mathcal S\) let \(F_s\) be the exact
endpoint after processing bridge \(\tau_s\). Thus \(F_{s-1}\) is the state
immediately before stage \(s\).

### Theorem 5.1 (positive-density exact schedule)

For every fixed \(A>0\) and \(m\ge m_A^{(6)}\), some exact coherent endpoint
\(F^\sharp\) of the heterogeneous MSW packet cube satisfies

\[
\boxed{
\mathbb E[
\mathcal Q_H(F_{s-1})-\mathcal Q_H(F_s)]
>7HC_{m-s-2}
}
\tag{5.1}
\]

at every distinct bridge stage, and

\[
\boxed{
\mathbb E[
\mathcal Q_H(F^\sharp)-\mathcal Q_H(F_{\rm final})]
>7H\sum_{r=H}^{m-4}C_r
>\frac7{256}HB.
}
\tag{5.2}
\]

Some deterministic exact path attains the total bound.

#### Proof

Theorems 3.2 and 4.1 give

\[
\mathbb EG_s>\frac{\Lambda_s}{4}>7Hk_s.
\]

Sum over \(s\), and use

\[
k_2=C_{m-4}>\frac B{4^4}=\frac B{256}.
\]

Deterministic extraction is (4.4). \(\square\)

Every stage uses at least one packet because \(k_s\ge C_H\). The first stage
alone toggles at least

\[
\frac{C_{m-4}-1}{2}>\frac B{512}-\frac12.
\tag{5.3}
\]

After enlarging \(m_A^{(6)}\) so that \(B>512\), the path contains more than
\(B/1024\) microsteps and more than \(B/512\) distinct toggled owner rows.
No owner is used at two bridges.

At the first bridge the coordinate group is trivial, so

\[
\Delta_2^Q=\mathcal R_{\tau_2}
>7HC_{m-4}>\frac7{256}HB.
\tag{5.4}
\]

For every later bridge,

\[
\boxed{
\mathbb E\Gamma_{\tau_s}^*,\quad
\mathbb E\mathcal R_{\tau_s}
>7HC_{m-s-2}.
}
\tag{5.5}
\]

Theorem 5.1 alone gives no comparison with later subgroup release
\(\Delta_s^Q\).

---

## 6. Annealed later subgroup release

Sample all initial coherent signs \(\delta_s\) independently and fairly, choose
that random exact cube endpoint \(F_1=F(\delta)\), and then process blocks
forward by independent balanced laws, with \(F_s\) again denoting the endpoint
after stage \(s\). Averaging removes all coherent cross terms, so

\[
\boxed{
\mathbb EG_s=
\frac14\left(1+\frac1{\kappa_s}\right)\Lambda_s
>7Hk_s
}
\tag{6.1}
\]

at every stage.

Let

\[
G_{s-1}=\langle\tau_2,\ldots,\tau_{s-1}\rangle.
\]

Write \(\mathfrak B_{H,G}(F)\) for the weighted integral floor energy obtained
by optimally balancing every depth-\(q\) load, \(q\le H\), inside each
\(G\)-orbit. With \(G_s=\langle G_{s-1},\tau_s\rangle\), define the released
profile floor at stage \(s\) by

\[
\Delta_s^Q
=\mathfrak B_{H,G_{s-1}}(F_{s-1})-
  \mathfrak B_{H,G_s}(F_s)
=\mathfrak B_{H,G_{s-1}}(F_{s-1})-
  \mathfrak B_{H,G_s}(F_{s-1}).
\tag{6.2a}
\]

The second equality is exact: every stage-\(s\) component switch replaces a
load contribution by its \(\tau_s\)-translate and therefore preserves every
\(G_s\)-orbit total. In the estimates below, expectation is over the initial
\(\delta\)-vector and all earlier balanced blocks; the current block outcome is
immaterial to \(\Delta_s^Q\).

### Lemma 6.1 (private targets are singleton prior orbits)

If \(s\in\mathcal S\) is odd, every private depth-\(H\) target pair from
Lemma 3.1 consists of two singleton \(G_{s-1}\)-orbits, and \(\tau_s\)
exchanges the two targets.

#### Proof

For \(P_s=1^s0^s\), the set underlying \(\mathsf B(P_s)\) is
\(\{1,\ldots,s\}\). An earlier edge
\(\tau_t=\{2t+2,2t+3\}\) straddles its boundary only if
\(s=2t+2\), impossible for odd \(s\). All other private-core coordinates in
(3.7), as well as the current pair coordinates, exceed every earlier endpoint
or equal \(n\). Thus every earlier generator fixes each target setwise, while
\(\tau_s\) swaps the current pair coordinates. \(\square\)

### Theorem 6.2 (positive-density annealed subgroup release)

For every odd \(s\in\mathcal S\),

\[
\boxed{
\mathbb E\Delta_s^Q
\ge
\frac{C_{M_s-H}(C_H^2-1)}{2c_H}
>\frac92Hk_s.
}
\tag{6.2}
\]

There are at least \(\lfloor L/2\rfloor\) such stages, and

\[
\boxed{
\sum_{\substack{s\in\mathcal S\\s\ {\rm odd}}}
\mathbb E\Delta_s^Q
>\frac92HC_{m-5}
>\frac9{2048}HB.
}
\tag{6.3}
\]

#### Proof

Fix a private pair indexed by \(V\), and condition on all randomness except
\(\delta_s\). The coherent \(J_s\)-pile contributes
\(\delta_sa_V\), where \(|a_V|\ge C_H\); write everything else as
\(b_V\). Then

\[
\mathbb E_{\delta_s}(b_V+\delta_sa_V)^2
=b_V^2+a_V^2\ge C_H^2.
\tag{6.4}
\]

By Lemma 6.1 the old subgroup orbits are singleton targets and the new subgroup
orbit is their pair. Its exact full-\(Q\) release is

\[
\frac{z_V^2-(|z_V|\bmod2)}{2c_H}.
\]

The parity term is at most one. Sum over the
\(C_{M_s-H}\) private pairs to obtain the first inequality.

Since \(C_H^2-1\ge C_H^2/2\), equations (3.10)--(3.14) yield

\[
\mathbb E\Delta_s^Q
>\frac{k_s4^H}{64L_AH^4}
\ge\frac92Hk_s.
\]

The first odd stage is \(s=3\), and
\(C_{m-5}>B/4^5=B/1024\), proving (6.3). \(\square\)

This is genuine later subgroup-profile release along evolving exact factors. It
is not an exposure ratio: an uncontrolled \(b_V^2\) may make
\(\Delta_s^Q\) much larger than the guaranteed gain.

---

## 7. The literal canonical corner

The fixed-endpoint theorem selects a coherent cube corner. There is an exact
alternative for the literal canonical MSW corner.

Orient selected packets so that the canonical corner has all signs \(+1\), and
put

\[
\Theta=
\sum_{s\in\mathcal S}
\left(1+\frac1{\kappa_s}\right)\Lambda_s,
\tag{7.1}
\]

\[
\mathfrak C=
\left\langle E,\sum_sD_s\right\rangle_H
+\sum_{s<t}\langle D_s,D_t\rangle_H.
\tag{7.2}
\]

### Theorem 7.1 (canonical descent-or-alignment dichotomy)

Independent balanced resampling from the canonical factor has expected total gain

\[
\boxed{
G_{\rm can}=\frac{\Theta+2\mathfrak C}{4}.
}
\tag{7.3}
\]

At least one of the following holds:

1. the canonical expected gain satisfies

   \[
   \boxed{G_{\rm can}>\frac7{512}HB;}
   \tag{7.4}
   \]

   consequently the canonical factor has a deterministic exact
   distinct-bridge path whose actual gain is at least \(G_{\rm can}\), and hence
   is greater than \(7HB/512\);

2. the packet piles have adverse aggregate base--pile plus cross-pile alignment

   \[
   \boxed{
   \mathfrak C<-\frac{\Theta}{4}<-\frac7{256}HB.
   }
   \tag{7.5}
   \]

#### Proof

The canonical residual is \(E+\sum_sD_s\). After balanced resampling, expected
squared residual is

\[
\|E\|_H^2+\sum_s\left(V_s-\frac{\Lambda_s}{\kappa_s}\right).
\]

Expansion gives (7.3). If \(\mathfrak C\ge-\Theta/4\), then
\(G_{\rm can}\ge\Theta/8\). By Theorem 3.2 and (2.5),

\[
\Theta>28HK>\frac7{64}HB,
\]

so (7.4) follows and some deterministic outcome attains at least the expected
gain. Otherwise (7.5) holds. \(\square\)

Thus prescribed-canonical failure forces a quantitative negative interaction,
not merely an absence of fragmentation.

---

## 8. Quantitative decay and structural limits

### Proposition 8.1 (geometric depletion in the explicit schedule)

With \(M=m-s-2\),

\[
\boxed{
\frac{k_{s+1}}{k_s}
=\frac{C_{M-1}}{C_M}
=\frac{M+1}{2(2M-1)}.
}
\tag{8.1}
\]

For \(M\ge5\),

\[
\frac14<\frac{k_{s+1}}{k_s}\le\frac13.
\tag{8.2}
\]

Consequently

\[
\boxed{
C_{m-4}\le K<\frac32C_{m-4}.
}
\tag{8.3}
\]

Both packet supply and the certified internal stage floor \(7Hk_s\) decay
geometrically.

#### Proof

Equation (8.1) is the Catalan ratio. The two inequalities in (8.2) reduce to
\(4(M+1)>4M-2\) and \(M\ge5\). Sum the geometric series. \(\square\)

This is a limitation of the explicit first-run schedule, not every possible
packet packing.

### Proposition 8.2 (simultaneous owner-packing capacity)

Suppose a family of pairwise owner-disjoint size-two packets is simultaneously
embedded in one exact factor, or in one fixed heterogeneous packet cube, and is
grouped into \(x_t\) packets at each of \(T\) distinct bridges. Then

\[
\boxed{\sum_{t=1}^T x_t\le\frac B2.}
\tag{8.4}
\]

At least \(T/2\) bridges therefore have

\[
\boxed{x_t\le\frac BT.}
\tag{8.5}
\]

#### Proof

Every packet uses two distinct owner rows, while the exact factor has \(B\) rows.
If more than \(T/2\) blocks had \(x_t>B/T\), their sum would exceed \(B/2\).
\(\square\)

Thus a positive-density \(T=\Theta(m)\) zero-recycling schedule of this
simultaneously embedded type cannot place a positive fraction of all owners in
every bridge cell. The statement does not constrain adaptive schedules that
create genuinely new packet owners after leaving the original cube, and it does
not upper-bound deeper-rank gain, whose cross terms may be large.

### Proposition 8.3 (first-shadow anchoring of the scheduled cube)

For a cyclic owner row \(C\), let

\[
B_{m-1}e_C=\sum_{S\in\mathcal W_{m-1}(C)}e_S
\]

be its rank-\((m-1)\) cyclic-interval histogram, extended linearly to formal
signed row sums. For \(s\in\mathcal S\) and \(R\in\mathcal D_{M_s}\), put

\[
X_{s,R}=P_s1100R,\qquad Y_{s,R}=P_s1010R,
\]

and, writing \(C(W)\) for the canonical MSW row indexed by \(W\), define the
oriented exact packet move

\[
z_{s,R}
=e_{\tau_sC(X_{s,R})}+e_{\tau_sC(Y_{s,R})}
-e_{C(X_{s,R})}-e_{C(Y_{s,R})}.
\]

Then, over every field and hence over the integers and reals,

\[
B_{m-1}
\sum_{s\in\mathcal S}\sum_{R\in\mathcal D_{M_s}}
c_{s,R}z_{s,R}=0
\quad\Longrightarrow\quad
c_{s,R}=0\quad\text{for all }(s,R).
\tag{8.6}
\]

Consequently two different vertices of the scheduled heterogeneous packet cube
never have the same depth-one histogram.

#### Proof

Put \(\beta_s=2s+2\) and \(\gamma_s=2s+3\). Let \(E_{s,R}\) be the
underlying set of the even list \(\mathsf E_{s,R}\) in (3.2), let \(x\) and
\(y\) be its first and last entries, and put
\(K_{s,R}=E_{s,R}\setminus\{x,y\}\). The exact rank-\((m-1)\) four-arm
cancellation gives

\[
\begin{aligned}
B_{m-1}z_{s,R}={}&
 e_{K_{s,R}\cup\{\beta_s,x\}}
-e_{K_{s,R}\cup\{\gamma_s,x\}}\\
&-e_{K_{s,R}\cup\{\beta_s,y\}}
+e_{K_{s,R}\cup\{\gamma_s,y\}}.
\end{aligned}
\tag{8.7}
\]

Indeed, a step-two window avoiding the four local positions, or containing both
positions of one local pair, cancels between the two old and two new rows. At
rank \(m-1\), the odd-list prefix and suffix are both the whole odd list and
cancel; the even-list prefix and suffix omit \(y\) and \(x\), respectively,
leaving exactly (8.7).

Because \(M_s\ge H\ge5\), \(R\) is nonempty. In the MSW flip list, the first
entry of \(\mathsf A(R)\) is the first-return down-step \(a_0(R)\). Since
\(P_s=1^s0^s\), the underlying set of \(\mathsf B(P_s)\) is \([s]\).
Therefore the square target

\[
S^*_{s,R}:=E_{s,R}\setminus\{x\}\cup\{\beta_s\}
\]

has the explicit form

\[
S^*_{s,R}
=[s]\cup\{n,\beta_s\}
\cup\left(2s+4+
\bigl(\operatorname{Down}(R)\setminus\{a_0(R)\}\bigr)\right),
\tag{8.8}
\]

and occurs in (8.7) with coefficient \(-1\).

For an \((m-1)\)-set \(S\), define

\[
\eta(S)=\min\{j\le2m:2|S\cap[j]|-j<0\}.
\]

The pivot \(S^*_{s,R}\) contains precisely \([s]\) among the first
\(2s+1\) coordinates. Its height is nonnegative through \(2s\) and equals
\(-1\) at \(2s+1\), so

\[
\eta(S^*_{s,R})=2s+1.
\tag{8.9}
\]

Every square target of a lower color \(u<s\) has first-negative position at
most \(2u+1<2s+1\): a target retaining the last even-list endpoint contains
all of \([u]\) and first becomes negative at \(2u+1\), while a target using
the first endpoint omits one member of \([u]\) and is negative by \(2u\).
Thus no lower-color column contains \(S^*_{s,R}\).

At color \(s\), the two targets using \(x\) omit one member of \([s]\), so
their first-negative position is at most \(2s\). Of the two targets using
\(y\), one contains \(\beta_s\) and the other \(\gamma_s\). Hence only the
\(\beta_s\)-target of another \(R'\) could equal \(S^*_{s,R}\), and equality
would imply

\[
\operatorname{Down}(R')\setminus\{a_0(R')\}
=\operatorname{Down}(R)\setminus\{a_0(R)\}.
\tag{8.10}
\]

This deletion map is injective. Given the displayed set, treat its positions as
down-steps and all other positions as up-steps, and let \(h'\) be the resulting
height. Changing the original first-return down-step to an up-step leaves the
old height before that step and raises it by two afterward, so the missing
position is

\[
a_0(R)=1+\max\{j:h'(j)=1\}.
\tag{8.11}
\]

Adding it back recovers \(R\). Thus \(S^*_{s,R}\) occurs in no other column
of color \(s\).

In a nonzero relation choose the largest active \(s\) and then an \(R\) with
nonzero coefficient. No higher color is active, no lower color or other
same-color column contains \(S^*_{s,R}\), and its coefficient in its own
column is \(-1\). The \(S^*_{s,R}\)-coordinate of the relation is therefore
\(-c_{s,R}\ne0\), a contradiction. This proves independence. Any difference
of two scheduled cube vertices is a nonzero signed combination of these packet
moves, proving the endpoint assertion. \(\square\)

This anchoring is qualitative across bridge colors; it gives no uniform
first-shadow norm lower bound proportional to the number of toggles.

### Proposition 8.4 (native bridges cannot span)

The complete native family

\[
\tau_s=(2s+2\ \ 2s+3),\qquad0\le s\le m-2,
\]

is a matching of \(m-1\) coordinate edges. It covers coordinates
\(2,\ldots,2m-1\), leaves \(1,2m,2m+1\) unmatched, and generates

\[
(C_2)^{m-1}
\]

with \(m+2\) coordinate orbits. Any coordinate spanning tree containing all native
edges needs another \(m+1\) nonnative edges. Hence a strict majority of the
\(2m=n-1\) tree stages has no local size-two packet certificate from this
native atlas.

#### Proof

The coordinate pairs are disjoint. A forest with \(m-1\) edges on \(n\) vertices
has \(n-(m-1)=m+2\) components; connecting them takes \(m+1\) further edges.
\(\square\)

Global rebasing does not alter this in a fixed pulled-back frame. Its preparation
letters are additional stages and must be counted.

---

## 9. Exact later-exposure defect

At one depth let \(\mathfrak B_G(\mu)\) be the minimum integral floor energy
obtained by balancing inside each \(G\)-orbit, and define

\[
\mathsf D_G(\mu)=Q(\mu)-\mathfrak B_G(\mu).
\tag{9.1}
\]

Let \(\mu^\tau\) be obtained by independently balancing every \(\tau\)-pair, and
put

\[
G^+=\langle G,\tau\rangle,
\quad
\mathcal R_\tau=Q(\mu)-Q(\mu^\tau),
\quad
\Delta_{G,\tau}
=\mathfrak B_G(\mu)-\mathfrak B_{G^+}(\mu).
\]

### Proposition 9.1 (transversal-dispersion identity)

\[
\boxed{
\Delta_{G,\tau}-\mathcal R_\tau
=
\mathsf D_{G^+}(\mu^\tau)-\mathsf D_G(\mu).
}
\tag{9.2}
\]

The identity holds rankwise and after fixed-window weighting.

#### Proof

Pair balancing preserves every \(G^+\)-orbit total, so
\(\mathfrak B_{G^+}(\mu^\tau)=\mathfrak B_{G^+}(\mu)\). Expanding the
right side gives (9.2). \(\square\)

At the first bridge both dispersions vanish, giving
\(\Delta=\mathcal R\). Later, elementary and subgroup release differ by a new
transversal-dispersion term.

There are integral formal orbit profiles with

\[
\frac{\mathcal R_\tau}{\Delta_{G,\tau}}=\frac1t.
\tag{9.3}
\]

Take two \(G\)-orbits \(O,O'\), each of size \(2t\). On \(O\) put \(t\)
zeros and \(t\) ones; on \(O'\) put \(t\) ones and \(t\) twos. Pair all
zeros with ones and all ones with twos except for one crossed pair \((0,2)\)
and compensating pair \((1,1)\). With global floor one, merging the two
\(G\)-orbits releases \(2t\), whereas pair balancing releases only two.

This is still a formal coordinate-orbit profile, not an exact wreath factor:
required total load, homogeneous point margins, and exact ownership completion
are not proved. It diagnoses the missing invariant but is not an exact-factor
counterexample.

---

## 10. Independent audit and scope

The geometry, signing algebra, and obstruction calculations were attacked
independently. The following corrections and checks are incorporated above.

1. **Shifted marker.** The private core is
   \(2s+4+2q+\mathsf A(V)\), not \(2s+4+\mathsf A(V)\). For
   \(q\le s\), a boundary entry of \(\mathsf B(P_s)\) is the marker;
   marking only \(n\) fails. For \(q>s\), \(n\) is valid.

2. **Weighted variance.** Equation (3.12) is an exact weighted sum followed by
   an inequality. It is not equal to \((8H-4)k_s\) unless every \(c_q=1\).

3. **Constants.** The chain

   \[
   \|D_s\|_H^2>36Hk_s,\qquad
   V_s\le(8H-4)k_s
   \]

   gives \(\Lambda_s>(28H+4)k_s\). The factor \(1/4\) in cube energy
   yields stage gain \(>7Hk_s\).

4. **Translated-side persistence.** A packet initially on \(\tau_sK\) remains
   a full fresh component; its connected bipartite overlay is merely read with
   sides exchanged.

5. **Backward signs.** Initial signs are selected backward against the unprocessed
   tail. Choosing a higher endpoint independently at each forward stage would
   charge an unaccounted preparation.

6. **Expectation.** Equation (5.1) is unconditional over earlier balanced
   choices. The scalar example after (4.8) shows conditional stage drift may be
   negative. Deterministic extraction preserves total gain, not every stage bound.

7. **Starting factor.** \(F^\sharp\) is a selected exact cube endpoint, not
   necessarily the literal canonical corner. Moving there is not free. Theorem
   7.1 gives the canonical alternative.

8. **Bridge versus microstep.** Macro-bridges are distinct and forest-fresh.
   Packet microsteps reuse one intrinsic cell and create no additional subgroup
   releases.

9. **Later release.** Only the first fixed-endpoint stage has
   \(\Delta^Q=\mathcal R\). The odd-stage subgroup theorem uses an annealed
   initial endpoint and the singleton-orbit proof.

10. **No exposure ratio.** Lower bounds on both gain and \(\Delta_s^Q\) do not
    compare them by a fixed fraction. Proposition 9.1 names the missing
    transversal dispersion.

11. **Matching scope.** Native bridges provide asymptotically half the tree-edge
    count but form only a matching. A strict majority of a completed spanning tree
    must be nonnative connectors.

12. **Decay scope.** Geometric depletion is specific to the explicit first-run
    schedule. The owner-packing bound is only for a simultaneously embedded
    packet atlas; native matching and first-shadow anchoring have the stated
    atlas-relative scopes.

---

## 11. Exact remaining theorem

The sixth wave removes one genuine obstacle: distinctness and owner recycling do
not prevent a linear number of exact bridge stages with positive unconditional
expected gain from one backward-selected exact endpoint in the canonical MSW
hierarchy. A positive-density zero-recycling schedule exists, every stage carries
positive internal coherence, and a positive-density odd subsequence has positive
expected later subgroup-profile release under a separate annealed initialization.
These two
initializations are not asserted to coincide on one prescribed path.

Three gates remain.

1. **Later capture ratio.** Control the transversal dispersion in (9.2) strongly
   enough to compare stage gain with \(\Delta_s^Q\).
2. **Prescribed low endpoint.** Replace the selected backward endpoint and
   annealed initial endpoint by a theorem starting at a prescribed global
   minimizer while paying all preparatory height.
3. **Nonnative connectors.** Supply productive exact components for the \(m+1\)
   connector edges needed to turn the native matching into a spanning tree.

Until these are proved, \(AFR_A\), fixed-window balancing, MWB, and the
contiguous-OR conjecture remain open.
