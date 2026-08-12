# Antitone pairing solves the terminal birail Hall problem exactly

Date: 2026-08-01  
Status: unconditional abstract optimization theorem and exact conditional
application to the robust two-boundary compiler.  The quotient-folded C8
carrier has the required all-depth comparator action on its two nested ray
supports, but owner-legal host planting, matching closure, and transport to
arbitrary adjacent obligations remain open.  No unconditional `B(k)+O(1)`
claim is made.

## 0. Result

Let `x_1,...,x_N` and `y_1,...,y_N` lie in `{0,...,d}`.  A permutation
`pi` pairs `x_i` with `y_{pi(i)}`.  Put

\[
 C_\pi(a,c)=\#\{i:x_i\le a,\ y_{\pi(i)}\le c\},
 \qquad
 \delta(\pi)=\max_{0\le a,c\le d}
       \bigl(C_\pi(a,c)-a-c\bigr)_+ .                 \tag{0.1}
\]

Write

\[
 L(a)=\#\{i:x_i\le a\},\qquad
 R(c)=\#\{j:y_j\le c\},                              \tag{0.2}
\]

and

\[
 E_L=\max_a(L(a)-a),\qquad E_R=\max_c(R(c)-c).        \tag{0.3}
\]

Then

\[
 \boxed{\min_\pi\delta(\pi)=(E_L+E_R-N)_+.}          \tag{0.4}
\]

Pairing the increasing order of the `x` values with the decreasing order of
the `y` values attains (0.4).  Moreover, every switch which removes one
strict concordance decreases the southwest corner-count matrix pointwise.
Consequently the abstract terminal birail landscape has no nonglobal local
minimum under these switches.

On the exact robust two-boundary compiler face of
`MATH_THEOREM_R_OUTWARD_RAY_SEAM_PORT_SDR_AND_LOWER_HALL_SEPARATION_20260730.md`,
this proves the exact optimum over every freely reachable right-threshold
pairing.  The remaining OR-specific theorem is physical reachability of the
pairings inside one closed safe-move component.

The quotient-folded C8 Hamilton pair in
`MATH_THEOREM_A_FOUR_BLOCK_C8_COMMONQ_SCREENS_AND_PHYSICAL_BOUNDARY_20260801.md`
has precisely the required comparator support:

\[
 \begin{array}{c|cc}
 &\text{prefix rail}&\text{suffix rail}\\ \hline
 -&a_3&a_1\\
 +&a_1&a_3.
 \end{array}                                          \tag{0.5}
\]

Thus the central owner, immediate palettes, topology, and residence parts
of one all-depth comparator are now physical.  The two nonnative ray hosts,
the cut casualties, addressed occurrence transport, and matching-closed
common-Q state are not yet physicalized.

## 1. Pointwise minimum of every corner

For fixed `a,c`, put

\[
 A_a=\{i:x_i\le a\},\qquad
 B_c=\{i:y_{\pi(i)}\le c\}.                            \tag{1.1}
\]

Their cardinalities are `L(a)` and `R(c)`, independent of the pairing.
Inclusion-exclusion gives the universal Frechet lower bound

\[
 C_\pi(a,c)=|A_a\cap B_c|
 \ge \max\{0,L(a)+R(c)-N\}.                           \tag{1.2}
\]

Sort the `x` values increasingly and pair them with the `y` values sorted
decreasingly.  Then `A_a` is an initial segment of length `L(a)`, whereas
`B_c` is a terminal segment of length `R(c)`.  Therefore this one pairing
simultaneously attains equality in (1.2) for every `a,c`:

\[
 C_\downarrow(a,c)=\max\{0,L(a)+R(c)-N\}.             \tag{1.3}
\]

This remains true with repeated threshold values; choose arbitrary stable
orders inside tied classes.

## 2. Evaluation of the deficiency

Substituting (1.3) into (0.1), a corner with `L(a)+R(c)<=N` contributes
zero.  At any other corner its unsigned excess is

\[
 L(a)+R(c)-N-a-c
   =(L(a)-a)+(R(c)-c)-N.                               \tag{2.1}
\]

If `E_L+E_R>N`, choose maximizers `a_*`,`c_*`.  Then

\[
 L(a_*)+R(c_*)
  =E_L+E_R+a_*+c_*>N,                                  \tag{2.2}
\]

so (2.1) applies and gives `E_L+E_R-N`.  If
`E_L+E_R<=N`, every value in (2.1) is nonpositive.  This proves (0.4).

## 3. Monotone comparator path

Suppose two paired rows have

\[
 x_i<x_j,\qquad y_i<y_j.                               \tag{3.1}
\]

Swap their right endpoints.  Directly comparing the two contributions to
each southwest corner gives

\[
 C_{\rm old}(a,c)-C_{\rm new}(a,c)
  =\mathbf 1_{\{x_i\le a<x_j\}}
   \mathbf 1_{\{y_i\le c<y_j\}}.                     \tag{3.2}
\]

Hence no corner count increases.  For the integral potential

\[
 \Phi(\pi)=\sum_{a=0}^d\sum_{c=0}^d C_\pi(a,c),       \tag{3.3}
\]

the decrease is exactly

\[
 (x_j-x_i)(y_j-y_i)>0.                                 \tag{3.4}
\]

Repeated concordance removal terminates and yields an antitone pairing.
Weak concordances involving a tie may be reordered freely and have empty
rectangle in (3.2).  This proves the monotone form of the theorem.

## 4. Exact robust-compiler specialization

On the authenticated robust-core face, every residual lower obligation `S`
has a two-prefix neighbourhood

\[
 N_C(S)=\{L_1,\ldots,L_{\ell_L(S)}\}
       \cup\{R_1,\ldots,R_{\ell_R(S)}\}.              \tag{4.1}
\]

The exact deficiency form of Hall is

\[
 \delta=\max_{0\le a,c\le d}
 \left(
  \#\{S:\ell_L(S)\le a,\ \ell_R(S)\le c\}-a-c
 \right)_+.                                           \tag{4.2}
\]

If the safe physical component preserves the two marginal threshold
multisets and realizes an arbitrary pairing between them, (0.4) gives

\[
 \min\delta=(E_L+E_R-N)_+.                             \tag{4.3}
\]

Combining (4.3) with the corrected serial bound gives, for an
upper-complete starting carrier and a genuinely recycled zero-length move
bank,

\[
 \nu(k)\le B(k)+(E_L+E_R-N)_+.                         \tag{4.4}
\]

With upper defect `u` and retained length charge `chi`, the honest statement
is instead

\[
 \nu(k)\le B(k)+u+\chi+(E_L+E_R-N)_+.                 \tag{4.5}
\]

Equations (4.4)--(4.5) are conditional on the robust two-prefix reduction
and physical permutation reachability.  They do not apply to the unrestricted
compiler or to a union of incompatible cap states.

## 5. The folded C8 is the correct comparator shape

For the aligned quotient-folded Hamilton cut, suppressing the fixed core,
the directed source-support differences are

\[
\begin{aligned}
 {\cal P}^-&=\{\{z,a_3\}\cup\{f_1,\ldots,f_t\}:1\le t<d\},\\
 {\cal S}^-&=\{\{z,a_1\}\cup\{f_t,\ldots,f_d\}:1<t\le d\},\\
 {\cal P}^+&=\{\{z,a_1\}\cup\{f_1,\ldots,f_t\}:1\le t<d\},\\
 {\cal S}^+&=\{\{z,a_3\}\cup\{f_t,\ldots,f_d\}:1<t\le d\}.
                                                               \tag{5.1}
\end{aligned}
\]

Thus the move interchanges the endpoint labels `a_1,a_3` between the same
two nested profile chains.  This is the all-depth analogue of one 2x2
birail comparator, not merely a depth-two projection.

The same folded construction already proves, for the audited range
`2<=d<=12`:

1. one simple owner bank on `8d+24` vertices;
2. exact lower-q1 rainbow degree two;
3. Hamilton topology;
4. complete immediate upper support with phase-common multiplicity; and
5. depth-`d` residence with a nonzero maximal inverse.

This removes the literal four-copy owner-multiplicity obstruction.  It does
not yet prove an edge of the corrected safe graph `Gamma`, because:

* opening the cycle loses one lower-q1 colour;
* the minimum aligned-base cut loses one upper colour and the minimum
  upper-safe cut has displaced ray addresses; a separate upper-safe aligned
  face exists at graded cost `22d+44`, but its two natural internal host
  modes respectively create rank-`r+1` owners or a triple owner stutter;
* the two required ray hosts are not native maximal-erosion letters;
* distinct-value support closure is weaker than protected addressed
  occurrence transport; and
* a local common-Q solution is weaker than a matching-closed global cap
  state.

## 6. Exact remaining physical theorem

A sufficient next statement is the following.

**Folded adjacent-comparator lift.**  Every strict concordant adjacent pair
in the terminal robust-core order admits a relabelled quotient-folded C8
replacement which:

1. realizes exactly the corner update (3.2);
2. preserves the complete upper interval-OR language and depth-`d`
   residence;
3. repairs the cut palettes and plants/recycles the two ray hosts with
   bounded total `chi`;
4. stays in one matching-closed common-Q state; and
5. fixes all other terminal threshold pairs.

If this holds, bubble sorting physically reaches the antitone optimum.  If
also `E_L+E_R<=N+C` uniformly, then the corrected serial theorem gives

\[
                         \nu(k)\le B(k)+C+O(1),          \tag{6.1}
\]

where the displayed `O(1)` is exactly the recycled host/cut state, not a
cost per comparator.  If that state has zero terminal charge and
`E_L+E_R<=N`, the same implication gives `nu(k)=B(k)`.

The number of serial comparators is irrelevant to length only after item 3
is proved.  A constant fresh split cost per move would accumulate and does
not imply (6.1).

## 7. Canonical two-ray marginals are exactly on the zero-defect boundary

There is one useful scalar consequence which does not require a physical
reachability claim.  Suppose the residual local task bank consists of one
left ray and one right ray of length `d-1`, and the two marginal threshold
multisets are

\[
 \{x_i\}=\{0^{d-1},1,2,\ldots,d-1\},\qquad
 \{y_i\}=\{0^{d-1},1,2,\ldots,d-1\}.                  \tag{7.1}
\]

Then `N=2d-2`.  For `0<=a<=d-1`,

\[
 L(a)=d-1+a,\qquad L(a)-a=d-1,                        \tag{7.2}
\]

and the same formula holds on the right.  Hence

\[
 E_L=E_R=d-1,\qquad E_L+E_R=N.                        \tag{7.3}
\]

The antitone optimum therefore has

\[
                         \min_\pi\delta(\pi)=0.        \tag{7.4}
\]

This is exactly the scalar profile suggested by the folded source rays
(5.1): one family has a positive left threshold and zero right threshold,
and the other has the reflected profile.  Turning this observation into a
compiler theorem still requires proving that the actual owner-legal host
atlas exposes precisely the lists (7.1), with no additional structural
zeros or cap-state incompatibility.  Subject to that identification, the
terminal two-ray Hall gate has no residual defect at all; only the physical
comparator/host regeneration remains.
