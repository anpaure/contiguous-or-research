# Quantitative two-sided gain at near-width length

2026-09-07. Pure proof. Root synthesis and a separate quantitative audit
passed; no mathematical computation was used.

For a nonzero set-valued word A on [2b], let U(A) be its set of nonempty
interval unions. Put W=binom(2b,b). The accepted long tensor construction
proves the following statement for every sufficiently large integer b.

There exist two words A_b,B_b, of the same length (1+o(1))W, such that:

1. Both realize the entire middle layer.
2. U(A_b) is contained in U(B_b): NO old target is lost.
3. In EACH of the two rank ranges b-q and b+q, with
   ceil(h/2)<=q<=h and h=floor(sqrt(b)/4), the difference
   U(B_b) minus U(A_b) contains at least 4^b/2000 targets.

Thus the total new target count is at least 4^b/1000, or 0.1 percent of
the entire cube. This is a deliberately conservative proved lower bound,
not an empirical coverage percentage or an optimal gain claim.

## Accepted construction and its exact inputs

The complete geometry, simultaneous endpoint-role rethreading, global
collision proof and literal-word ledger are in
`/Users/amir.nuriyev/.codex/worktrees/7796/problem/research_round1/LONG_TENSOR_TWO_SIDED_ACTUAL_GAIN.md`.
That theorem passed full root reading, a separate root geometry audit,
a separate full-synthesis audit, and task02's independent census and
compiler audits. Its finite actual-union estimate invokes the previously
accepted central matching and temporal pair-selection theorems; no
independent residual or unproved geometric gate is being inserted here.

Choose m=floor(log log log b), eventually positive, and set

    h=floor(sqrt(b)/4),  ell=2mh+1,  t=4^m,
    N=mt/4,  M=2t ell,  R=M-6N,  H=floor(h sqrt(m)).

Each marked packet comprises ALL t tensor rows, and its whole R-point
middle support is selected as one matching unit. Matching individual
rows separately would not prove this result. The correct prefix
parameters are a=4mh, g=8m+2, and t=4^m. They satisfy the accepted
theorem along every sufficiently large integer b. The local module size
is b_0=4h+1; padding p=b-m b_0 is eventually nonnegative.

For 2<=q<=h, the exact fresh packet count and old-support bound are

    g_q=4N(q-1),
    o_q<=M-2tq-4N(q-1).

The second inequality counts every old endpoint occurrence, including
cross-module ones, then subtracts explicitly paired duplicate witnesses.
For the strict range 2<=q<h, the independently audited sharper census is

    o_q=M-2tq-4N(q+1),  f_q=M-2tq-8N,
    (o_q+g_q/2)/R=1-2q(t+N)/R<=1-q/(8h),

where f_q is the new packet support. These are PER-PACKET counts; they
do not assert that different selected packets are disjoint away from the
middle layer.

The actual global selection lemma debits both old-bank interference and
repeated new targets. With N_q=binom(2b,b-q), it gives, for each sign,

    E fresh_q >= theta*(W/R)*g_q
      *[1-(K_2/theta)*(W/N_q)*(o_q+g_q/2)/R],

where theta=1-o(1), K_2=1+o(1). On x=q/h in [1/2,1], the bracket is
at least 3/64-o(1), uniformly, since

    exp(x^2/16)*(1-x/8)
      <=(1-x/8)/(1-x^2/16)<=61/64.

## Explicit gain constant and one common realization

Uniformly on this interval, g_q/R=x/4+o(1). Therefore the expected
total fresh count F_b at EITHER sign satisfies

    E F_b >= (3/64-o(1))*W*h*integral_(1/2)^1 (x/4) dx
          = (9/2048-o(1))*W*h.

Since W*h/4^b tends to 1/(4 sqrt(pi)),

    E F_b >= [9/(8192 sqrt(pi))-o(1)]*4^b.             (1)

The entire displayed rank range contains O(4^b) targets. The contribution
to this expectation from non-near-perfect matching outcomes is therefore
o(4^b). Some good near-perfect outcome retains the lower bound (1).
For every outcome, complementation bijects the two signed packet supports
and their fresh unions in this controlled band. Hence BOTH signs attain
the bound in the SAME good outcome, rather than in separately chosen words.

Finally pi<4 gives

    9/(8192 sqrt(pi)) > 9/16384 > 1/2000.

The strict gap absorbs the o(1) errors and proves the claimed constant
for all sufficiently large b. No explicit numerical threshold is claimed.

## Literal support and cost, not only a target inventory

The canonical derivative blocks retain every upper designated target and
exactly the lower designated targets with q<=H. All-rank tensor inclusion
therefore preserves their old actual designated support. Every remaining
source union has rank at most 2mh or at least 2b-2mh. One shared,
full-set-guarded listing of these extreme targets has exactly that support
and costs 2e_ext=o(W), where

    e_ext=2*sum_(j=0)^(2mh) binom(2b,j)-1=2^{o(b)}.

It insures all possible incidental losses and covers no gained target.
If n packets are selected and u=W-nR=o(W), a fixed guarded middle
completion costs 2u. The two words have the same exact total length

    n(M+2Ht+t)-1+2e_ext+2u
      =W+n(6N+2Ht+t)+u-1+2e_ext=(1+o(1))W.

The three relative active overheads are O(1/h), O(1/sqrt(m)), and
O(1/(mh)); each vanishes.

Optionally append the accepted o(W) far-rank repair beyond H, with a
full-set guard, to BOTH words. This repair may incidentally contain some
gained targets. A length-L word realizes at most L distinct targets of
one fixed rank, so its debit over the O(sqrt(b)) gain ranks is o(4^b).
Retain the stronger constant in (1) until after this debit; its strict
margin still yields 4^b/2000 per sign. This optional repair is not needed
for the main whole-support inclusion.

## What remains open

These words are not universal. The theorem gives one positive,
globally distinct, lossless augmentation with negligible length overhead.
It does not show that the gain can be repeated against the enlarged
support, nor that the remaining Gaussian-band holes have a cheap repair.
The full-cube coefficient 1.180703803847... is unchanged. In particular,
this theorem does not prove coefficient one or nu(k)=B(k).
