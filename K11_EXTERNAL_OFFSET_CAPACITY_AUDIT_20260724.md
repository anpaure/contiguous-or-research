# Independent audit of the external-offset capacity note

## Verdict

**PASS, with two minor self-containment edits recommended.**  I found no
false inequality, missing charge, or incorrect constant in
`K11_EXTERNAL_OFFSET_CAPACITY_20260724.md`.  In particular:

* the external endpoint slots really are in bijection with the
  (E=465-m) external matching edges;
* the rank-five witness is a proper physical subinterval of the matched
  rank-six witness;
* the source, anchor, and directed-exposure bounds in (3.4) are valid for
  every (X\subseteq[11]);
* the factor (3) in (d_X\le3u_X) is a literal maximum indegree, not an
  average estimate;
* the completion hierarchy (3.5), including
  ((\Delta_1,\ldots,\Delta_6)=(42,42,28,14,5,1)), is exact;
* the singleton calculation gives exactly (K_x\le210); and
* all five (n_5=133) inequalities (6.5)--(6.9) have the stated constants.

No search, computation, random experiment, or solver was used.  The audit
uses only the two cited frozen notes and direct interval/set counting.

The two recommended edits do not alter any result:

1. In the outcome paragraph around (1.3), explicitly restrict to
   (1\le |X|\le6), as Theorem 1 already does.  Without an announced
   out-of-range binomial convention, the displayed formula is not literally
   defined for arbitrary (X\subseteq[11]).
2. In the definition immediately before (3.5), write completion for a
   generic matching edge (S\subset U) as
   (X\subseteq U, X\nsubseteq S).  The notation (S_p,U_p) was introduced
   only for external anchors (p\in\mathcal P_{\rm ext}), so using it in the
   same sentence to define central completions is formally undefined.

It would also improve wording, without being logically necessary, to say at
the first use of “canonically” that the selected witness families have been
fixed, and to mention (\sum_xe_x^{\rm ext}=E) explicitly in the Hall
paragraph.

## 1. External anchor bijection and physical containment

Let the central segment be ([L,R]), of length (m).  The audited endpoint
saturation gives (L) prefix slots and (464-R) suffix slots, hence

\[
 L+(464-R)=465-m=E.
\]

Every one is occupied exactly once in each selected witness family.  At a
prefix anchor (p<L), the rank-five and rank-six witnesses have the same
left endpoint.  The rank-six endpoint cannot be earlier, since its OR would
then be contained in the rank-five OR, and it cannot be equal, since one
physical interval cannot have two OR ranks.  Thus it ends later.  The suffix
argument is symmetric.  Therefore (I_p\subsetneq J_p) is justified.

With (D_p=J_p\setminus I_p), one has

\[
 S_p\cup\operatorname{OR}(D_p)=U_p=S_p\sqcup\{\xi_p\}.
\]

The anchor entry (B_p\) lies in (I_p), so (B_p\subseteq S_p) and
(\xi_p\notin B_p).  Also (\xi_p\in\operatorname{OR}(D_p)).  These are
exactly the three physical facts subsequently used.

Both selected families have 462 intervals in 465 positions with strictly
ordered endpoints.  Hence every selected rank-six interval has at most four
cells.  It follows that a prefix added cell is at one of
(p+1,p+2,p+3), while a suffix added cell is at one of
(p-1,p-2,p-3).  Consequently all added cells lie in

\[
 [0,L+2]\cup[R-2,464].
\]

The classified central segments have length at least (228), so the two
halos are disjoint; no occurrence can receive both a prefix and a suffix
charge.

## 2. Audit of the three capacity bounds

If (\xi_p\in X), then (X\nsubseteq S_p), because (\xi_p\notin S_p).
Thus only the (E-s_X) sources not containing all of (X) can carry a
label from (X).  The same argument with (B_p) gives (E-a_X).
Finally, (\xi_p\in\operatorname{OR}(D_p)\cap X), so that anchor is counted
by (d_X).  Hence

\[
 e^{\rm ext}(X)\le\min\{E-s_X,E-a_X,d_X\}.
\]

For every anchor counted by (d_X), choose one added-cell position meeting
(X).  A fixed left-halo position (t) can be charged only from
(p=t-1,t-2,t-3); a fixed right-halo position has the reversed list.  The
halos are disjoint, so the charge multiplicity is at most three, proving

\[
 d_X\le3u_X.
\]

There is no omitted factor of two at the two boundaries.

The Hall interpretation is also exact.  Make (e_x^{\rm ext}) copies of
coordinate (x), and join them to sources omitting (x).  For a family of
copies with coordinate support (X), its neighborhood is exactly the
sources which fail to contain (X), of size (E-s_X).  Its cardinality is
at most (e^{\rm ext}(X)), and taking all copies on a support proves the
converse necessity.  Since the actual multiplicities satisfy
(\sum_xe_x^{\rm ext}=E), the stated family of inequalities is precisely
Hall's condition.

## 3. Audit of the subset-completion hierarchy

For a generic inclusion-matching edge (S\subset U), the indicator

\[
 \mathbf1_{X\subseteq U}-\mathbf1_{X\subseteq S}
\]

is one precisely when that edge completes (X).  Summing over the perfect
matching gives

\[
 \Delta_t
 =\binom{11-t}{6-t}-\binom{11-t}{5-t},
 \qquad 1\le t\le6.
\]

Thus the central and external completion counts sum to (\Delta_t).  An
external completion must have its unique added coordinate in (X), so

\[
 \Delta_t-\kappa_X^{\rm cen}
 =\kappa_X^{\rm ext}
 \le e^{\rm ext}(X).
\]

The numerical rows check directly:

\[
 (u_1,\ldots,u_6)=(252,126,56,21,6,1),
\]

\[
 (\Delta_1,\ldots,\Delta_6)=(42,42,28,14,5,1).
\]

For (t\le5), writing (c_X) for the number of central five-set sources
containing (X) gives (s_X=v_t-c_X), and the displayed algebra yields

\[
 w_X^{\rm cen}=c_X+\kappa_X^{\rm cen}\ge u_t-E.
\]

The classified modes have (E\ge132), while (u_t\le126) for every
(t\ge2).  Hence the statement that this coarse projection has positive
content only at (t=1) is correct.

## 4. Audit of the singleton constant (210)

For one coordinate, let

\[
 J_x=\sum_\ell(\ell-2)_+,
 \qquad
 K_x=\sum_\ell(\ell-3)_+,
 \qquad
 R_x^{(3)}=\#\{\ell:\ell\ge3\}.
\]

Then (J_x-K_x=R_x^{(3)}).  The number of central selected five-set sources
containing (x) is

\[
 c_x=m-2-J_x-h_x,
\]

because all triple windows except (H) are used.  Since the complete
five-set point degree is 210,

\[
 s_x=210-c_x.
\]

Using (e_x^{\rm ext}=43-R_x^{(3)}-h_x), (E=465-m), and the source
capacity gives

\[
 43-R_x^{(3)}-h_x
 \le253-J_x-h_x,
\]

which is exactly (K_x\le210).

The independent upper-layer derivation has exactly the same slack.  There
are (m-3-K_x) central four-window six-sets containing (x), while at most
(E) of the 252 six-sets containing (x) can be external.  Thus

\[
 m-3-K_x\ge252-E=m-213,
\]

again giving (K_x\le210).  No seam indicator or endpoint unit is missing.

## 5. Audit of the (n_5=133) algebra

Here (m=332-n_4) and (E=133+n_4).  Every physical position outside the
central (D_3) segment is either one of the 133 distinct literal five-set
entries or one of the (n_4) distinct literal four-set entries.  Therefore

\[
 a_x=\ell_x^{(5)}+\lambda_x,
 \qquad
 u_{\{x\}}=\ell_x^{(5)}+\lambda_x+b_x.
\]

Substituting these and

\[
 e_x^{\rm ext}
 =\lambda_x+\varrho_x+E_{1,x}+E_{2,x}
  -22-2h_x-2i_x
\]

into the anchor and exposure capacities gives, respectively,

\[
 \ell_x^{(5)}+\lambda_x
 \le90+n_4+R_x^{(3)}+h_x,
\]

\[
 \ell_x^{(5)}+2\lambda_x+\varrho_x+E_{1,x}+E_{2,x}
 \le155+n_4+2h_x+2i_x,
\]

and

\[
 \varrho_x+E_{1,x}+E_{2,x}
 \le3\ell_x^{(5)}+2\lambda_x+3b_x+22+2h_x+2i_x.
\]

All constants (90,155,22) check.

The zero positions decompose exactly as

\[
 K_x=m-o_x-E_{1,x}-2E_{2,x}-3R_x^{(3)},
 \qquad
 o_x=56-h_x-i_x+\varrho_x.
\]

Combining with (K_x\le210) gives

\[
 \varrho_x+E_{1,x}+2E_{2,x}+3R_x^{(3)}
 \ge66-n_4+h_x+i_x.
\]

Finally, subtracting the audited budget

\[
 E_{1,x}+E_{2,x}+R_x^{(3)}+\lambda_x+\varrho_x
 =65+h_x+2i_x
\]

gives exactly

\[
 E_{2,x}+2R_x^{(3)}\ge1+\lambda_x-n_4-i_x.
\]

Thus (6.5)--(6.9) are algebraically correct and mutually consistent.

## 6. Final scope check

The note proves a necessary external-capacity system, not a contradiction.
The scalar projections retain slack because (E>u_t) from (t=2)
onward, and the (n_5=133) literal-five incidence and boundary-halo
incidence are not fixed by the existing run ledger.  The stated next gate
therefore accurately requires a genuinely set-valued or order-sensitive
use of (3.4).  The note makes no unsupported improvement to the interval
for (\nu(11)).
