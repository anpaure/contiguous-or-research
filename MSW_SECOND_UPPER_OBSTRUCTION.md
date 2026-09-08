# A uniform second-upper obstruction for the MSW Catalan factor

## 1. Outcome

Let

\[
 P=(x_0,y_0,x_1,\ldots,y_{m-1},x_m)
\]

be a column of the Mütze--Standke--Wiechert minimum-change Chung--Feller
factor on a `2m`-element core.  Its first upper colours

\[
                         y_i=x_i\cup x_{i+1}
\]

biject the rank-`m+1` layer.  The next upper map on internal states is

\[
 \Gamma(x_i)=y_{i-1}\cup y_i,\qquad 1\le i<m.       \tag{1.1}
\]

The map (1.1) is not onto once `m>=4`.  A uniform missing target is

\[
 T_m=\{1,2,3,5,6\}\cup\{8,9,\ldots,m+4\}.          \tag{1.2}
\]

It has size `m+2`.  Equivalently, its incidence word is

\[
                 1110110\,1^{m-3}0^{m-4}.          \tag{1.3}
\]

This gives an all-dimensional obstruction to using the unchanged MSW
factor in the fixed-outer punctured-prism lift.  In the notation of
`PRISM_SEGMENT_COMPLETION.md`, the colour map `g` in (5.13) is not
surjective for every `m>=4`.

The result does **not** obstruct a rewired old factor or a lift which first
replaces the outer paths by the Mütze--Weber upper-layer path systems.  It
only closes the most direct canonical-factor branch.

The definitions of the maps `f,g,h` used below are those in Mütze,
Standke and Wiechert, [A minimum-change version of the Chung--Feller
theorem](https://arxiv.org/abs/1603.02525).

## 2. The two flip coordinates at an internal column state

Write the MSW flip permutation of a column as

\[
             (a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1}),           \tag{2.1}
\]

where `a_i` is inserted by the MSW map `g` and `b_i` is then deleted by
the map `h`.  At the internal state `x_i`,

\[
 y_{i-1}=x_i\cup\{b_{i-1}\},\qquad
 y_i=x_i\cup\{a_i\}.                              \tag{2.2}
\]

Therefore

\[
                 \boxed{\Gamma(x_i)
                    =x_i\cup\{a_i,b_{i-1}\}.}      \tag{2.3}
\]

The column states are the Chung--Feller classes: `x_i` has exactly `i`
flaws, and the minimum-change bijection

\[
                         f=h\circ g                 \tag{2.4}
\]

maps flaw class `i-1` bijectively to flaw class `i`.  Thus, for `i>0`,
the preceding state and the deleted coordinate `b_(i-1)` are unique.

## 3. Symbolic height audit of the target

Regard a set as an up/down word, with membership giving an up-step.  Let
`H(r)` be the height immediately before position `r` in (1.3).  Directly,

\[
\begin{array}{c|rrrrrrr}
r&1&2&3&4&5&6&7\\ \hline
H(r)&0&1&2&3&2&3&4,
\end{array}                                                       \tag{3.1}
\]

and

\[
 H(r)=r-5\quad(8\le r\le m+4),\qquad
 H(r)=2m+5-r\quad(m+5\le r\le2m).                \tag{3.2}
\]

If (1.2) were `Gamma(x_i)`, equation (2.3) would give

\[
                    x_i=T_m\setminus\{p,q\}         \tag{3.3}
\]

for two up-step positions `p<q` of `T_m`.  The height immediately before
position `r` in (3.3) is

\[
 H_{p,q}(r)=H(r)-2\mathbf1_{p<r}-2\mathbf1_{q<r}.  \tag{3.4}
\]

The MSW map `g` has the following elementary height description.  Let
`d_0(x)` be the number of down-steps starting at height zero.  Among the
down-steps starting at height zero or one, in left-to-right order, `g`
flips number `d_0(x)+1`.

Substituting (3.1)--(3.4) into this rule gives the complete list of pairs
for which the bit inserted by `g(x_i)` is one of `p,q`:

\[
\begin{array}{c|c|c}
\{p,q\}&\text{bit inserted by }g&\text{number of flaws of }x_i\\ \hline
\{1,6\}&6&2\\
\{2,5\}&5&2\\
\{3,6\}&6&1\\ \hline
\{2,r\},\ 8\le r\le m+4&2&0\\
\{5,8\}&8&0\\
\{6,8\}&8&0.
\end{array}                                                       \tag{3.5}
\]

For completeness, (3.5) is only a constant-size height case split.  The
two subtractions in (3.4) divide the word into three height translates of
(3.1)--(3.2).  A new down-step can be selected by `g` only where its
starting height is zero or one.  Checking the two early descents at
positions `4,7`, the two changed positions, and the final descent gives
exactly the six rows of (3.5); all other pairs make `g` select a position
outside `\{p,q\}`.

The last three families in (3.5) have zero flaws.  They can only be initial
states `x_0`, whereas (1.1) is indexed by `1<=i<m`; hence they cannot be
preimages of `T_m` under `Gamma`.

## 4. The three nonzero-flaw cases

For the first three rows of (3.5), the inverse Chung--Feller move is again
read directly from the height word.  The following table displays the
unique predecessor.  The notation `x-a+b` means turn the up-step at `a`
down and the down-step at `b` up.

\[
\begin{array}{c|c|c|c}
\{p,q\}&x=T_m\setminus\{p,q\}&f^{-1}(x)&
  \text{bit deleted by the preceding }h\\ \hline
\{1,6\}&x&x-8+4&4\\
\{2,5\}&x&x-6+4&4\\
\{3,6\}&x&x-8+4&4.
\end{array}                                                       \tag{4.1}

Indeed, applying the height rule for `g` to the three displayed
predecessors inserts respectively `8,6,8`; the subsequent `h` move deletes
position `4` and produces `x`.  Uniqueness follows from the bijectivity in
(2.4).  Consequently

\[
                            b_{i-1}=4               \tag{4.2}
\]

in every remaining case.

But `4` is not a member of `T_m`.  Equation (2.3) says that every
`Gamma(x_i)` contains `b_(i-1)`, contradicting (4.2).  This proves

\[
                         T_m\notin\operatorname{im}\Gamma
                         \qquad(m\ge4).              \tag{4.3}
\]

## 5. Consequence for the Catalan seam programme

For the fixed MSW outer scaffold, the canonical rank-transfer squares are
indexed by the internal states `x_i`, and their zero-tag colours are exactly
`Gamma(x_i)`.  The surjectivity prerequisite in Corollary 9 of
`GRID_SHUFFLE_DEFECT_AUDIT.md` therefore fails uniformly.

The correct next use of the MSW/Mütze--Weber machinery is not to keep these
outer paths.  It is to translate the published inductive dangling-path
systems in all upper layers into the punctured-prism language, then ask
whether their exposed ports can be joined to prescribed rungs with
complementary endpoint topology and `O(Cat_m)` total cuts.

The accompanying programs `audit_msw_g_surjectivity.cpp` and
`analyze_msw_explicit_g_obstruction.cpp` check the formulas, but the proof
above is symbolic and does not depend on finite enumeration.
