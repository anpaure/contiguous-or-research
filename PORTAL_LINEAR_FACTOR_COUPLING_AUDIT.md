# Independent audit of PORTAL_LINEAR_FACTOR_COUPLING.md

## 1. Verdict

The main variable-band obstruction is correct, with one essential scope:
it applies to a prescribed occurrence row linked to one monotone interval
band (6.1)--(6.2).  It is not a theorem about every equality word.  The
equal-rank noncontainment normal form applies to one witness per distinct
target, not automatically to every occurrence of an externally prescribed
portal row.

Within that scope, Lemma 6.1, the endpoint-capacity argument, the exact
lower-ideal count, Theorem 6.2, and Corollary 6.3 check out.

The rounded-corner construction is also correct, with one wording
qualification.  If an inherited line neighbour is missing, \(X_0\) or
\(Y_0\) is a component endpoint carried literally by
ARM_WORD_FACTOR_LIFT; it is not recovered from two adjacent edge minima.
This does not change the \(O(m^2)\) first-factor conclusion.

Section 7 has a small omitted boundary case.  Its displayed
\(X_1,X_0,Y_0\) peak requires \(B\le q-2\).  The remaining nondegenerate
label \((A,B)=(0,q-1)\) has the symmetric peak \(X_0,Y_0,Y_1\), so the
claimed count remains correct after that addition.

## 2. Rounded complementary corner

With

\[
 X_0=Z-e_{h_2},\quad Y_0=Z-e_{h_1},\quad W=Z-e_j,
\]

where \(j\) is low and \(Z_j>0\), one has

\[
\begin{aligned}
 X_0\wedge W&=Z-e_{h_2}-e_j,\\
 W\wedge Y_0&=Z-e_j-e_{h_1}.
\end{aligned}
\]

If the incoming line neighbour exists, its meet with \(X_0\) is
\(X_0-e_{h_1}\), so the labels at \(X_0\) are \(h_1,j\).  At \(W\)
they are \(h_2,h_1\).  If the outgoing neighbour exists, the labels at
\(Y_0\) are \(j,h_2\).  All pairs are distinct.

An old interval crossing the former adjacency \(X_0,Y_0\) contains both
endpoints and has maximum at least \(Z=X_0\vee Y_0\).  Since \(W\le Z\),
inserting \(W\) changes no old maximum.  Intervals ending at \(X_0\) or
beginning at \(Y_0\) do not acquire \(W\).

If an inherited neighbour is absent, the corresponding corner is an arm
endpoint.  The lift writes it literally.  Only the internal point \(W\) is
always recovered by the two connector minima.

For balanced coordinates, \(\delta>0\) implies \(d_0>0\), so coordinate
4 supplies \(W\).  For the swapped hard catalogue, \(A+B>0\) supplies one
positive low coordinate.  At \(A=B=0\), \(Z\) has positive support only
in its two high coordinates, and \(X_0,Y_0\) are its only rank-\(R\)
lower covers.  The stated degenerate cut is therefore necessary for this
gadget.

## 3. Component lift and lower-edge coverage

After rounding, every internal transition has distinct half-edge labels,
so

\[
 b_{e_i}\vee b_{e_{i+1}}=v_i.
\]

ARM_WORD_FACTOR_LIFT preserves all intervals of the rounded source word,
including intervals crossing virtual component seams when encoded blocks
remain in the same signed order.  The hard and balanced insertion counts
are valid \(O(q^2)\) and \(O(m^2)\) occurrence upper bounds.

Condition (4.3) is sufficient but genuinely additional:

\[
 \forall x\in L_{R-1}\quad
 \exists i\ne j,\ x_i,x_j<m,\quad
 (x+e_i,x+e_j)\text{ retained consecutively}.
\]

The two endpoints lie in \(L_R\) and have meet exactly \(x\), so the
encoded word contains \(x\).  Upper portal completeness does not imply
this condition.  A direction assignment can omit cover edges for a large
lower family.  If only \(C=O(m^2)\) otherwise valid retained adjacencies
are cut, at most \(C\) minima are lost and literal repair is surface-size;
this does not repair a larger family never selected in the first place.

## 4. Maximal second iteration

For \((h_1,h_2,j)=(1,3,2)\), the four local minima are

\[
 b_0=b_3=Z-e_1-e_3,\quad
 b_1=Z-e_2-e_3,\quad
 b_2=Z-e_1-e_2.
\]

Every adjacent meet is \(Z-e_1-e_2-e_3\).  Thus the maximal second meet
word cannot recover \(b_1,b_2\) by adjacent joins.  This refutes literal
maximal self-iteration only, not sparse factors or nonlocal windows.

## 5. Singleton atoms and Lemma 6.1

Atomize coordinate \(c\) into thresholds \((c,t)\).  If an atom is present
in \(T_p\) and absent from \(T_{p-1},T_{p+1}\), no position in
\(I_{p-1}\cup I_{p+1}\) carries it, while some position in \(I_p\) does.
The strict monotone endpoint order leaves such a position only if

\[
 r_{p-1}+1<\ell_{p+1},
\]

equivalently

\[
 \beta_{p-1}\le\alpha_{p+1}.                       \tag{5.1}
\]

Equality leaves exactly one possible atom position, so the integer
boundary is correct.

At a peak,

\[
 w_p\le(\beta_p-\beta_{p-1})
       +(\alpha_{p+1}-\alpha_p).
\]

The peak increments sum to at most \(2d\).  For
\(p_j<i<p_{j+1}\), monotonicity and (5.1) give

\[
 w_i\le\beta_{p_{j+1}-1}-\beta_{p_j-1}.
\]

There are at most \(H\) indices in each gap, and the beta differences
over successive gaps telescope, contributing at most \(Hd\), not one
\(Hd\) per gap.  Prefix and suffix contribute \(2Hd\).  Therefore

\[
 \sum_iw_i\le2d+Hd+2Hd=3Hd+2d.
\]

Prefix, peaks, inter-peak gaps, and suffix partition all indices.
Adjacent peaks merely give an empty gap.

## 6. Endpoint capacity

The selected right endpoints \(r_i=i+\beta_i\) are strictly increasing,
so exactly \(d=N-L\) physical endpoints are unselected.

A lower witness ending at \(r_i\) cannot begin at or before \(\ell_i\):
it would contain \(I_i\) and dominate the rank-\(R\) point \(T_i\).
Its start is one of

\[
 \ell_i+1,\ldots,r_i,
\]

exactly \(r_i-\ell_i=w_i\) choices.  There is no missing \(+1\).

At an unselected endpoint, distinct nonzero suffix maxima form a strict
coordinatewise chain.  Below rank \(R\), it has at most
\(R-1=2m-2\) members.  Grouping one chosen witness for each lower target
by its right endpoint gives

\[
\begin{aligned}
 |\{x:1\le|x|<R\}|
 &\le\sum_iw_i+(R-1)d\\
 &\le(3H+2m)d.
\end{aligned}
\]

The lower witnesses are arbitrary.  The restrictive input is the linked
central occurrence band used to bound \(\sum_iw_i\).

## 7. Exact ideal count

Rank symmetry about \(2m\) gives

\[
 \sum_{r=0}^{2m-1}|L_r|
 ={(m+1)^4-|L_{2m}|\over2}.
\]

Using

\[
 |L_{2m}|={2m^3+6m^2+7m+3\over3},\qquad
 |L_{2m-1}|={2m^3+6m^2+4m\over3},
\]

one obtains

\[
\begin{aligned}
 |\{x:1\le|x|<2m-1\}|
 &={(m+1)^4-|L_{2m}|\over2}-|L_{2m-1}|-1\\
 &={m^4+2m^3-m-2\over2}.
\end{aligned}
\]

Consequently

\[
 d\ge {m^4+2m^3-m-2\over2(3H+2m)}.
\]

The algebra and direct finite rank enumeration agree.

## 8. Exact scope of Theorem 6.2

The theorem assumes simultaneously:

1. a specified occurrence row \(T_1,\ldots,T_L\);
2. a physical word of length \(L+d\);
3. one witness for every prescribed occurrence;
4. the linked form
   \[
   I_i=[i+\alpha_i,i+\beta_i]
   \]
   with both offset sequences nondecreasing;
5. dense sharp turns in that prescribed row;
6. lower-ideal universality of the same word.

Under these assumptions it is rigorous.  What is not proved is that an
arbitrary equality word, arbitrary near-width word, or every successful
portal construction admits such a linked occurrence-by-occurrence band.
Repeated \(T_i\)'s may have nested witnesses, and the distinct-target
normal form need not order all portal occurrences as (6.1).

The valid consequence is:

> a densely alternating portal row cannot couple to the lower ideal
> through this prescribed linked monotone occurrence band with
> \(d=o(m^3)\) when \(H=O(m)\).

It is not an unrestricted obstruction to every equality word with many
portal-like occurrences.  Such an upgrade needs a theorem extracting
dense sharp turns inside the selected distinct-target endpoint band.

## 9. Fixed-delay peak count

For \(B\le q-2\), \(X_1,X_0,Y_0\) has the stated singleton threshold
peak.  The only nondegenerate label per orientation omitted by this
condition is \((A,B)=(0,q-1)\).  There \(Y_1\) exists, and

\[
 X_0,Y_0,Y_1
\]

has coordinate-3 values

\[
 m-B-1,\quad m-B,\quad m-B-1.
\]

Thus the intended count

\[
 4\left({q(q+1)\over2}-1\right)=2q(q+1)-4
\]

is correct after adding the symmetric boundary case.  An internal
singleton run in a delay-\(D\) derivative row must be lengthened to at
least \(D+1\), so keeping each local order costs at least \(D\) inserted
atom-positive row occurrences.  The occurrence neighbourhoods are
disjoint, proving the scoped product bound.

## 10. Ledger

| claim | audit status |
|---|---|
| rounded connector and noncontamination | proved |
| all rounded corners recovered by adjacent minima | endpoint qualification needed |
| surface-order first-factor cost | proved |
| lower-edge condition (4.3) | sufficient and genuinely additional |
| maximal second iteration fails | proved |
| singleton-run inequality and telescoping | proved |
| endpoint capacity | proved |
| exact lower-ideal count | proved |
| Theorem 6.2 for a prescribed linked monotone band | proved |
| Theorem 6.2 for arbitrary equality words | not proved |
| fixed-delay peak count | proved after symmetric boundary case |

The mathematical message survives: rounded portal corners support one
lower factor layer at surface cost, while a dense linked occurrence band
has too little endpoint capacity for the full lower ideal.  A general
no-go still needs a theorem forcing that linked band in arbitrary words.
