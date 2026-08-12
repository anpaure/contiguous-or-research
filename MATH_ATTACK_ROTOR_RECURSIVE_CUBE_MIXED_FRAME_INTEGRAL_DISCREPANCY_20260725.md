# Recursive-cube rotor resolution: fixed-frame no-go and the exact mixed-frame discrepancy

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web input is
used.

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 Q_m=(2m-1)(2m)!.
\]

Fix \(A>0\) and \(H=\lceil A\sqrt m\rceil\). The new recursive cube
permutation in `ROTOR_SCD_PARITY_CHECK_CYCLE_TILING_20260725.md` is valid:
it partitions an \(\ell\)-dimensional orientation cube into \(2\ell\)-cycles,
has coordinate residence exactly \(\ell\), and is simultaneously lower- and
upper-rainbow through depth \(\ell/2\). In particular, its exponentially many
coordinate orders are genuine and remove the old within-cube template
obstruction.

It does **not** give a low-toll SCD while all blocks use one fixed coordinate
pairing. The Gaussian pair-type deficit is insensitive to the order used
inside an orientation cube. If all selected rotor arcs use pairs of one fixed
perfect matching, then

\[
 \liminf_{m\to\infty}
 \frac{\widehat\Phi_H}{W}
 \ge 2e^{-A^2}\Delta(A)>0,
 \qquad
 \Delta(A)=\Phi_{\rm G}(A/2)-e^{A^2}\Phi_{\rm G}(-3A/2).
 \tag{0.1}
\]

Thus the recursive factor cannot be completed to the required SCD inside one
stationary pair frame. More quantitatively, any \(o(W)\)-toll repair of a
fixed-frame forest needs

\[
 \Omega_A(W/\sqrt m)
 \tag{0.2}
\]

selected arcs outside that frame, contaminating \(\Omega_A(W)\) Gaussian
windows.

There is, however, no interface-toll obstruction to changing the frame
*blockwise*. If recursive necklaces have \(R=2\ell\) middle owners and
\(\ell/H\to\infty\), one hard cut per necklace costs at most

\[
 \frac{2HW}{R}=\frac{HW}{\ell}=o(W).
 \tag{0.3}
\]

The frame may therefore depend on the necklace (and hence on its owners),
even if almost every necklace uses a different coordinate pairing.

The exact remaining problem is integral. Let \(A_{\rm rec}\) be the
band-mask incidence matrix of all coordinate relabelings of native recursive
necklaces. Then:

1. \(A_{\rm rec}x=\mathbf1\) has an explicit nonnegative rational solution
   of weighted toll at most \(HW/\ell=o(W)\);
2. an integral solution \(A_{\rm rec}z=\mathbf1\), together with negligible
   correction chains, is exactly a saturated central-band SCD with low rotor
   toll, and hence gives the requested coloring into \(Q_m\) genuine SCDs;
3. whole \(R\)-necklaces alone have the necessary congruences
   \(R\mid\gamma_d\) in every radius class. These already fail infinitely
   often (for example, at \(m\) a power of two); and
4. after the \(O(RH)\) census residues are allowed as correction chains, the
   unresolved assertion is the nonnegative **exact-cover/completion** equation
   on individual masks. Equal rank counts do not imply this equation.

Consequently this note does not prove coefficient one. It identifies the
precise surviving lemma inside the SCD route: mixed-frame
recursive-necklace exact rounding with low-cost integral completion. The new
exponential order diversity solves the local cube part, and (0.3) solves the
interface ledger; neither solves this semigroup discrepancy.

There is a weaker and more appropriate direct target. The exact literal
compiler does not require the selected vertical flags to form an SCD. It
only requires an exact partition of the middle owners, \(o(W)\) aggregate
lower/upper path-hitting holes, and \(o(W)\) useful-prefix bridge excess.
This is the gate \(\mathrm{MFUP}_A\). Section 6 below shows that its
middle-owner and target-cover LP is feasible by the same mixed group orbit,
and that the bridge term is automatically \(o(W)\) for unfragmented
\(2\ell\)-necklaces. Thus \(\mathrm{MFUP}_A\), not the stronger exact-SCD
semigroup equation, is the primary remaining integral discrepancy.

## 1. The audited rotor ledger

Set \(N_{m+1}=0\), and for the band clipped at radius \(H\) put

\[
 \gamma_d=N_d-N_{d+1}\quad(0\le d<H),
 \qquad \gamma_H=N_H.
 \tag{1.1}
\]

Then

\[
 \sum_{d=0}^H\gamma_d=W,
 \qquad
 \sum_{d=q}^H\gamma_d=N_q\quad(0\le q\le H).
 \tag{1.2}
\]

For a full SCD \(\mathcal D\), clipped to this band, let
\(p_d^*(\mathcal D)\) be
the minimum number of components in a spanning vertex-disjoint directed
rotor path forest on its radius-\(d\) chain states. The exact hard-prefix
run-start toll is

\[
 \widehat\Phi_H(\mathcal D)
 =\sum_{d=0}^H2d\,p_d^*(\mathcal D).
 \tag{1.3}
\]

If

\[
 P_q(\mathcal D)=\sum_{d=q}^Hp_d^*(\mathcal D),
 \tag{1.4}
\]

then the layer-cake identity is

\[
 \widehat\Phi_H(\mathcal D)
 =2\sum_{q=1}^HP_q(\mathcal D).
 \tag{1.5}
\]

The conservative reset toll
\(\Phi_H=\sum_d(2d+1)p_d^*\)
has the same \(o(W)\) threshold; radius zero contributes at most
\(\gamma_0=W/(m+1)=o(W)\). We use (1.3), since it is the exact prefix toll.

The audited chronology-elimination theorem gives

\[
 \min\{\text{exact master prefix toll}\}
 =Q_m\min_{\mathcal D\ {\rm full\ SCD}}
       \widehat\Phi_H(\mathcal D).
 \tag{1.6}
\]

The separately charged physical initialization is within a constant factor
of the conservative toll. Hence the \(o(Q_mW)\) question is equivalent to
finding one full integral SCD with (1.3) equal to \(o(W)\). In particular,
mixing many SCD colors cannot average away the absence of one good SCD.

Finally, every saturated SCD of the ranks \(m-H,\ldots,m+H\) extends
integrally to a full SCD while preserving each band chain as a contiguous
subchain. It is therefore enough, but essential, to produce an **exact
saturated band SCD**. A near-packing with the correct rank census is not
enough.

## 2. Audit of the recursive cube factor

Let \(\ell\) be a power of two and \(Q_\ell=\mathbb F_2^\ell\). Define
\(F_1\) by toggling its only coordinate. Recursively, for \(\ell=2a\) and
\((u,v)\in Q_a\times Q_a\), set

\[
 F_{2a}(u,v)=
 \begin{cases}
  (F_a(u),v),&|u|+|v|\equiv0\pmod2,\\
  (u,F_a(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}
 \tag{2.1}
\]

Let \(\rho_\ell(x)\) be the toggled coordinate. For \(q\ge0\), define

\[
 D_q^+(x)=\{\rho_\ell(F_\ell^jx):0\le j<q\},
 \qquad
 \Sigma_q^+(x)=
 \bigl(D_q^+(x),x|_{[\ell]\setminus D_q^+(x)}\bigr),
 \tag{2.2}
\]

and define \(\Sigma_q^-\) using \(F_\ell^{-1}\).

### Theorem 2.1 (recursive half-depth factor, audited)

For every power of two \(\ell\ge2\):

1. \(F_\ell\) is a permutation and all its cycles have length \(2\ell\);
2. the transition word on each cycle is \(\pi\pi\) for a permutation
   \(\pi\) of the \(\ell\) coordinates; and
3. for every \(0\le q\le\ell/2\), both \(\Sigma_q^+\) and \(\Sigma_q^-\)
   are injective on \(Q_\ell\).

#### Proof

The inverse recursion is

\[
 F_{2a}^{-1}(u,v)=
 \begin{cases}
  (F_a^{-1}(u),v),&|u|+|v|\equiv1\pmod2,\\
  (u,F_a^{-1}(v)),&|u|+|v|\equiv0\pmod2.
 \end{cases}
 \tag{2.3}
\]

Thus \(F_{2a}\) is bijective. Total parity changes at every move, so the
two halves move alternately and

\[
 F_{2a}^{2t}(u,v)=(F_a^t(u),F_a^t(v)).
 \tag{2.4}
\]

Inductively the exact period of every \(F_a\)-orbit is \(2a\). An odd
return in (2.4) is impossible by parity, and an even return requires \(t\)
to be a common multiple of the two exact periods. The exact \(F_{2a}\)
period is therefore \(4a=2(2a)\).

By induction, every \(a\) consecutive moves of an \(F_a\)-orbit use every
coordinate of that half once. During \(2a\) global moves, each half makes
exactly \(a\) moves. Hence those \(2a\) global moves use all \(2a\)
coordinates once. The next \(2a\) moves repeat the same interleaving, which
proves the \(\pi\pi\) assertion.

For injectivity, induct on \(\ell\). The case \(\ell=2\) is the four-cycle.
Let \(\ell=2a\). If \(q=2t\le a\), the two halves each make
\(t\le a/2\) moves, and \(\Sigma_{2t}^+(u,v)\) splits canonically into

\[
 \Sigma_t^+(u),\qquad \Sigma_t^+(v).
 \tag{2.5}
\]

The induction hypothesis recovers \(u,v\). If \(q=2t+1\le a\), the half
scheduled first makes \(t+1\) moves and the other makes \(t\). The two
deleted-set cardinalities identify the first half, hence the initial total
parity. Since \(a\) is even and \(q\le a\), one has \(t+1\le a/2\).
The two induced shadows again recover \(u,v\) by induction. The inverse
recursion (2.3) gives the identical argument for \(\Sigma_q^-\). \(\square\)

In the fixed-pair interpretation, a \(q\)-step forward window empties the
next \(q\) split pairs and gives the lower shadow; a reverse window fills
the preceding \(q\) split pairs and gives the upper shadow. Therefore
Theorem 2.1 partitions an orientation cube into genuine pair-flip rotor
cycles which are two-sided rainbow through half depth.

The exponential order diversity is also real. If \(T_\ell\) is the number
of distinct cyclic coordinate orders among the cycles, the template-capacity
bound at \(q=\ell/2\) gives

\[
 T_\ell\ge\frac{2^{\ell/2}}\ell.
 \tag{2.6}
\]

No step of the proof above supplies ownership of masks lying in different
pair-type strata. That missing implication is exactly where the fixed-frame
capacity deficit enters.

### 2.2 The exact path-hitting interpretation

The shadow condition is most cleanly stated without referring to a chosen
pair frame. Let

\[
 X_0,X_1,\ldots
 \tag{2.7}
\]

be consecutive vertices of a Johnson cycle in the middle rank, and for a
rank-\(m-q\) target \(T\) put

\[
 \mathcal U_T
 =\{X\in\tbinom{[2m]}m:T\subseteq X\}.
 \tag{2.8}
\]

If \(X_j,\ldots,X_{j+q}\) is a Johnson geodesic, then

\[
 \left|\bigcap_{a=0}^qX_{j+a}\right|=m-q.
 \tag{2.9}
\]

Consequently this window has lower shadow \(T\) if and only if

\[
 X_j,X_{j+1},\ldots,X_{j+q}\in\mathcal U_T.
 \tag{2.10}
\]

Indeed, membership in the up-set gives
\(T\subseteq\bigcap_aX_{j+a}\), and (2.9) forces equality. For the
recursive factor, every window of length at most \(\ell+1\) is geodesic, so
(2.10) applies
through the whole certified range.

For comparison, the odd-wreath normalization has ground-set size
\(2m+1\) and

\[
 X_j=I_\pi(j,m).
 \tag{2.11}
\]

There one has the exact identities

\[
 \bigcap_{a=0}^qX_{j+a}=I_\pi(j+q,m-q),
 \qquad
 \bigcup_{a=0}^qX_{j+a}=I_\pi(j,m+q).
 \tag{2.12}
\]

Thus lower ownership is exactly the consecutive-path hitting problem
(2.10). In odd dimension, complementation sends a rank-\(m+q\) upper
target to rank \(m-(q-1)\), so **upper depth \(q\) is the complement of
lower depth \(q-1\)**. The shift must not be suppressed. In the present
even rotor band on \(2m\) coordinates, complementation instead preserves
the numerical depth \(q\). All incidence equations below use the appropriate
parity convention.

## 3. A stationary frame is still impossible

Fix a perfect matching \(\mathcal P\) of the \(2m\) ground coordinates. A
rank-\(m-q\) target of pair type \(f\) has

\[
 f\text{ full pairs},\qquad f+q\text{ empty pairs},\qquad
 m-2f-q\text{ split pairs}.
\]

The number of such targets is

\[
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
 \tag{3.1}
\]

The number of middle starts with \(f\) full pairs, \(f\) empty pairs and
\(m-2f\) split pairs is

\[
 V_f
 =\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.
 \tag{3.2}
\]

Set

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
 \tag{3.3}
\]

Order diversity cannot change (3.1)--(3.2): a \(q\)-window using pairs of
\(\mathcal P\) empties \(q\) currently split pairs and preserves \(f\).

### Theorem 3.1 (fixed-frame and exceptional-arc inequalities)

Let a clipped SCD have selected path forests in all radii \(d\ge q\), and
let \(P_q\) be their total number of path components. If every selected arc
uses a pair of \(\mathcal P\), then

\[
 qP_q\ge D_{m,q}.
 \tag{3.4}
\]

More generally, if \(s_q\) selected arcs in these forests do not use a pair
of \(\mathcal P\), then

\[
 q(P_q+s_q)\ge D_{m,q}.
 \tag{3.5}
\]

#### Proof

A path with \(t\) states contains \((t-q)_+\) starts followed by \(q\)
arcs, and \((t-q)_+\ge t-q\). Summing over the \(P_q\) paths, which contain
\(N_q\) states in total, gives at least \(N_q-qP_q\) length-\(q\) starts.
In a pure fixed-frame window, the \(q\) used pairs are distinct: after a pair
is used, its inserted endpoint remains in the radius state word throughout
the window. Its lower shadow therefore has the same value of \(f\) as its
middle start.

The SCD property makes all lower shadows distinct. Type \(f\) can supply at
most \(\min(V_f,T_{f,q})\) distinct targets. Hence

\[
 N_q-qP_q
 \le\sum_f\min(V_f,T_{f,q})
 =N_q-D_{m,q},
\]

which proves (3.4). One exceptional arc lies in at most \(q\) of the
length-\(q\) windows just counted. Removing all contaminated windows leaves
at least \(N_q-qP_q-qs_q\) pure starts. Repeating the argument proves
(3.5). \(\square\)

For \(q=A\sqrt m+o(\sqrt m)\), the exact likelihood ratio is

\[
 \frac{T_{f,q}}{V_f}
 =\prod_{i=0}^{q-1}
   \frac{m-2f-i}{2(f+1+i)}.
 \tag{3.6}
\]

Writing \(X_m=(f-m/4)/\sqrt m\), the source law \(V_f/W\) converges to
\(N(0,1/16)\), while the target law \(T_{f,q}/N_q\) converges to
\(N(-A/2,1/16)\). Uniformly for bounded \(X_m\),

\[
 \log\frac{T_{f,q}}{V_f}=-8AX_m-3A^2+o(1),
 \tag{3.7}
\]

so the ratio crosses one at \(X_m=-3A/8+o(1)\). Consequently

\[
 \frac{D_{m,q}}W
 \longrightarrow
 e^{-A^2}\Phi_{\rm G}(A/2)-\Phi_{\rm G}(-3A/2)
 =e^{-A^2}\Delta(A)>0.
 \tag{3.8}
\]

By (1.5),

\[
 \widehat\Phi_H
 \ge2qP_q\ge2D_{m,q},
 \tag{3.9}
\]

which proves (0.1). If instead \(\widehat\Phi_H=o(W)\), then
\(P_q=o(W/\sqrt m)\), and (3.5), (3.8) give

\[
 s_q\ge
 \left(\frac{e^{-A^2}\Delta(A)}A-o(1)\right)
 \frac W{\sqrt m}.
 \tag{3.10}
\]

Every cycle of Theorem 2.1 inside one fixed frame is pure in the sense of
Theorem 3.1. Therefore neither its long residence nor its exponential order
library affects (3.9). The new factor solves the conditional problem
"given a source stratum, avoid internal shadow repetitions"; it cannot
alter the source-to-target type imbalance between (3.1) and (3.2).

## 4. Mixed frames have negligible interface toll

Take a power of two ℓ with

\[
 2H\le\ell\le m,
 \qquad R=2\ell.
 \tag{4.1}
\]

Embed one \(F_\ell\)-cycle into an all-split coordinate-pair frame on the
\(2m\) ground coordinates. For a fixed \(0\le d\le H\), attach to each
cycle vertex its native symmetric chain segment of radius \(d\): the lower
members are the forward empty-pair shadows and the upper members are the
reverse full-pair shadows.

Theorem 2.1 implies that the \(R\) chain segments are pairwise mask-disjoint
inside the band. Consecutive centers are directed rotor neighbors. Call this
family a **typed recursive necklace** \(B_d\). It has

\[
 R(2d+1)
 \tag{4.2}
\]

band masks and \(R\) middle owners. Cutting its directed center cycle once
gives one radius-\(d\) rotor path component, of exact prefix toll \(2d\).

### Lemma 4.1 (blockwise frame-change ledger)

Suppose a saturated central-band SCD is the disjoint union of typed
recursive necklaces \(B_j\), where necklace \(j\) may use an arbitrary
coordinate pairing and has \(R_j\ge R_{\min}\) middle owners. Then

\[
 \widehat\Phi_H
 \le\sum_j2d_j
 \le \frac{2HW}{R_{\min}}.
 \tag{4.3}
\]

In particular, if \(R_{\min}=2\ell\) and \(\ell/H\to\infty\), this is
\(o(W)\).

#### Proof

At radius \(d\), cut each selected necklace of type \(d\) once. The resulting
paths are vertex-disjoint and span that radius class, so they are an
admissible path forest. This gives the first inequality. The middle members
of all necklaces partition the \(W\) middle masks, whence the number of
necklaces is at most \(W/R_{\min}\). Since \(d_j\le H\), the second
inequality follows. \(\square\)

This is the desired phase-changing-frame mechanism at the toll level. No
rotor splice between different frames is required: every frame interface is
declared a hard start. With \(\ell\asymp m\), the charge is
\(O_A(W/\sqrt m)\).
The fixed-frame lower bound is not contradicted, because relative to any one
pairing, the internal arcs of necklaces using other pairings are exceptional;
only the **paid boundaries** are sparse.

### Corollary 4.2 (conditional \(Q_m\)-color resolution)

If the band admits such a mixed-frame necklace SCD with \(\ell/H\to\infty\),
then it extends to a full SCD \(\mathcal D\) with
\(\widehat\Phi_H(\mathcal D)=o(W)\). The coordinate-orbit/Euler construction
then resolves the exact rotor master into \(Q_m\) genuine full-SCD colors with
total prefix toll

\[
 Q_m\widehat\Phi_H(\mathcal D)=o(Q_mW).
 \tag{4.4}
\]

The conservative reset and physical-initialization ledgers are \(o(Q_mW)\)
as well.

Thus frame interfaces are no longer the issue. The issue is whether the
necklace chain segments can be chosen to partition every band mask exactly.

## 5. The mixed-frame fractional system is solved exactly

Let \(\mathcal U_H\) be the set of masks in ranks
\(m-H,\ldots,m+H\). Fix one typed recursive necklace \(B_d\) for each
\(0\le d\le H\), all with the same \(R=2\ell\). For every
\(\sigma\in S_{2m}\), let \(\sigma B_d\) be its coordinate
relabeling. Relabeling changes the underlying pair frame, so this is a
genuinely mixed-frame reservoir.

Equivalently, the lower rank-\(m-q\) entries of the column of
\(\sigma B_d\) are precisely the targets \(T\) whose principal up-sets
\(\mathcal U_T\) contain one of its consecutive \((q+1)\)-vertex paths. The
upper
entries are obtained from the reverse paths and complementation. Thus the
matrix below records exact Johnson-path hits, not merely pair-type counts.

Index repeated orbit copies by \(\sigma\), even when two copies have the same
unlabelled support. Let \(G=(2m)!\), and let \(A_{\rm rec}\) be the
\(0\)-\(1\) band-mask incidence matrix of these columns.

### Theorem 5.1 (explicit low-toll fractional resolution)

Assign to every copy σB_d the weight

\[
 x_{\sigma,d}=\frac{\gamma_d}{GR}.
 \tag{5.1}
\]

Then

\[
 A_{\rm rec}x=\mathbf1_{\mathcal U_H}.
 \tag{5.2}
\]

Its total weighted run-start toll is exactly

\[
 \sum_{\sigma,d}2d\,x_{\sigma,d}
 =\frac1R\sum_{d=0}^H2d\gamma_d
 =\frac2R\sum_{q=1}^HN_q
 \le\frac{2HW}{R}
 =\frac{HW}{\ell}.
 \tag{5.3}
\]

#### Proof

For \(q\le d\), one necklace \(B_d\) contains exactly \(R\) masks of rank
\(m-q\) and \(R\) masks of rank \(m+q\). The symmetric group is transitive
on either rank, so a fixed mask in that rank occurs in exactly \(GR/N_q\)
of the indexed copies \(\sigma B_d\). Its total degree under (5.1) is
therefore

\[
 \sum_{d=q}^H
 \frac{\gamma_d}{GR}\frac{GR}{N_q}
 =\frac1{N_q}\sum_{d=q}^H\gamma_d=1
\]

by (1.2). The middle-rank calculation is the same with \(q=0\). This proves
(5.2). The first equality in (5.3) is the one-cut cost of a necklace. The
layer-cake identity

\[
 \sum_{d=0}^Hd\gamma_d=\sum_{q=1}^HN_q
\]

proves the rest. \(\square\)

Thus every rank equation, every lower/upper marginal, and the desired toll
are simultaneously feasible over the rationals. This construction mixes
all coordinate pairings through the group orbit; it is not the invalid
independent randomization of strata in one pairing.

## 6. The weaker direct discrepancy \(\mathrm{MFUP}_A\)

The direct useful-prefix compiler associated with a legal piece has exact
length

\[
 W+2H+\sum_{j<C}(b_j-1)
   +\sum_{q=1}^H(M_q^-+M_q^+).
 \tag{6.1}
\]

Here the pieces partition the \(W\) middle owners, \(b_j\) is the shortest
positive MTF bridge from the terminal state of piece \(j\) to the useful
initial prefix of piece \(j+1\), and \(M_q^\pm\) are the lower and upper
path-hitting holes. This formula uses no SCD colors.

We now write its exact integer optimization. Let \(\mathscr B\) contain all
oriented, coordinate-relabelled legal segments of the recursive factor. For
\(B\in\mathscr B\), let

\[
 M(B)\subseteq\binom{[2m]}m
 \tag{6.2}
\]

be its middle-owner set. Let \(M\) be the middle-incidence matrix
\(M_{X,B}=\mathbf1_{X\in M(B)}\).

For later fractional comparison, define the **internal** incidence
\(h_{T,B}^-=1\) when \(B\) itself contains a consecutive
\((q+1)\)-vertex Johnson path in \(\mathcal U_T\), and define \(h_{T,B}^+\)
by reverse paths and complementation. These internal hits are sufficient but
not exhaustive: a physical bridge may create a useful path or advertised
flag crossing two pieces.

For a \(0\)-\(1\) selection \(z\), the stronger internal-only hole count is

\[
 {\rm Hol}_{\rm int}(z)
 =\sum_{q=1}^H\left[
   \sum_{T\in\binom{[2m]}{m-q}}
     \left(1-\sum_Bh_{T,B}^-z_B\right)_+
  +\sum_{T\in\binom{[2m]}{m+q}}
     \left(1-\sum_Bh_{T,B}^+z_B\right)_+
 \right].
 \tag{6.3}
\]

Let \(\Pi\) be a physical chronology ordering and orienting the selected
pieces. Recursively let \(\Sigma_j^{\rm out}(\Pi)\) be the *actual*
last-occurrence state after piece \(j\), including the residual state
transported from all earlier pieces, and let
\(\Lambda_{j+1}^{\rm in}(\Pi)\) be the chosen useful initial prefix of the
next piece. Put

\[
 {\rm Br}(\Pi)
 =\sum_{j<C}
 \bigl(b(\Sigma_j^{\rm out}(\Pi),\Lambda_{j+1}^{\rm in}(\Pi))-1\bigr),
 \tag{6.4}
\]

where the exact useful-prefix bridge satisfies
\(1\le b(\Sigma,\Lambda)\le2H+1\).

Let \(\mathcal H_q^\pm(\Pi)\) be the sets of lower and upper rank targets
actually exposed at the designated principal endpoints of the compiled
chronology, including useful flags crossing piece boundaries. In the odd
wreath normalization, the upper depth-\(q\) ledger is the complementary
lower depth-\((q-1)\) ledger. Define

\[
 {\rm Hol}(\Pi)
 =\sum_{q=1}^H
 \left[
   N_q-|\mathcal H_q^-(\Pi)|
  +N_q-|\mathcal H_q^+(\Pi)|
 \right].
 \tag{6.5}
\]

Every internal hit remains literal in the compilation, while bridges may add
hits, so \({\rm Hol}(\Pi)\le{\rm Hol}_{\rm int}(z)\).

Now define

\[
 \boxed{
 \mathfrak M_{m,H,\ell}
 =\min\left\{
   {\rm Hol}(\Pi)+{\rm Br}(\Pi):
   Mz=\mathbf1,\ z\in\{0,1\}^{\mathscr B},\
   \Pi\text{ is a legal physical chronology of }\operatorname{supp}z
 \right\}.}
 \tag{6.6}
\]

### Proposition 6.1 (exact direct equivalence)

The mixed-frame useful-prefix gate \(\mathrm{MFUP}_A\) is exactly

\[
 \mathfrak M_{m,H,\ell}=o_A(W)
 \tag{6.7}
\]

for some \(\ell\) with \(H=o(\ell)\le m\), allowing \(o(W/H)\) residual
short pieces. If (6.7) holds, the direct compiler gives a central-band OR
word of length \(W+o_A(W)\).

#### Proof

The equation \(Mz=\mathbf1\) is precisely the exact middle-owner partition.
By the path-hitting equivalence (2.10), (6.5) is precisely the number of
missing advertised band masks. Formula (6.4) is the exact bridge excess,
not an upper proxy. Substitution in (6.1) proves both directions within the
declared legal-piece architecture. \(\square\)

The use of the actual state in (6.4) is essential: the terminal residual of
a piece need not be intrinsic to that piece, so the bridge costs do not form
a fixed pairwise metric on \(\mathscr B\).

The bridge part is nevertheless not the hard term if rounding preserves long
necklaces.
If all but \(o(W/H)\) selected pieces have at least \(R=2\ell\) owners, then

\[
 C\le \frac WR+o(W/H)
 \tag{6.8}
\]

and an arbitrary legal ordering satisfies

\[
 {\rm Br}(\Pi)\le2HC
 \le\frac{2HW}{R}+o(W)
 =\frac{HW}{\ell}+o(W)=o(W).
 \tag{6.9}
\]

Thus useful-prefix compatibility need not be optimized separately unless an
integral rounding fragments a positive fraction of the necklaces.

### Proposition 6.2 (mixed-frame fractional MFUP system)

For all sufficiently large \(m\), take \(\ell\) to be the largest power of
two not exceeding \(m\), so \(R=2\ell\ge m+1\) and \(H\le\ell/2\). Cut one
full recursive necklace into an open legal segment \(B\) with \(R\) middle
owners, and take all indexed coordinate
relabelings \(\sigma B\), \(\sigma\in S_{2m}\). Give each orbit copy weight

\[
 x_\sigma=\frac{W}{(2m)!\,R}.
 \tag{6.10}
\]

Then every middle owner has weighted degree exactly one. Every lower or
upper target at even depth \(1\le q\le H\) has weighted path-hit degree at
least

\[
 \left(1-\frac qR\right)\frac W{N_q}\ge1.
 \tag{6.11}
\]

#### Proof

The open segment has \(R\) distinct middle owners. At depth \(q\), exactly
\(R-q\) starts are followed by \(q\) internal edges. By Theorem 2.1 and
(2.10), their lower path hits are distinct; the reverse-path statement gives
\(R-q\) distinct upper hits. The symmetric group is transitive on each
rank. Double counting orbit incidences gives \((2m)!R/W\) copies through a
fixed middle owner and \((2m)!(R-q)/N_q\) copies through a fixed target.
Multiplication by (6.10) gives the first expression in (6.11) and middle
degree one.

It remains to prove the last inequality. The exact ratio satisfies

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}
 \le\frac{m-q+1}{m+q}
 \le\frac{m-q+1}{m+1}
 =1-\frac q{m+1}
 \le1-\frac qR,
 \tag{6.12}
\]

where the first inequality follows by retaining the last factor and bounding
every remaining factor by one. This proves
(6.11). \(\square\)

Proposition 6.2 is the exact fractional removal of the fixed-frame
pair-type deficit. It is stronger than targetwise availability: one common
mixed orbit simultaneously satisfies the owner equalities and every target
cover inequality. It supplies no integral owner partition, and hence no
physical chronology.

The first integral obstruction for full \(R\)-cycles is the middle congruence
\(R\mid W\). Variable-length residual segments remove that scalar obstruction
at negligible cost, but they do not solve the simultaneous owner-partition
and low-hole rounding in (6.6). This is the primary unresolved discrepancy.

## 7. The stronger exact-SCD integral discrepancy

Theorem 5.1 does not round automatically. First consider whole typed
\(R\)-necklaces only. For an integral selection \(z\), let

\[
 k_d=\sum_\sigma z_{\sigma,d}.
\]

If \(A_{\rm rec}z=\mathbf1\), summing the rank-\(m-q\) equations gives

\[
 R\sum_{d=q}^Hk_d=N_q.
 \tag{7.1}
\]

Subtracting consecutive equations yields

\[
 \boxed{Rk_d=\gamma_d\quad(0\le d\le H).}
 \tag{7.2}
\]

Hence \(R\mid\gamma_d\) for every \(d\), and in particular \(R\mid W\).
This obstruction is real. Kummer's theorem gives

\[
 v_2\binom{2m}{m}=s_2(m),
 \tag{7.3}
\]

where \(s_2(m)\) is the number of ones in the binary expansion of \(m\).
If \(m\) is a power of two, then \(v_2(W)=1\). For \(\ell\ge2\),
\(R=2\ell\) is divisible by four, so even the middle-rank equation
in (7.1) is impossible along this infinite sequence.

This congruence is not an asymptotic toll obstruction. Put

\[
 r_d\equiv\gamma_d\pmod R,
 \qquad 0\le r_d<R.
 \tag{7.4}
\]

If correction chains are allowed, their radius counts \(h_d\) must satisfy

\[
 h_d\equiv r_d\pmod R.
 \tag{7.5}
\]

The minimal census has

\[
 \sum_dh_d\le (H+1)(R-1),
 \qquad
 \sum_d2d\,h_d=O(RH^2)=o(W)
 \tag{7.6}
\]

for \(R\le2m\) and \(H=O_A(\sqrt m)\). Thus the rank residues can be paid
for polynomially cheaply **if** suitable disjoint correction chains exist.
That final qualification is substantive: even a one-chain leave with the
correct lower, middle, and upper cardinalities need not complete to a
saturated band SCD.

Here is the exact formulation. Let \(\mathscr C\) be the family of all valid
symmetric chain segments in \(\mathcal U_H\), used as possible correction
columns. Let \(A_{\rm cor}\) be their mask-incidence matrix, and give a
radius-\(d\) correction chain cost \(2d\). Define

\[
 \mathfrak I_{m,H,\ell}
 =\min\left\{
   \sum_{\sigma,d}2d\,z_{\sigma,d}
   +\sum_{C\in\mathscr C}2d(C)y_C:
   A_{\rm rec}z+A_{\rm cor}y=\mathbf1_{\mathcal U_H},
   \ z,y\in\mathbb Z_{\ge0}
 \right\}.
 \tag{7.7}
\]

The middle-rank rows force all chosen columns to be mask-disjoint, and all
other rows force exact lower and upper ownership. Therefore a feasible point
of (7.7) is precisely a saturated band SCD assembled from recursive
necklaces and correction chains. Cutting every necklace once and treating
each correction chain as one path gives

\[
 \widehat\Phi_H\le\mathfrak I_{m,H,\ell}.
 \tag{7.8}
\]

Conversely, every band SCD in this declared architecture induces a feasible
integer point with its stated one-cut toll. Thus the exact missing statement
is

\[
 \boxed{
 \text{for some power of two }\ell\text{ with }H=o(\ell)\le m,
 \qquad
 \mathfrak I_{m,H,\ell}=o(W).}
 \tag{MRC_A}
\]

Theorem 5.1 proves the corresponding LP statement with value at most
\(HW/\ell=o(W)\). Equations (7.2)--(7.6) identify the first integral
discrepancy. After those rank residues are supplied, what remains is the
nonnegative exact-cover question in (7.7), not another scalar census. In
algebraic terms, the unresolved issue is whether the all-ones incidence
vector lies in the low-cost part of the affine semigroup generated by the
mixed-frame necklace and correction columns. Its membership in the real
cone is already proved.

## 8. Implications and nonimplications

If \((\mathrm{MRC}_A)\) holds for every fixed \(A>0\), Corollary 4.2 gives
an exact \(Q_m\)-SCD coloring with total weighted run-start toll
\(o(Q_mW)\). The standard fixed-window diagonal argument then supplies the
rotor route to coefficient one.

The following weaker assertions do not prove \((\mathrm{MRC}_A)\):

1. partitioning every orientation cube of one fixed pairing by the recursive
   factor;
2. exponential diversity of the coordinate orders inside those cubes;
3. the rational identity \(A_{\rm rec}x=\mathbf1\);
4. correct rank totals or the residue bounds (7.6);
5. a near-perfect packing leaving \(o(W)\) masks; or
6. a block factor on the middle rank alone.

Nor is any converse from arbitrary near-optimal OR words to these necklace
columns being used. A general OR word has ordered-partition states and may
make nonsingleton updates. The implication

\[
 \text{coefficient one}\Longrightarrow
 \text{singleton central near-universal cycle}
\]

is unsupported. Recursive necklaces and the path-hitting system (2.10) are
used here only as a sufficient structured route to a low-toll SCD.

The fixed-frame no-go (3.9) forces genuine owner-dependent frame mixing.
The blockwise construction in Section 4 shows that such mixing can occur on
\(\ell\)-scale pieces with only \(O(HW/\ell)=o(W)\) paid starts.

For the direct coefficient-one route, the precise open step is the weaker
rounding (6.6): an exact mixed-frame middle-owner partition with aggregate
path-hitting holes \(o(W)\), while retaining long enough pieces that (6.9)
pays all interfaces. The exact band-SCD semigroup (7.7) is a sufficient
stronger route and is not logically necessary. No additional local cube
geometry is currently missing.
