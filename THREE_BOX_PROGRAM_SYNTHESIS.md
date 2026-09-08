# Three-chain programme: audited theorem ledger and exact frontier

## 1. Why this local problem matters

Let

\[
 P(p,q,r)=[0,p]\times[0,q]\times[0,r]
\]

with coordinatewise join, and let `g_3(p,q,r)` be the least length of a
sequence whose contiguous joins contain every nonzero point of this box.

Split the Boolean coordinates into three balanced blocks, take a symmetric
chain decomposition in each block, and form the resulting products of three
chains.  These boxes partition the Boolean lattice and their widths add
**exactly** to

\[
 W(k)={k\choose\lfloor k/2\rfloor}.
\]

Consequently, the uniform local estimate

\[
 g_3(p,q,r)\leq \operatorname{width}P(p,q,r)+O(p+q+r+1)       \tag{1.1}
\]

would imply

\[
 \nu(k)\leq W(k)+O\!\left({W(k)\over\sqrt{k}}\right)
          =(1+o(1))W(k).                                      \tag{1.2}
\]

The aggregation proof is exact; no witnesses cross between boxes and no
cross-box compatibility is required.  Thus (1.1), or a counterexample to
it, is a genuinely global target rather than another finite-`k` search.

## 2. Exact normalization

Arbitrary increment masks give no extra freedom locally.  Close each entry
coordinatewise to the least triple of chain prefixes containing it.  If an
interval originally joins to a box point `T`, every entry in that interval
is contained in `T`, so its closure is still contained in `T`; the interval
join remains exactly `T`.

Hence `g_3` is equivalently the shortest sequence of nonzero triples whose
contiguous **componentwise maxima** contain the entire box.

## 3. Proved lower bounds and the first exact obstruction

For rank numbers

\[
 m_s=[z^s](1+\cdots+z^p)(1+\cdots+z^q)(1+\cdots+z^r),
 \qquad L_s=\sum_{j=1}^{s-1}m_j,
\]

the rank-slack argument gives

\[
 g_3(p,q,r)\geq
 \max_s\{m_s+\tau_s\},
 \quad
 \tau_s=\min\left\{t:L_s\leq tm_s+{t+1\choose2}\right\}.    \tag{3.1}
\]

For the cube `[0,d]^3`, with width `M_d`, this yields

\[
 g_3(d,d,d)\geq M_d+{2d\over3}+O(1).                          \tag{3.2}
\]

Thus a linear boundary term is necessary; `width+o(d)` is impossible.
The independent shell argument also gives

\[
 g_3(p,q,r)\geq p+q+2r\qquad(p\geq q\geq r),                  \tag{3.3}
\]

and in particular `g_3(d,d,d)>=4d`.

The first nontrivial cube is now proof-producing exact:

\[
                         g_3(2,2,2)=10.                        \tag{3.4}
\]

A ten-term word is stored in `three_box_certificates/cube_2`; length nine
has a checked DRAT refutation.  Its rank-slack bound is only nine, so the
local analogue of `nu=B` already fails by one.

## 4. Necessary endpoint structure

Choosing one witness per target and grouping by common left and right
endpoints shows that every OR word induces two orthogonal chain partitions,
each with at most the word length many chains.  This gives a necessary
ordered-orthogonal-chain formulation.

For the cube `[0,m]^3`, two explicit hook constructions can be modified to
give orthogonal chain partitions

\[
                   |\mathcal L|=W_m,
             \qquad|\mathcal R'|=W_m+m.                       \tag{4.1}
\]

The double intersections of the parenthesized hook decompositions are
exactly

\[
 u_{i,j}=(j,i,i),\qquad
 v_{i,j}=(m-i,m-j,m-j),\qquad i+j<m.
\]

Cutting the right chains at `u_(i,j)` and rejoining prefix `(i,j)` to suffix
`(i+1,j)` removes every double, at a net cost of exactly `m` chains.

This proves that raw orthogonal-chain count is **not** an obstruction to
(1.1).  It is not yet sufficient: this particular rechain has cycles in
the endpoint-precedence constraints.  A successful pair must be ordered as
well as orthogonal, and must subsequently satisfy coordinate pinning.

The cycle obstruction is now quantitative.  There is one two-chain reversal
for every `(a,j)` with `a+j<m`, and their exact gap supports have congestion
at most two.  Therefore every precedence repair obtained by cutting the
displayed chain pieces needs at least

\[
                         {m(m+1)\over4}=\Theta(W_m)
\]

additional cuts across the two endpoint families.  In the **pure-refinement**
model, where the resulting pieces are not subsequently re-merged across old
chains, balancing those cuts against the initial `+m` right-family excess
already forces endpoint length

\[
                         n\geq W_m+{m^2+5m\over8}
                          =(7/6-o(1))W_m,
\]

before triangular bandwidth or pinning.  The quadratic cut theorem also holds
for every one-prefix/one-suffix rematching of the same pieces.  The `7/6`
length consequence does **not** cover a compensating global rechain after the
cuts, and simultaneous surgery of both endpoint partitions remains outside
the cap lemma.  The full proof, four-point certificates, and independent
scope audit are in
`THREE_BOX_NEAR_ORTHOGONAL_PRECEDENCE_OBSTRUCTION.md` and
`THREE_BOX_NEAR_ORTHOGONAL_PRECEDENCE_OBSTRUCTION_AUDIT.md`.

## 5. Complete two-sided shadow geometry

For the even cube `[0,2a]^3`, translate the middle layer to

\[
 H_a=\{(x,y,z):x+y+z=0,\ |x|,|y|,|z|\leq a\},
 \qquad |H_a|=M_a=3a^2+3a+1.
\]

Traverse the concentric radius-`s` hexagons as closed cycles and concatenate
them radially.  The resulting walk has length

\[
                         M_a+a.                                \tag{5.1}
\]

Every nonpositive-sum point of the translated cube is the coordinatewise
minimum of a contiguous walk interval, and every nonnegative-sum point is
the coordinatewise maximum of one.  The proof is an exact six-side arc
calculation plus one radial seam case.  Moreover the ordinary ring edges
bijectionally enumerate both layers adjacent to the middle.

This completely solves all-depth shadow enumeration with only `a` repeated
middle points.

## 6. Two rigorous no-go theorems

### 6.1 Fixed-delay rows are impossible

In `[0,2a]^3`, each of the three top chain increments occurs in exactly
`a+1` middle points, and no middle point contains two of them.  Every delay
allowed by the rank-slack lower bound is at least `a+1`.  The fixed-window
run criterion would force all three short, disjoint incidence supports to
touch one of only two row boundaries.  Therefore no permutation of the
middle layer can be a fixed-delay row at any universally feasible delay.

Any proof of (1.1) must use genuinely variable witness intervals.

### 6.2 Contiguous concentric rings cannot be that variable band

Let central witnesses be ordered in complete radius-ring blocks and let

\[
 I_i=[i+\alpha_i,i+\beta_i],
 \qquad 0\leq\alpha_1\leq\cdots\leq\alpha_L\leq D,
 \quad 0\leq\beta_1\leq\cdots\leq\beta_L\leq D,
\]

where `D=O(a)`.  For an internal coordinate 1-run `[u,v]`, factorability
forces the exact separation inequality

\[
                  r_{u-1}+2\leq\ell_{v+1}.                    \tag{6.1}
\]

On every complete hexagonal ring, two positive extreme-coordinate sides
are internal runs of only `s+1<=a+1` vertices, and such a run occurs after
only `O(a)` further middle occurrences.  Charging (6.1) gives

\[
              \sum_i(r_i-\ell_i)\leq3a^3+O(a^2).              \tag{6.2}
\]

The exact avoidance ledger then bounds the number of physical intervals
which contain no complete middle witness by the same leading term.  But the
lower half contains

\[
                         4a^3+O(a^2)                           \tag{6.3}
\]

targets.  Hence **every** width-plus-perimeter monotone band whose central
order consists of contiguous complete rings is impossible, irrespective of
labels or pinning.

This includes outward/inward ring order, arbitrary ring permutations,
orientations and cuts, and `O(a)` repetitions.  It does not include a true
cross-radius interleaving.

A later unrestricted anti-mixing theorem narrows that exception.  If
`D=N-M_s` and `H` is the mesh of the internal runs of the three extreme
increments in the selected middle-target order, then

\[
                         HD\ge (1/2-o(1))s^3.
\]

Thus `D=O(s)` forces `H=Omega(s^2)`: random and every certified
low-discrepancy cross-radius weave are impossible.  This still leaves highly
phase-separated interleavings.  Applying the theorem to nested subcubes gives
one quadratic-desert requirement in each induced witness order, but does not
prove that those deserts physically align.

## 7. Exact frontier

The three-chain reduction survives, but its first two canonical
realizations are now completely classified:

* the fixed middle row fails because of three rare coordinates;
* the perfect concentric shadow walk fails as a monotone band because its
  short extreme runs are too dense;
* the near-minimum orthogonal hook pair clears raw chain count but its first
  rechain fails endpoint precedence.

The next theorem must therefore take one of two precise forms.

1. **Interleaved-radius band theorem.**  Order middle points by weaving arcs
   from different radii so that a factorable `O(a)` monotone band leaves at
   least `4a^3+O(a^2)` middle-avoiding intervals, while retaining complete
   upper shadows; then solve lower Hall and pinning.
2. **Ordered orthogonal-chain theorem.**  Construct two orthogonal chain
   partitions with `W_m+O(m)` chains whose incidence edges admit a triangular
   endpoint layout respecting both within-chain orders, followed by an exact
   coordinate pinning rule.

Either theorem, with a linear local error, proves the asymptotically sharp
global result (1.2).  Conversely, an order-independent obstruction forcing
`Omega(W_m)` extra chains or destroying `Theta(a^3)` lower interval capacity
would disprove the entire fixed-three-box route.
