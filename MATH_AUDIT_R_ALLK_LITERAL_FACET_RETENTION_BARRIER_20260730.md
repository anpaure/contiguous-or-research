# Adversarial audit of the all-`k` literal-facet retention barrier

Date: 2026-07-30  
Method: hand proof audit only; no web, finite search, SAT, or remote job.  
Audited file:
`MATH_THEOREM_R_ALLK_LITERAL_FACET_RETENTION_BARRIER_20260730.md`.

## 0. Verdict

The decisive claims are valid after four scope corrections, all already
applied to the theorem file:

1. the general cutoff is `1<=s<=k`; `mu(k,0)=0` is only a recursion base;
2. the Pascal recurrence is stated for `1<=s<=k-1`;
3. the two-value adjacent-deadline conclusion is explicitly conditional on
   (3.2), with unconditional applicability only eventually; and
4. the finite word lengths prove nonretention of the complete literal facet
   layer, not a derivative normal form by themselves.

No mathematical retraction is required.

## 1. Truncated deadline

The standard monotone-deadline proof uses only the selected top antichain
and targets below it.  It therefore applies verbatim to the initial ideal
through rank `s`.  If a word for that ideal has length

\[
                         n={k\choose s}+t,
\]

then every lower occurrence lies before the first rank-`s` occurrence in
its column and hence has physical length at most `t`.  The number of such
triangular cells is at most

\[
 t n-{t\choose2}
 =t{k\choose s}+{t+1\choose2}.                      \tag{1.1}
\]

This proves the initial-ideal deadline used in the theorem without any
upper-target hypothesis.

## 2. Deletion and concatenation

If an interval has union `S`, every constituent letter is a subset of `S`.
Thus a witness of rank at most `s` cannot contain a cell of rank greater
than `s`.  Deleting all high cells preserves every such witness inside one
retained low component.  Concatenating the components preserves those
intervals and can only add extra ones.  Therefore

\[
 |A|-H_{>s}\ge {k\choose s}+d_s,                    \tag{2.1}
\]

which is the claimed rank-separation bound.

For odd `k=2m+1`, choosing `s=m-1` gives the exact cutoff `rank>=m` and
lower count

\[
 \sum_{j=1}^{m-2}{k\choose j}=\Lambda-W-M.          \tag{2.2}
\]

Hence every retained literal PBBS facet is genuinely charged as a high
cell; seam placement and interleaving cannot evade the inequality.

## 3. Adjacent-deadline algebra

Let

\[
 f_M(t)=tM+{t+1\choose2},
 \qquad \Lambda'=\Lambda-W-M.
\]

The three decisive evaluations are

\[
 f_M(d-3)-\Lambda'
 =\sigma-(d-2)(W-M)-W-3d+3,                         \tag{3.1}
\]

\[
 f_M(d-1)-\Lambda'
 =\sigma+W-d(W-M)-d,                                \tag{3.2}
\]

and

\[
 f_M(d-2)-\Lambda'
 =\sigma-(d-1)(W-M)-2d+1.                           \tag{3.3}
\]

Minimality of `d` gives `sigma<W+d`, so (3.1) is negative for `d>=3`;
the cases `d<=2` give `delta>=d-2` trivially.  Condition (3.2) of the
theorem makes the present equation (3.2) nonnegative.  Equation (3.3)
then gives the exact threshold between `delta=d-2` and `delta=d-1`.

The ratio

\[
 W-M={4W\over k+3}                                  \tag{3.4}
\]

and `d=O(sqrt(k))` make the side condition valid eventually.  Therefore a
`B(k)+O(k)` word can contain only `O(W/k)` rank-at-least-`m` cells; a
literal PBBS construction must compile a `1-O(1/k)` fraction of its facets.

## 4. Pascal recurrence and finite scope

For `1<=s<=k-1`, the word

\[
                         A,\{z\},z+C                \tag{4.1}
\]

proves the displayed recurrence: `A` covers the old ideal through rank
`s`, while `z+C` covers marked targets whose old part has rank at most
`s-1`.  The singleton handles the empty old part.  Iteration never invokes
`nu(0)` under the corrected scope.

The finite floors `793,3004,11441` for `k=11,13,15` recompute exactly.
They prove that the complete rank-`m` deck is not literal in the retained
optimal words.  The stronger statement that those words possess a
derivative carrier is known from separate audits and is not inferred here.

## 5. Exact surviving gate

The barrier is architectural, not a stronger lower bound on unrestricted
`nu(k)`.  It leaves open—and quantitatively forces—the common compiler
route: rank-`m` facets must occur mainly as overlapping OR windows of
lower-rank physical cells.  The unresolved obstruction is exactly the
pair-and-higher interval-conflict expansion isolated in the run-boundary
theorem.
