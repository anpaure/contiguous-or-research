# Portal braids and the linear-depth lower factor

## 1. Outcome

Put

\[
 P_m=[0,m]^4,\qquad R=2m-1,
 \qquad L_r=\{x\in P_m:|x|=r\}.
\]

Assume that the complementary-line portal programme succeeds on the upper
side: a near-once word on `L_R`, made from alternating coordinate-`{1,2}`
and coordinate-`{3,4}` segments, represents the required upper targets.

There are two rigorous conclusions about coupling that word to the lower
half.

1. **One factor step is compatible with the portal seams.**  Every
   nondegenerate sharp corner can be rounded by one additional rank-`R`
   point.  The rounded turn has distinct half-edge labels at all three of
   its internal vertices, does not change any old interval maximum, and is
   therefore eligible for `ARM_WORD_FACTOR_LIFT`.  The hard swapped-baseline
   catalogue needs only `O(q^2)` such points.  The full balanced catalogue
   can have labels with `A+B` much larger than `q`, but still needs at most
   `O(m^2)` points.  Thus the occurrence-by-occurrence factorization costs
   only surface order.  Complete coverage of the next lower layer requires
   the additional lower-edge condition (4.3); it is not implied by portal
   completeness alone.

2. **A densely alternating linked band cannot reach linear lower depth at
   near-width length.**  More generally, let a prescribed rank-`R` row have
   a strict coordinate peak at least once in every `H` positions.  If one
   monotone interval band realizes every occurrence of that row and the same
   physical word covers the whole strict lower ideal, then its physical
   slack `d` satisfies

   \[
   \boxed{
   d\ge {m^4+2m^3-m-2\over 2(3H+2m)}.}             \tag{1.1}
   \]

   In particular, `H=O(m)` forces `d=Omega(m^3)`.  Therefore a braid which
   alternates sharp line corners uniformly at line scale cannot be the
   central schedule of a width-plus-`o(m^3)` lower factor, even with
   variable witness widths and even when arbitrary non-core lower witnesses
   are allowed.

The second result is not a no-go for every portal construction.  It says
exactly how a successful construction must escape: cluster the sharp turns
and leave a factor reservoir with gaps of length `Omega(m^2)` when
`d=O(m^2)`, replace most sharp corners by nonsharp shared-pin transitions,
or abandon one linked occurrence-by-occurrence central band.  Merely
iterating the maximal arm factor does not work.

## 2. The two catalogues must be distinguished

For one coordinate orientation, a portal seam has two high coordinates
and two low coordinates.  Write its high deficits as `(A,B)` and put

\[
                         \delta=A+B.
\]

The hard-family construction in
`COMPLEMENTARY_SEAM_RECTANGLE_TILING.md` uses the swapped baseline and only

\[
                         A+B\le q-1.                \tag{2.1}
\]

It therefore has

\[
 4\left({q(q+1)\over2}-1\right)
      =2q(q+1)-4                                      \tag{2.2}
\]

nondegenerate seam labels, after excluding `(A,B)=(0,0)` in the four
orientations.

The balanced tie-strip catalogue is larger.  It takes

\[
 c_0=\lfloor\delta/2\rfloor,
 \qquad d_0=\lceil\delta/2\rceil,                  \tag{2.3}
\]

and a demanded label can have `delta` far larger than `q`.  The audit's
example `(m,q,delta)=(8,2,5)` is a concrete warning.  Nevertheless every
legal central corner has `0<=A,B<=m-1`, so there are at most `m^2` labels
per orientation and at most

\[
                              4m^2                  \tag{2.4}
\]

overall.  One local repair per demanded seam is still surface order.

There is a useful algebraic invariant in the canonical demand graph.  A
seam `(A,B)` of even `delta` shares its `{1,2}` line, when that neighbouring
label is demanded, with `(A-1,B)` and shares its `{3,4}` line with
`(A,B+1)`.  The reverse moves apply from odd `delta`.  Consequently

\[
             \kappa=A-B+(\delta\bmod2)              \tag{2.5}
\]

is constant on every demand component.  The demanded-seam inequalities
are, for `delta=2r`,

\[
 A+r\le m,\qquad B+r\le m,
\]

and, for `delta=2r+1` and `q>=2`,

\[
 A+r+1\le m,\qquad B+r+1\le m.                    \tag{2.6}
\]

Along a fixed `kappa` these conditions cut out one consecutive interval.
Therefore the canonical balanced catalogue has exactly one path per
nonempty `kappa` class and only `O(m)` path components.  This stronger fact
has been proved and independently checked in
`BALANCED_LINE_DEMAND_BRAID.md` and
`BALANCED_LINE_DEMAND_BRAID_AUDIT.md`.

The simple component graph does not by itself solve physical ordering.
The same audit proves an `Omega(qm^2)` copy tax if the portal arms are
required simultaneously with their preferred intact easy-line blocks.
Thus the assumed near-once upper completion must already escape that
literal intact-line architecture.  The rounding lemma below applies to any
such completed physical braid; it does not assume the discredited intact
line realization.

## 3. A one-point rounding of a sharp portal corner

The following lemma is the positive coupling step.

### Lemma 3.1 (rounded complementary corner)

Let `h_1,h_2,l_1,l_2` be the four coordinate positions, with the first two
the high coordinates.  Let `Z in L_(R+1)` and assume

\[
 X_0=Z-e_{h_2},\qquad Y_0=Z-e_{h_1}.               \tag{3.1}
\]

The incoming coordinate-`{h_1,l_1}` line is oriented toward `X_0`, and the
outgoing coordinate-`{h_2,l_2}` line is oriented away from `Y_0`.  Thus, if
the neighbours exist, their edge minima omit `h_1` at `X_0` and `h_2` at
`Y_0`.

If one low coordinate `j in {l_1,l_2}` has `Z_j>0`, insert

\[
                         W=Z-e_j                    \tag{3.2}
\]

between `X_0` and `Y_0`.

Then:

* `W` is a legal rank-`R` point;
* every old interval maximum in the source word is unchanged;
* when the inherited line neighbours exist, the two labels at `X_0` are
  `h_1,j`, the labels at `W` are `h_2,h_1`, and the labels at `Y_0` are
  `j,h_2`; hence each internal pair is distinct (a missing neighbour makes
  the corresponding corner a literal component endpoint); and
* the edge-minimum word recovers `W` by adjacent joins and recovers `X_0`
  and `Y_0` the same way whenever their inherited line neighbours exist;
  a missing neighbour makes the corresponding point a literal component
  endpoint in `ARM_WORD_FACTOR_LIFT`.

#### Proof

The rank and legality of `W` follow from `Z_j>0`.  Any old interval which
crossed the seam contained both `X_0` and `Y_0`, and therefore had maximum
at least

\[
                         X_0\vee Y_0=Z.
\]

Since `W<=Z`, inserting `W` cannot change that maximum.  Intervals ending
at `X_0` or starting at `Y_0` are left unchanged.

At `X_0`, the incoming line minimum is `X_0-e_(h_1)`, whereas
`X_0 meet W=X_0-e_j`.  At `W`, the two connector minima are
`W-e_(h_2)` and `W-e_(h_1)`.  At `Y_0`, the connector minimum is
`Y_0-e_j`, whereas the outgoing line minimum is `Y_0-e_(h_2)`.
All displayed pairs use distinct coordinates.  The adjacent-join equation
is the usual distinct-half-edge-label identity.  QED.

### Concrete balanced coordinates

In the canonical orientation,

\[
 \begin{aligned}
 Z&=(m-A,c_0,m-B,d_0),\\
 X_0&=(m-A,c_0,m-B-1,d_0),\\
 Y_0&=(m-A-1,c_0,m-B,d_0).
 \end{aligned}                                      \tag{3.3}

When `delta>0`, at least one of `c_0,d_0` is positive (indeed `d_0>0`), so one may
take `W=Z-e_4` in this orientation.  In the swapped-baseline hard catalogue,
the low coordinates are `(B,A)`; use coordinate 2 when `B>0` and coordinate
4 when `A>0`.

The unique degenerate label `A=B=0` has no positive low coordinate.  Below
its minimal portal value `Z`, the only rank-`R` points are `X_0,Y_0`, so no
third dominated rank-`R` connector exists.  Cut there and use literal arm
endpoints.  There are at most four such exceptions, one per orientation.

The proof is coordinate-equivariant, so it covers all four high/low
orientations.  It also proves noncontamination for **every** old interval
crossing the seam, not only for the designated portal rectangle.

## 4. Componentwise arm-to-factor lift

Start from any physically valid alternating portal braid.  Insert the
rounded point of Lemma 3.1 at every nondegenerate sharp seam.  Keep every
straight requested line portion in its inherited orientation.  Cut at the
degenerate seams, at path endpoints, and once in every transition cycle.

Along a straight coordinate line, the two half-edge labels at an internal
point are the two line coordinates and are distinct.  Lemma 3.1 gives the
same property at every rounded corner.  Hence every resulting component

\[
 Q=(v_0,e_1,v_1,\ldots,e_h,v_h)
\]

satisfies

\[
       b_{e_i}\vee b_{e_{i+1}}=v_i,
       \qquad b_e=u\wedge v.                       \tag{4.1}
\]

Apply `ARM_WORD_FACTOR_LIFT` and replace its vertex word by

\[
                    v_0,b_{e_1},\ldots,b_{e_h},v_h. \tag{4.2}

Every contiguous maximum of the original signed component word, including
every suffix--prefix portal witness and every witness crossing virtual
component seams, has an exact contiguous representative in (4.2).  The
new word has one edge-minimum occurrence per retained source adjacency and
two literal endpoints per component.

For the hard swapped-baseline catalogue the rounding cost is at most
`2q(q+1)-4`; for the full balanced catalogue it is at most `4m^2`.
For the canonical catalogue there are only `O(m)` component endpoints;
even the conservative `O(m^2)` bound for a noncanonical completed braid
leaves a word of source length plus `O(m^2)`.

This gives a precise conditional three-layer conclusion.  If the retained
source adjacencies have the **lower-edge coverage property**

\[
 \forall x\in L_{R-1}\quad
 \exists i\ne j:\ x_i,x_j<m,
 \quad (x+e_i,x+e_j)\text{ is a retained adjacency},              \tag{4.3}

then every rank-`R-1` point occurs as one of the edge-minimum letters.
Missing adjacencies at only `O(m^2)` cuts can instead be repaired literally.
The lift covers rank `R` through the recovered source vertices, and it
preserves every upper rank already covered by the assumed portal braid.

Condition (4.3) is a real extra gate.  Upper portal completeness alone does
not imply it: a direction assignment may cut or choose the wrong line at a
positive-volume family of lower points.  Component joins themselves are
harmless--the lossless interval map handles them--but the edge-minimum image
still has to cover the lower layer.

## 5. Why maximal ARM iteration stops immediately

The rounded connector removes the first factor obstruction, but it is not
self-similar under maximal edge-minimum iteration.

Take `(h_1,h_2,j)=(1,3,2)` for notation.  Around the connector, the first
edge-minimum word contains

\[
 \begin{aligned}
 b_0&=Z-e_1-e_3,\\
 b_1&=Z-e_2-e_3,\\
 b_2&=Z-e_1-e_2,\\
 b_3&=Z-e_1-e_3=b_0.                              \tag{5.1}
 \end{aligned}

The three consecutive second minima are all equal:

\[
 b_0\wedge b_1=b_1\wedge b_2=b_2\wedge b_3
             =Z-e_1-e_2-e_3.                       \tag{5.2}

Thus the maximal second edge-minimum word cannot recover `b_1` or `b_2`
by adjacent joins.  One may choose a sparser nonmaximal factor, insert a
new lower-rank rounding gadget, or use nonlocal windows, but none is supplied
by the first connector.  Repeating one new surface repair at every one of
`Theta(m)` depths would again cost `Theta(m^3)`.

This is a scoped failure of **naive maximal iteration**, not an
impossibility theorem for sparse or variable-band factors.

### 5.1 What the exact line erosion still gives

Nothing fails in the interiors of the straight arms.  In a
coordinate-`{1,2}` segment write

\[
                         \beta_t=(t,K-t,c,d_0).
\]

For every legal erosion depth `q`, the literal factor letters

\[
 \gamma_t^{(q)}=\bigwedge_{h=0}^q\beta_{t+h}
                =(t,K-t-q,c,d_0)                   \tag{5.3}
\]

satisfy, for every legal `s`,

\[
 \bigvee_{h=0}^s\gamma_{t+h}^{(q)}
                =(t+s,K-t-q,c,d_0).                \tag{5.4}
\]

The complementary line has the coordinate-permuted identical formula.
Thus an arbitrary linear-depth factor exists on every intact arm, with
explicit physical entries and pins.  Its only loss is at the first and last
`q` source positions of the arm.  Repairing those boundary ramps separately
at `Theta(m^2)` alternating turns costs `Theta(qm^2)`, which is cubic for
`q=Theta(m)`.

Equations (5.3)--(5.4) show why further local algebra is not the missing
ingredient.  The unresolved positive object must share the erosion boundary
ramps between many turns, or place most lower capacity in long reservoirs.
The next section proves that one monotone variable band cannot hide this
cost when bounded sharp runs remain uniformly dense.

## 6. A variable-band interval-supply theorem

The next theorem gives the promised linear-depth obstruction without
assuming a fixed delay or a maximal factor.

Let `T_1,...,T_L in L_R` be a prescribed occurrence row.  Here `L` is the
number of physical occurrences in the source portal word; it need not equal
`|L_R|`, although a near-once braid has `L=|L_R|+o(m^3)`.  Suppose a word
`A_1,...,A_N`, with

\[
                              d=N-L\ge0,             \tag{6.0}
\]

realizes it on monotone intervals

\[
 I_i=[\ell_i,r_i]=[i+\alpha_i,i+\beta_i],
 \quad 0\le\alpha_1\le\cdots\le\alpha_L\le d,
 \quad 0\le\beta_1\le\cdots\le\beta_L\le d,       \tag{6.1}
\]

where `alpha_i<=beta_i` and

\[
                         \bigvee_{p\in I_i}A_p=T_i. \tag{6.2}

Put `w_i=beta_i-alpha_i=|I_i|-1`.

Call `p` a **sharp turn** when some coordinate threshold atom is present in
`T_p` and absent from both `T_(p-1)` and `T_(p+1)`.  Let
`p_1<...<p_s` be sharp turns such that

\[
 p_1-1\le H,\quad L-p_s\le H,
 \quad p_{j+1}-p_j-1\le H.                         \tag{6.3}

### Lemma 6.1 (total central span)

Under (6.1)--(6.3),

\[
                         \sum_{i=1}^L w_i\le3Hd+2d. \tag{6.4}

#### Proof

The exact variable-band run inequality at a singleton atom run gives

\[
                         \beta_{p-1}\le\alpha_{p+1} \tag{6.5}

at every sharp turn.

For a peak position itself,

\[
 \begin{aligned}
 w_p
 &=\beta_p-\alpha_p\\
 &\le(\beta_p-\beta_{p-1})
       +(\alpha_{p+1}-\alpha_p),                  \tag{6.6}
 \end{aligned}

so all peak widths sum to at most `2d`.

For `p_j<i<p_(j+1)`, monotonicity and (6.5) give

\[
 w_i\le\beta_i-\beta_{p_j-1}
      \le\beta_{p_(j+1)-1}-\beta_{p_j-1}.          \tag{6.7}

There are at most `H` such indices.  Summing (6.7) over the gaps telescopes
in `beta` and contributes at most `Hd`.  The prefix and suffix in (6.3)
have at most `H` positions each and every width is at most `d`, contributing
at most another `2Hd`.  This proves (6.4).  QED.

### Theorem 6.2 (dense-sharp-turn lower-half obstruction)

If the same physical word `A` represents every nonzero point of rank below
`R`, then (1.1) holds.

#### Proof

The right endpoints `r_i=i+beta_i` are strictly increasing.  Consider a
chosen lower-target interval ending at `r_i`.  If it began at or before
`ell_i`, it would contain `I_i` and its maximum would contain the rank-`R`
point `T_i`, which is impossible.  It must therefore start strictly after
`ell_i`.  There are at most

\[
                         r_i-\ell_i=w_i             \tag{6.8}

such physical intervals.

Exactly `d=N-L` right endpoints are not among the `r_i`.  At one fixed
right endpoint, the distinct suffix maxima form a strict chain.  A chain of
nonzero targets of ranks below `R` has at most `R-1=2m-2` members.  Hence

\[
 |\{x:1\le |x|<R\}|
   \le\sum_iw_i+(2m-2)d
   \le(3H+2m)d.                                    \tag{6.9}

By symmetry about rank `2m`,

\[
 \begin{aligned}
 |\{x:1\le|x|<2m-1\}|
 &=\frac{(m+1)^4-|L_{2m}|}{2}-|L_{2m-1}|-1\\
 &=\frac{m^4+2m^3-m-2}{2}.                         \tag{6.10}
 \end{aligned}

Substitution in (6.9) proves (1.1).  QED.

The proof permits arbitrary lower witnesses.  It does not assume that they
are natural meet cores, does not use the maximal factor, and does not assume
pin survival beyond the fact that the displayed central and lower equations
are actually realized.  Failed pins can only make the construction harder.

There is one further scope point.  The monotone normal form is automatic
after selecting one witness for each member of a **distinct** rank-`R`
antichain and ordering those witnesses by their endpoints.  It is not
automatic that extra repeated occurrences in a proposed portal word receive
additional intervals in precisely the portal order.  Theorem 6.2 applies
when that occurrence-by-occurrence schedule is part of the factor lift--as
it is in `ARM_WORD_FACTOR_LIFT`.  It is not an unrestricted lower bound for
an array which merely represents every distinct point of `L_R` somewhere.

### Proposition 6.3 (bounded rounded runs)

The singleton hypothesis can be relaxed.  Suppose there are `s`
position-disjoint, pairwise ordered intervals, each an internal maximal
positive run for some coordinate atom,

\[
 [u_1,v_1],\ldots,[u_s,v_s],\qquad
 1\le v_j-u_j+1\le C,                               \tag{6.11}
\]

with prefix, suffix, and intervening gaps all of length at most `H`.  Then

\[
 \sum_iw_i\le(3H+2C)d+(C-1)(H+C)s.                 \tag{6.12}
\]

Consequently full lower-ideal coverage forces

\[
 d\ge
 {\displaystyle {m^4+2m^3-m-2\over2}
       -(C-1)(H+C)s
  \over
  \displaystyle 3H+2C+2m-2}.                       \tag{6.13}
\]

#### Proof

For one maximal positive run, the exact variable-band inequality is

\[
 \beta_{u-1}-\alpha_{v+1}\le v-u\le C-1.           \tag{6.14}
\]

For a position in the gap after this run,

\[
 w_i\le\beta_i-\beta_{u-1}+C-1.                   \tag{6.15}
\]

The beta increments telescope over the ordered gaps, while there are at
most `H` positions per gap.  Together with the two boundary gaps this costs
at most `3Hd+(C-1)Hs`.

For `p in [u,v]`, insert the two run boundaries in `w_p` and use (6.14):

\[
 w_p\le(\beta_v-\beta_{u-1})
        +(\alpha_{v+1}-\alpha_u)+(C-1).             \tag{6.16}
\]

There are at most `C` positions per run.  The beta- and alpha-increment
intervals of the ordered runs are disjoint, so their total contribution is
at most `2Cd+C(C-1)s`.  This proves (6.12).  The endpoint-chain count in
(6.8)--(6.10) then gives (6.13).  QED.

The rounded connector of Lemma 3.1 changes each old singleton peak into an
atom run of length two: the high-coordinate atom is present on `X_0,W` and
absent on the preceding line point and on `Y_0`.  Thus take `C=2`.  If a
completed rounded braid contains a **position-disjoint ordered selection**
of `s=O(m^2)` such maximal runs whose prefix, suffix, and intervening gaps
are all `H=O(m)`, the subtracted term in (6.13) is only `O(m^3)`, and the
conclusion remains

\[
                              d=\Omega(m^3).          \tag{6.17}
\]

### Corollary 6.4 (necessary macroscopic reservoir)

If `d=O(m^2)`, every linked factor schedule in the singleton case covering
the lower half must have

\[
                              H=\Omega(m^2).          \tag{6.18}

Thus distributing unused base points evenly between `Theta(m^2)` productive
portal blocks is fatal for the lower factor.  A successful portal word must
cluster the sharp turns and retain a superline-length factor reservoir, or
use a different nonsharp pin geometry.

## 7. Fixed-delay corollary for the explicit portal blocks

The scoped fixed-delay obstruction is even more local.  In one hard-family
portal block with `B<=q-2`, the three consecutive terms

\[
                         X_1,X_0,Y_0

have coordinate 1 equal respectively to

\[
                         m-A-1,\ m-A,\ m-A-1.
\]

The threshold atom `(1,m-A)` is an internal singleton run.  For the one
remaining nondegenerate label in each orientation,
`(A,B)=(0,q-1)`, use instead the consecutive terms

\[
                         X_0,Y_0,Y_1.
\]

Their third-coordinate values are `m-B-1,m-B,m-B-1`, so they give the
symmetric internal singleton peak.  Including this boundary case, there are

\[
 4\left({q(q+1)\over2}-1\right)=2q(q+1)-4           \tag{7.1}

such disjoint peak neighbourhoods over the four orientations.

This count deserves one boundary note.  The `B<=q-2` family includes
`(A,B)=(0,0)`, whose fixed-delay peak is valid even though its rounded
connector is degenerate, and excludes `(A,B)=(0,q-1)`, which lacks `X_1`.
If one instead wants exactly the nondegenerate seam labels, replace the
former by the latter: at `(0,q-1)` the symmetric triple
`X_0,Y_0,Y_1` has a coordinate-3 singleton peak.  The total (7.1) is
unchanged.

Consequently a literal delay-`D` factorable repair which keeps these three
terms in their local order must insert at least

\[
                         D(2q(q+1)-4)                \tag{7.2}

additional atom-positive occurrences into the disjoint peak regions.  If
`q=Theta(m)` and `D=Theta(m)`, this is `Theta(m^3)`.  Rounding by Lemma 3.1
avoids this cost for the **first** factor step; equation (5.2) explains why
the same maximal trick does not automatically repeat.

## 8. Correct next targets

The lower coupling problem is therefore narrower than before.

1. **Lower-edge coverage for the rounded braid.**  Prove that the balanced
   line assignment can retain, up to `O(m^2)` cuts, at least one upper-cover
   edge for every point of `L_(R-1)`.  This would make the one-step ARM lift
   unconditional.
2. **A self-similar sparse corner factor.**  Replace the maximal connector
   factor (5.1) by chosen pin subsets whose factor image is another rounded
   connector rather than the collapse (5.2).  One such gadget working for
   `Theta(m)` levels with only `O(1)` new occurrences per original seam
   would solve the local linear-depth problem.
3. **Reservoir architecture.**  Concentrate the `Theta(m^2)` sharp upper
   turns into a short portal zone and order the remaining base points as one
   or a few long erosion reservoirs.  Theorem 6.2 quantifies the minimum
   reservoir scale and prevents an unproductive uniformly alternating
   search.
4. **Non-core pin sharing.**  A construction may evade (6.4) only by changing
   the prescribed central schedule/band, not by merely reassigning lower
   core witnesses: Theorem 6.2 already allows arbitrary lower intervals.

The present ledger is thus positive for one factor layer, negative for
uniform or densely alternating linear-depth iteration, and open for a
clustered or self-similar variable-band factor.  It does not prove or
disprove the general `g_4=M_m+o(m^3)` conjecture.
