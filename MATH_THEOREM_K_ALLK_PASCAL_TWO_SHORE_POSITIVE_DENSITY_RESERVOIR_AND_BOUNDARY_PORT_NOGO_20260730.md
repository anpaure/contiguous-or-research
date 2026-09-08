# Pascal two-shore positive-density reservoirs, exact shadow triangles, and the boundary-port no-go

Date: 2026-07-30  
Lane: K, pure-mathematics all-`k` construction lane  
Status: unconditional local construction and obstruction theorems; conditional `B(k)+O(k)` compiler theorem. A global PBBS/Pascal collision-balancing braid is not proved.

## 0. Verdict

The positive-density compiler gate from the preceding report has a genuine
constructive solution at the levels of phase, local physical cells, run
geometry, and scalar density.

There are four exact advances.

1. **Shadow-collar dictionary.**  In the maximal depth-`d` erosion, the
   `binom(d+1,2)` subintervals of a full `d`-collar are exactly the complete
   lower-shadow triangle crossing one middle transition: at depth `q` there
   are exactly `q` crossing flag occurrences.  Keeping every run-boundary
   core makes the overwrite transparent to every interval not wholly inside
   one collar.
2. **Triangular Pascal phase law.**  If a new-coordinate sector trace has
   `s` positive runs, every run transfers exactly `binom(e+1,2)` short
   physical cells between the two phase shores of its depth-`e` controller.
   For an odd-to-even Pascal step the resulting scalar phase demands can
   always be met with only `O(e^2)=O(k)` phase defect.  This is a deterministic
   trace construction, not an existence proof for the full Johnson braid.
3. **Two-shore guarded reservoir.**  For odd `k=2m+1`, any resident
   generalized Pascal factor admits explicit `z`-positive and `z`-negative
   guarded collar banks.  For every fixed

   \[
   4\Phi(-\sqrt{\pi/2})<\alpha<1,                  \tag{0.1}
   \]

   collars of maximum length `floor(alpha d)` contain more deep collar-cell
   occurrences on each shore than there are deep targets on that shore;
   those occurrences are injective within each collar.  This is total
   capacity, not rankwise coverage.  In fact the uniform maximal-base choice
   misses `Theta(Wd)` low-rank targets, so a rank-stratified base schedule is
   necessary.  The collars preserve every derivative row from depth
   `floor(alpha d)` through `d`, including the scarce facet shell.
4. **Boundary-pair obstruction.**  Raw minimum-run endpoints do not furnish
   a port-captured Hall system.  A three-candidate fork forces the same
   candidate to use two different singleton seam ports.  The complete
   complementary-interval conflict graph has graphic rank exactly `dW`.
   Thus target-independent interval colours collapse to only
   `binom(d+1,2)` ports and have Hall defect `Lambda-O(k)`, not `O(k)`.

The construction stops at one exact, non-scalar condition.  Collar bases
must first be distributed across ranks; then labels from different collars
must cover the two deep target shores with only `O(k)` excess collision, and
every shallow flag in a mutable collar triangle must have an outside
occurrence or be recreated by a correlated seam triangle.  Equivalently,
the final word must satisfy

\[
                         C_{<}(A)+R_{=}(A)
                         \le \sigma+O(k).            \tag{0.2}
\]

Here `C_<(A)` is strict-lower collision excess, `R_=(A)` is rank-middle
short-window waste, and `sigma` is deadline slack.  Under (0.2), the explicit
reservoir gives `B(k)+O(k)`; equality with `sigma` gives coefficient one.

This remaining collision/shadow-copy statement is not proved for PBBS or
Pascal factors.  Consequently this note does not improve the unconditional
`O(sqrt(log k))` approximation from handoff item 1977.  It proves that the
missing resource is neither scalar density nor boundary capacity: it is a
nonlocal, target-dependent, all-depth correlation theorem.

## 1. Fixed chronology notation

Put

\[
 r=\lceil k/2\rceil,
 \qquad W={k\choose r},
 \qquad \Lambda=\sum_{s=1}^{r-1}{k\choose s},       \tag{1.1}
\]

and

\[
 d=\min\{j\ge0:jW+{j+1\choose2}\ge\Lambda\},
 \qquad B(k)=W+d,
 \qquad \sigma=dW+{d+1\choose2}-\Lambda.            \tag{1.2}
\]

Let `T=(T_0,...,T_(W-1))` be a strict depth-`d`-resident rank-`r`
Johnson chronology.  Its linearly truncated maximal erosion is

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i,
 \qquad 0\le p<W+d.                                  \tag{1.3}
\]

At every source position put

\[
 F_p=(P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1}),\tag{1.4}
\]

omitting nonexistent endpoint terms.  The run-boundary theorem gives

\[
                         \varnothing\ne F_p\subseteq A_p              \tag{1.5}
\]

for every nonzero `A<=P` with `D^dA=T`.

For a source interval `I`, write

\[
                         F(I)=\bigcup_{p\in I}F_p,
 \qquad P(I)=\bigcup_{p\in I}P_p.                   \tag{1.6}
\]

All exact collar statements below have clean cyclic versions.  In the
linear version a complete collar is placed at least `d` owner positions from
either opening; the two ramps contribute only `O(d^2)=O(k)` short cells.

## 2. The exact shadow-collar triangle

For `1<=q<=d`, define the depth-`q` lower flag ending at owner `s` by

\[
                         L_q(T)_s=\bigcap_{i=s-q}^{s}T_i.               \tag{2.1}
\]

### Theorem 2.1 (erosion/dilation flag identity)

Whenever `0<=s-q<=s<=W-1`, one has

\[
 \boxed{
 \bigcup_{u=0}^{d-q}P_{s+u}=L_q(T)_s.}               \tag{2.2}
\]

For a strict Johnson chronology, the common set has rank exactly `r-q`.

#### Proof

Every erosion window defining `P_(s+u)`, `0<=u<=d-q`, contains the owner
interval `[s-q,s]`, proving the forward inclusion in (2.2).

For the reverse inclusion, fix `x in L_q(T)_s` and let `[a,b]` be the
positive `x`-run containing `[s-q,s]`.  If `a=0`, take `u=0`; if `b=W-1`,
take `u=d-q`.  Otherwise residence gives `b-a+1>=d+1`, and

\[
 [a+d-s,b-s]\cap[0,d-q]\ne\varnothing.              \tag{2.3}
\]

For an integer `u` in this intersection, the complete erosion window for
`P_(s+u)` lies in `[a,b]`, so `x in P_(s+u)`.

Across the `q` Johnson transitions, the deleted coordinates are distinct
members of the first owner.  A newly inserted coordinate deleted again in
the same window would have an internal positive run of length at most
`q<=d`, contrary to residence.  Hence exactly `q` coordinates are lost and
the rank is `r-q`. QED.

Fix an interior cut `(c,c+1)` and its full source collar

\[
                         J_c=[c+1,c+d].              \tag{2.4}
\]

For `1<=q<=d`, the `q` subintervals of `J_c` of length `d-q+1` are

\[
 I_{q,j}=[c+j,c+j+d-q],\qquad1\le j\le q.           \tag{2.5}
\]

By (2.2),

\[
 P(I_{q,j})=\bigcap_{i=c+j-q}^{c+j}T_i.             \tag{2.6}
\]

These are exactly the `q` depth-`q` flag occurrences crossing the cut.
They need not be `q` distinct masks.  Summing over `q` proves the exact
triangle count

\[
                         \sum_{q=1}^d q={d+1\choose2}.                 \tag{2.7}
\]

For a collar of length `ell<=d`, its mutable depth-`q` capacity is

\[
                         (\ell-d+q)^+.                \tag{2.8}
\]

### Theorem 2.2 (run-boundary transparency)

Let `J_1,...,J_t` be interval blocks separated by at least one genuinely
untouched position.  Define `A=P` outside their union and assume

\[
                         F_p\subseteq A_p\subseteq P_p                \tag{2.9}
\]

inside every block.  Then

\[
 \boxed{A(I)=P(I)}                                    \tag{2.10}
\]

for every source interval `I` not wholly contained in one block.

#### Proof

Suppose `x in P(I)` but `x notin A(I)`, and take a positive `P`-run `C`
of `x` meeting `I`.  No finite endpoint of `C` can lie in `I`, since `x`
belongs to `F_p` and survives there.  Therefore `C` contains all of `I`.
Every position of `I` must be edited; connectedness of `I` and the untouched
separator then force `I` to lie in one block, a contradiction.  The reverse
inclusion follows from `A<=P`. QED.

In particular, blocks of length at most `d` preserve `D^dA=T`, every middle
and arbitrary upper interval witness, and every lower occurrence outside the
internal collar triangles.  This is stronger than a generic seam-count
statement: all external labels are literally unchanged.

Let

\[
 \mathcal M=\{I:I\subseteq J_j\text{ for some }j\},
 \qquad \mathcal U=\{P(I):I\notin\mathcal M\}.       \tag{2.11}
\]

The final lower labels are exactly

\[
                         \mathcal U\cup
                         \{A(I):I\in\mathcal M\}.   \tag{2.12}
\]

Since `A(I) subseteq P(I)`, a changed depth-`q` flag occurrence drops to a
strictly deeper rank; it cannot silently turn into a different rank-`(r-q)`
target.  Hence every shallow target whose selected occurrences all lie in
the collar triangle must be retained locally or recreated elsewhere.

## 3. Exact triangular phase law for an odd-to-even Pascal step

Let a cyclic binary sector trace have `G` zero states, `O` one states, and
`s` one-runs.  Assume every one-run has length at least `e+1`, and put the
new coordinate `z` exactly on its maximal depth-`e` source controller.
Write

\[
                         C_e={e+1\choose2}.           \tag{3.1}
\]

### Theorem 3.1 (phase-cell law)

Among all cyclic source intervals of lengths `1,...,e`, the numbers omitting
and containing `z` are respectively

\[
 \boxed{C_0=eG+sC_e,
        \qquad C_1=eO-sC_e.}                         \tag{3.2}
\]

If disjoint collars of lengths `ell_j<=e` lie wholly inside positive
controller runs, and each collar is flanked on both cyclic sides by a
retained `z` position, then deleting `z` on those collars gives

\[
 C_0=eG+sC_e+\sum_j{\ell_j+1\choose2},
 \qquad C_1=e(G+O)-C_0.                              \tag{3.3}
\]

#### Proof

A middle one-run of length `L` erodes to a controller run of length `L-e`.
The following middle zero-gap of length `g` becomes a controller zero-gap of
length `g+e`.  Such a gap contains

\[
 \sum_{t=1}^e(g+e-t+1)=eg+C_e                      \tag{3.4}
\]

short intervals.  Summing `g` over the `s` gaps gives `eG+sC_e`; subtract
from all `e(G+O)` cyclic short intervals to get `C_1`.  A deleted collar
with retained `z` on both sides is a new isolated zero component, so it
contributes precisely its number of subintervals and has no cross-term. QED.

Thus every sector-run boundary transfers exactly `C_e` physical phase cells.
This is the literal triangular form of the odd/even Pascal-shadow braid.

Now take an odd parent of dimension `2m-1`. Put

\[
 W={2m-1\choose m},
 \qquad \Lambda=2^{2m-2}-1,
 \qquad a=dW-\Lambda.                                \tag{3.5}
\]

For the even child,

\[
 W'=2W,
 \qquad \Lambda'=2\Lambda-W+1,                      \tag{3.6}
\]

and, for all sufficiently large `m`, its deadline `e` belongs to
`{d-1,d}`. Direct substitution into the deadline inequalities gives

\[
 e=d-1
 \quad\Longleftrightarrow\quad
 2a\ge W+1-{d\choose2}.                              \tag{3.7}
\]

In a balanced Pascal tag trace, `G=O=W`.  The no-`z` and `z` lower target
demands are

\[
                         L_0=\Lambda,
 \qquad L_1=\Lambda-W+1.                             \tag{3.8}
\]

If `Q=sC_e+sum_j binom(ell_j+1,2)`, scalar phase feasibility is exactly

\[
 (d-e)W-a\le Q\le(e-d+1)W+a-1.                      \tag{3.9}
\]

The even-child capacity inequality implies that the left endpoint exceeds
the right endpoint by at most `C_e`.  Therefore

\[
 s=\max\left\{1,
 \left\lceil{\max(0,(d-e)W-a)\over C_e}\right\rceil
 \right\}                                             \tag{3.10}
\]

leaves fewer than `3C_e=O(k)` cyclic phase cells uncovered.  Linear opening
changes only `O(C_e)` boundary cells, so the phase defect remains `O(k)`.

The required binary trace exists at the scalar level.  If `e=d`, deadline
minimality gives `s=O(1)`.  If `e=d-1`, (3.7) gives

\[
 s\le {W\over2C_e}+O(1),
 \qquad s(e+1)\le {W\over e}+O(e)<W                 \tag{3.11}
\]

for all sufficiently large `m`.  Hence the `W` one-states can be divided
into `s` runs of length at least `e+1`, and the `W` zero-states into `s`
nonempty gaps.

This proves an exact scalar trace construction.  It does **not** prove that
there is a resident Johnson factor having the chosen trace and all old-label
shadow/compiler properties.  Indeed, the naive single forward-`T` block
followed by one reverse-facet block is deck-exact but not resident: the first
deleted old coordinate or the last inserted old coordinate has a singleton
child run at one seam.  Multiple Pascal runs are essential.

There is no scalar q1 conflict with (3.10).  A two-sector cycle with `s`
runs has `W-s` `AA` edges and `W-s` `BB` edges.  Hence q1 coverage requires

\[
 s\le W-{2m-1\choose m-2}={2W\over m+1}.             \tag{3.12}
\]

On a deadline-drop step, (3.7) and `e^2~pi m/4` give

\[
 s\le {W\over2C_e}+O(1)
   =\left({4\over\pi}+o(1)\right){W\over m}
   <{2W\over m+1}.                                   \tag{3.13}
\]

Thus scalar phase and q1 edge counts are compatible; literal cross-depth
routing is the obstruction.

## 4. Explicit two-shore guarded reservoir

We now work in odd dimension

\[
 k=2m+1,
 \qquad r=m+1,
 \qquad C=\operatorname{Cat}_m,
 \qquad W=(2m+1)C.                                   \tag{4.1}
\]

Assume `T` is a cyclic Hamilton chronology which is q1-exact, positively
`d`-resident, and has the generalized Pascal two-shore signature.  Assume
also that it comes with a declared linear opening which retains every
required upper target (or an explicitly charged `O(k)` upper boundary
ledger).  Fix a coordinate `z`; the cycle meets both `z` shores.  The exact
shore counts are

\[
 |A|=(m+1)C,
 \quad |B|=mC,
 \quad AA=mC,
 \quad AB+BA=2C,
 \quad BB=(m-1)C.                                    \tag{4.2}
\]

There are exactly `C` positive `z`-runs.  In the cyclic maximal erosion `P`,
the `z`-positive and `z`-negative source supports have sizes

\[
                         (m+1-d)C,
 \qquad (m+d)C.                                      \tag{4.3}
\]

Put `b=r-d`, fix a constant `alpha` satisfying (0.1), and let

\[
                         \ell=\lfloor\alpha d\rfloor.                 \tag{4.4}
\]

Within every source run on each shore, reserve separator sites and partition
the remainder into collars of lengths at most `ell`.  If

\[
 n=q(\ell+1)+s,
 \qquad0\le s\le\ell,                                \tag{4.5}
\]

the collar subinterval capacity is

\[
 f_\ell(n)=q{\ell+1\choose2}+{s+1\choose2}
 \ge {\ell n\over2}-{(\ell-1)^2\over8}.             \tag{4.6}
\]

The inequality follows by minimizing
`s(s+1-ell)/2` over `0<=s<=ell`.

On a collar `J` of size `s<=ell`, choose

\[
 K_J\subseteq\bigcap_{p\in J}P_p,
 \qquad 0\le |K_J|\le b-3\ell-1,                    \tag{4.7}
\]

with `1<=|K_J|` and `z in K_J` on the positive shore, and `z notin K_J`
on the negative shore.
The flat cyclic erosion has rank `b` and loses at most one coordinate per
step, so

\[
 \left|\bigcap_{p\in J}P_p\right|\ge b-(s-1).        \tag{4.8}
\]

The eventual inequality `b>=3ell+2` therefore makes every displayed base
size possible; on the positive shore a nonempty base may be chosen to
include `z`.  Since `|F(J)|<=2s`, the lists

\[
                         P_p\setminus(K_J\cup F(J))                  \tag{4.9}
\]

have at least `s+1` elements for all sufficiently large `m`.  Hall gives
distinct markers `w_p` in these lists.  Set

\[
                         A_p=K_J\cup F_p\cup\{w_p\}.                  \tag{4.10}
\]

For every nonempty `I subseteq J`,

\[
 A(I)=K_J\cup F(I)\cup\{w_p:p\in I\},               \tag{4.11}
\]

and the marker subset recovers `I`.  The collar therefore supplies exactly
`binom(s+1,2)` locally distinct labels, all of rank at most

\[
 |K_J|+3s\le b-1.                                    \tag{4.12}
\]

### Theorem 4.1 (total two-shore reservoir capacity)

Let `K_A,K_B` denote the total numbers of collar intervals, hence deep-label
occurrences, on the two shores.  Labels are injective within each collar;
no cross-collar injectivity is asserted. Then

\[
 K_A\ge {\ell\over2}(m-d)C-{C(\ell-1)^2\over8},       \tag{4.13}
\]

\[
 K_B\ge {\ell\over2}(m+d-1)C-{C(\ell-1)^2\over8}.   \tag{4.14}
\]

The deep target demands on the two shores are

\[
 D_+=\sum_{j=0}^{m-d-1}{2m\choose j},
 \qquad
 D_-=\sum_{j=1}^{m-d}{2m\choose j}.                 \tag{4.15}
\]

With `a_0=sqrt(pi/2)`, one has

\[
 {K_A\over Wd},{K_B\over Wd}\longrightarrow{\alpha\over4},
 \qquad
 {D_+\over Wd},{D_-\over Wd}\longrightarrow\Phi(-a_0).             \tag{4.16}
\]

Thus (0.1) implies the scalar occurrence surpluses

\[
                         K_A-D_+=\Omega_\alpha(Wd),
 \qquad K_B-D_-=\Omega_\alpha(Wd).                  \tag{4.17}
\]

#### Proof

Eroding the `C` positive runs gives (4.3).  Reserve one boundary site per
run; the usable totals are `(m-d)C` and `(m+d-1)C`.  Apply (4.6) in each
run and sum the error over `C` runs to obtain (4.13)--(4.14).

The central binomial estimate gives

\[
 d=\left({\sqrt\pi\over2}+o(1)\right)\sqrt m,
 \qquad Wd\sim2^{2m},                                \tag{4.18}
\]

and the binomial central limit theorem at displacement `d` gives the two
limits in (4.16).  The `O(C ell^2)=O(W)` separator/rounding loss is lower
order than `Wd`. QED.

The two shores cannot collide with one another because every positive-shore
label contains `z` and every negative-shore label omits it.  Equations
(4.13)--(4.17) are therefore a literal positive-density two-shore reservoir,
but they remain total occurrence arithmetic across ranks.

These displayed counts are for the cyclic controller.  After choosing the
declared linear opening and excluding its `d`-halo, each lower bound loses at
most `O(d^2)=O(k)` cells.  This is negligible in (4.16)--(4.17) and is
charged explicitly in PCB.

### Proposition 4.2 (uniform maximal bases miss a Gaussian tail)

If every collar uses the maximal base size

\[
                         |K_J|=b-3\ell-1,            \tag{4.19}
\]

then every output has rank at least `b-3ell`.  Consequently the positive
and negative shores miss, respectively, at least

\[
 \sum_{j=0}^{m-d-3\ell-1}{2m\choose j},
 \qquad
 \sum_{j=1}^{m-d-3\ell}{2m\choose j}.               \tag{4.20}
\]

For fixed `alpha`, each is

\[
 \left(\Phi(-(1+3\alpha)\sqrt{\pi/2})+o(1)\right)Wd
 =\Theta_\alpha(Wd).                                 \tag{4.21}
\]

Thus the uniform-base atlas cannot have `O(k)` defect.  Any viable
positive-density construction must distribute base sizes across the deep
rank range before solving cross-collar collision Hall.

#### Proof

Every nonempty collar interval contains a private marker outside `K_J`, so
its label has rank at least `|K_J|+1=b-3ell`.  Count all deep targets below
that threshold separately on the two `z` shores.  The central limit theorem
at displacement `(1+3alpha)d` gives (4.21). QED.

### Theorem 4.3 (protected derivative shells)

For the resulting antecedent `A`,

\[
 \boxed{D^hA=D^hP\qquad(h\ge\ell).}                  \tag{4.22}
\]

Consequently the first `d-ell` lower flag shells, including the facet shell,
are unchanged.

#### Proof

Every coordinate-deletion component lies in one collar and has length at
most `ell`; all finite run endpoints in `F_p` survive.  The run-component
proof applied to a window of length `h+1>=ell+1` gives equality in every
coordinate.  Under the dictionary (2.2), lower depth `q` uses source length
`d-q+1`; this is at least `ell+1` for `q<=d-ell`. QED.

## 5. Exact collision and lost-shadow ledger

Local injectivity is not global target coverage.  For a deep target `S` on
one shore, let `mu_+(S)` or `mu_-(S)` be its number of collar occurrences,
and define

\[
 C_\pm=\sum_S(\mu_\pm(S)-1)^+,
 \qquad H_\pm=|\{S:\mu_\pm(S)=0\}|.                 \tag{5.1}
\]

Because every collar label lies in the declared deep target shore,

\[
 \boxed{H_+=C_+-(K_A-D_+),
 \qquad H_-=C_--(K_B-D_-).}                          \tag{5.2}
\]

Thus the excess capacity in (4.16) is useful exactly when cross-collar
collisions exceed the unavoidable pigeonhole amount by only `O(k)`.

There is a second charge.  A mutable collar interval formerly carried the
shallow flag given by (2.6); its new label has deeper rank by (4.11).  Let
`H_tri` be the number of such shallow targets having neither an outside
`P`-occurrence nor a declared replacement seam occurrence.  Transparency
proves that there is no other shallow disruption.

The exact global form is especially concise.  For every strict lower target
let `mu_A(S)` be its short-interval multiplicity and put

\[
 C_<(A)=\sum_{1\le|S|<r}(\mu_A(S)-1)^+,             \tag{5.3}
\]

while `R_=(A)` is the number of short intervals whose union has rank `r`.
Since the number of short cells is `Lambda+sigma`, the number `H(A)` of
missing strict lower targets satisfies

\[
 \boxed{H(A)=C_<(A)+R_=(A)-\sigma.}                 \tag{5.4}
\]

### Corollary 5.1 (explicit reservoir-to-`B+O(k)` theorem)

Assume the resident factor and upper-complete opening package in Section 4
exist, with at most `C_U k` charged upper-boundary targets, and choose the
explicit two-shore reservoir above.  If its cross-collar choices and any
declared shadow braid satisfy

\[
                         C_<(A)+R_=(A)\le\sigma+C_0k                 \tag{5.5}
\]

for a fixed constant `C_0`, then

\[
                         \nu(k)\le B(k)+(C_0+C_U)k.   \tag{5.6}
\]

If equality with `sigma` holds and `C_U=0`, then `nu(k)=B(k)`.

#### Proof

Equation (5.4) gives at most `C_0k` lower holes.  Theorem 4.3 with `h=d`
gives the middle row; the opening package misses at most `C_Uk` upper
targets.  Append both charged families.  At zero lower and upper defect the
deadline lower bound gives equality. QED.

The exact missing constructive lemma is now:

> **Pascal collar balance (PCB).** Choose a rank-stratified distribution of
> bases, the markers, and correlated seam triangles in the explicit
> reservoir so that
> `H_++H_-+H_tri=O(k)`, equivalently (5.5), while retaining the declared
> resident factor and upper witnesses.

This is substantially narrower than constructing a compiler from scratch.
Every local atom, density inequality, phase count, central row, upper row,
and early shallow shell is already discharged.

## 6. Why a bulk BB bank and an all-depth braid are forced

For the generalized odd Pascal factor, the cross channel has exactly `2C`
`AB/BA` boundaries.  The number of short intervals of lengths at most `d`
crossing those boundaries is at most

\[
 2C\sum_{t=1}^d(t-1)+O(d^2)
   =Cd(d-1)+O(d^2)=O(W),                             \tag{6.1}
\]

where the `O(d^2)` term covers a chosen linear opening, whereas

\[
 D_++D_-=(2\Phi(-\sqrt{\pi/2})+o(1))Wd=\Theta(Wd). \tag{6.2}
\]

Hence an `O(d)` halo around the ordinary odd/even cross channel is
asymptotically negligible.  A genuine bulk bank on each pure shore is
necessary; the cross edges alone cannot be the positive-density compiler.

The required total number of full `d`-collars has the sharp scalar scale

\[
 {D_++D_-\over {d+1\choose2}}
   =(4\Phi(-\sqrt{\pi/2})+o(1)){W\over d}.           \tag{6.3}
\]

Their support density is the constant in (0.1).  Thus the reservoir is at
the correct scale, not merely within an order of magnitude.

There is a stronger cumulative reason that a bulk `BB` bank is unavoidable
inside the fixed flat controller.  Call a short cell **AA-pure** when every
flat erosion position in it belongs to the `z`-positive support.  Put

\[
 h=\lfloor\sqrt{m\log2}\rfloor,
 \quad B_h=\sum_{q=1}^h(W+q),
 \quad R_h=\sum_{q=1}^h{2m+1\choose m+1-q},          \tag{6.4}
\]

and

\[
 D_{\rm deep}=\sum_{s=1}^{m-d}{2m+1\choose s}.      \tag{6.5}
\]

### Theorem 6.1 (cumulative AA-only obstruction)

Even with arbitrary reassignment among rank rows, the number of deep targets
which can use AA-pure cells is at most

\[
 B_h-R_h+(d-h)(m+1)C+O(d^2).                         \tag{6.6}
\]

Consequently at least

\[
 (J+o(1))W\sqrt m,
 \qquad
 J=\int_{\sqrt{\log2}}^{\sqrt\pi/2}
       \left({1\over2}-e^{-x^2}\right)dx>0           \tag{6.7}
\]

deep targets require non-AA-pure cells.  After removing the `O(W)` mixed
halo from (6.1), the same asymptotic lower bound holds for genuinely
BB-bulk cells.  A separated BB-collar construction therefore needs support

\[
 L_B\ge\left({2J\over\sqrt\pi/2}+o(1)\right)W.       \tag{6.8}
\]

#### Proof

A rank-`(r-j)` target needs a flat source interval of length at least
`d-j+1`, because a length-`t` union of the rank-`b` erosion path has rank at
most `b+t-1`.  Hence the top `h` lower ranks consume `R_h` distinct cells
among the `B_h` longest row classes.  At most `B_h-R_h` cells in those rows
remain for deeper targets.  Each of the other `d-h` length classes has at
most `|A|=(m+1)C` AA-pure starts, proving (6.6).

Uniformly for `q=x sqrt(m)`,

\[
 { {2m+1\choose m+1-q}\over W}\longrightarrow e^{-x^2}.             \tag{6.9}
\]

Also

\[
 {D_{\rm deep}\over W\sqrt m}
 \longrightarrow
 \int_0^{\sqrt\pi/2}(1-e^{-x^2})\,dx.               \tag{6.10}
\]

Subtracting the limit of (6.6) gives exactly (6.7).  Finally a collar
support of size `L_B` contains at most `(d+1)L_B/2` internal short cells;
use `d/sqrt(m)->sqrt(pi)/2` to obtain (6.8). QED.

This is a cumulative prefix cut, not a rowwise matching assumption.  Its
scope is the fixed maximal-controller architecture; a nonflat cross-seam
word lies outside it.

At depth `q`, each full collar changes exactly `q` baseline flag
occurrences, by (2.6).  A new middle seam also has exactly `q` crossing
depth-`q` windows.  Scalar seam capacity is therefore perfect at every
depth, but the labels must be correlated.  Minimum-run boundary pairs settle
only the first endpoint/facet incidence; they do not imply the simultaneous
`q=2,...,d` label identities.

## 7. Boundary-pair ports fail already at arity two

We now prove that the minimum-run boundary pairs cannot themselves be the
port system in Corollary 4.2 of the preceding report.

Let the source positions be `0,...,n-1`, `n=W+d`, and give an interval
`I=[a,b]` only its two exterior seam ports

\[
                         \partial I=\{a-1,b\}.       \tag{7.1}
\]

### Theorem 7.1 (stable boundary fork)

Assume `r>=2d+6`.  For every bulk interval

\[
 I=[a,a+d-1]=[a,b],
 \qquad a\ge2,
 \qquad b+2<n,                                       \tag{7.2}
\]

there are candidates `v_-` on `{a-1}`, `v` on `I`, and `v_+` on `{b+1}`
in three distinct non-singleton, non-facet target parts such that

\[
                         \{v_-,v\},\qquad\{v,v_+\}                  \tag{7.3}
\]

are minimal conflicts.  Consequently no nonempty lists

\[
                         R(w)\subseteq\partial I(w)                  \tag{7.4}
\]

capture every pair conflict.

#### Proof

Put

\[
 C_0=\bigcap_{p=a-2}^{b+2}P_p,                      \tag{7.5}
\]

using only existing endpoint terms.  Consecutive erosion states lose at
most one coordinate, so

\[
                         |C_0|\ge r-2d-3\ge3.        \tag{7.6}
\]

Every member of `C_0` is absent from the mandatory cores on positions
`a-1,...,b+1`.  Choose distinct `y,u,z in C_0` and set

\[
 S=F(I)\cup\{u\},
 \quad S_-=F_{a-1}\cup\{z\},
 \quad S_+=F_{b+1}\cup\{u,z\}.                      \tag{7.7}
\]

The intersections with `C_0` distinguish these labels.  Their ranks are at
most `2d+1,3,4`, hence are strictly between the singleton and facet layers,
and all omit `y`.  Each pair of source intervals in (7.3) partitions a
central window of length `d+1` and deletes every allowed `y`-occurrence.
Unary compatibility makes the two conflicts minimal.

For two nonempty port lists, failure of an SDR forces both lists to be the
same singleton.  The left conflict forces `R(v)={a-1}`, while the right
conflict forces `R(v)={b}`.  These are different, a contradiction. QED.

There are `floor((W+d)/(d+4))` disjoint fork halos.  Thus an endpoint-list
pruning must delete a candidate from, or physically disturb, `Omega(W/d)`
bulk neighborhoods.

### Theorem 7.2 (exact complementary-interval graph)

Let `Gamma_(W,d)` have all source intervals of lengths `1,...,d` as
vertices.  Join two when they are consecutive, disjoint, and together form
a length-`d+1` central window.  Then `Gamma_(W,d)` is a path forest and

\[
 |V|=dW+{d+1\choose2},
 \qquad |E|=dW,
 \qquad \kappa(\Gamma)={d+1\choose2}.                \tag{7.8}
\]

Hence its graphic rank is exactly `dW`.

#### Proof

An interval of length `t` is paired with an adjacent interval of length
`d+1-t`.  Orient every edge from the left interval to the right interval.
Every vertex has indegree and outdegree at most one, and after two steps an
interval of the same length is shifted right by `d+1`; a cycle is impossible.
There is one edge for each of the `W` central windows and each of its `d`
splits.  The vertex count is the short-cell formula in (1.2), so a forest
has the stated number of components. QED.

Under `r>=2d+5`, every graph edge supports a physical minimal pair conflict.
Indeed, if consecutive intervals `I,J` partition `[a,a+d]`, intersect the
existing erosion states from `a-1` through `a+d+1`.  Their common stable core
has size at least

\[
                         r-d-(d+2)=r-2d-2\ge3.       \tag{7.9}
\]

It is disjoint from `F(I) union F(J)`.  Choose distinct stable coordinates
`y,u,z` and label the two intervals by `F(I) union {u}` and
`F(J) union {z}`.  Both labels are strict lower targets, both omit `y`, and
their intervals delete `y` from the central window.  Unary compatibility
makes the pair a minimal conflict.  The one-sided endpoint construction is
the same with nonexistent erosion terms omitted.

Therefore a target-independent singleton interval colour capturing all pair
conflicts is constant on every graph component and has at most
`binom(d+1,2)` colours.
Before scarce-part unit closure its target-port Hall defect, after `e`
omissions, is at least

\[
 \Lambda-e-{d+1\choose2}=dW-\sigma-e.               \tag{7.10}
\]

After unit closure one must use the rank of the surviving induced graph;
(7.9) is not asserted without a survival lemma.

A strict `W`-owner rank-`r` Johnson path has exactly

\[
                         W+r-1                                      \tag{7.11}
\]

positive coordinate runs: `r` initial runs and one birth at each transition.
Since deadline minimality gives

\[
                         \Lambda>(d-1)W+{d\choose2},                 \tag{7.12}
\]

a unit-capacity whole-run port system with `O(k)` defect requires average
port multiplicity at least `d-1-o(1)` per run.  One or two minimum-run ports
are therefore capacity-impossible.  Phase-refined `(run,offset)` ports and
nonlocal target-dependent ports remain open.

## 8. Pairwise base separation cannot solve the collision problem

Every guarded output in a collar differs from its chosen common base `K_J`
in at most `3d` coordinates.  It is tempting to prevent all cross-collar
collisions by requiring

\[
                         |K_I\mathbin\triangle K_J|>6d.               \tag{8.1}
\]

This cannot supply the required number of collars.

### Proposition 8.1 (Hamming-code ceiling)

Any family of subsets of `[k]` satisfying (8.1) has size at most

\[
 {2^k\over\sum_{i=0}^{3d}{k\choose i}}
 =o(W/d)                                               \tag{8.2}
\]

when `d=Theta(sqrt(k))`.

#### Proof

The Hamming balls of radius `3d` about the bases are disjoint, proving the
first inequality.  Moreover

\[
 \sum_{i=0}^{3d}{k\choose i}
 \ge {k\choose3d}
 =\exp(\Theta(\sqrt k\log k)),                       \tag{8.3}
\]

whereas `W/d=Theta(2^k/k)`.  Their ratio tends to zero. QED.

Thus the cross-collar step really requires Hall/absorption or a correlated
Pascal recursion; a globally collision-free code of bases is too sparse by
a superpolynomial factor.  This closes only robust pairwise Hamming-ball
separation: closer bases could still coordinate their sparse directed output
clouds without collision.

## 9. Exact remaining theorem and implication scope

The positive construction has reached the following precise boundary.

* The phase split is feasible with `O(k)` scalar defect.
* Both pure shores contain enough total physical, mandatory-core-safe deep
  occurrences at the exact positive density, with local injectivity inside
  each collar; their rankwise distribution remains open.
* Middle and upper targets, plus the first `d-ell` lower shells, survive
  literally.
* Ordinary cross halos, endpoint pairs, target-independent interval colours,
  and globally distance-separated bases are rigorously insufficient.

What remains is one physical theorem:

> **PCB(k).**  In one resident upper-complete PBBS/Pascal factor, choose the
> explicit two-shore collars and an all-depth correlated seam braid so that
> the global strict-lower excess satisfies
> `C_<(A)+R_=(A)<=sigma+O(k)`.

By Corollary 5.1,

\[
                         \mathrm{PCB}(k)
                         \Longrightarrow
                         \nu(k)\le B(k)+O(k).         \tag{9.1}
\]

The exact version with excess at most `sigma` proves `nu(k)=B(k)`.  A
version with `o(W)` excess proves asymptotic coefficient one.

No present PBBS theorem supplies the required resident generalized factor
and no present Pascal theorem supplies the collision/shadow-copy balance.
Accordingly no unconditional `B(k)+O(k)`, constant-factor, or coefficient-one
claim is made here.  The strongest unconditional all-`k` bound remains the
audited `O(sqrt(log k))W` construction.

## 10. Audit record

The shadow triangle and transparency theorem were independently proved
coordinatewise, including ramps, cyclic openings, occurrence-versus-mask
distinctions, and the exact mutable-depth count.  The boundary-fork and
interval-graph theorem were independently audited, including candidate
ranks, mandatory-core avoidance, zero-based endpoints, graph components,
and the pre/post-unit-closure scope.  The two-shore density and phase
constants received a separate adversarial audit.  It caught the forbidden
zero-run phase trace, the occurrence-versus-distinct-label distinction, the
rank-tail failure of uniform maximal bases, and the need for one literal
Hamilton/opening package; all corrections are incorporated above.

No SAT/CP solving, finite K16 search, web access, or heavy local or remote
computation was used.
